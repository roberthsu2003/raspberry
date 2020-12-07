#pip install Pillow
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import face_recognition
import picamera
import numpy as np
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
from firebase_admin.exceptions import FirebaseError
from datetime import datetime



class App():
    camera = picamera.PiCamera()
    face_path="captureFace.jpg"

    def __init__(self,window):
        # 初始化firebase Admin database
        cred = credentials.Certificate("/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-a7505a2201.json");
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'raspberryfirebase.appspot.com',
            'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
        });
        self.bucket = storage.bucket();
        self.cameraRef = db.reference('/iot20191126/camera')
        
        #相機初始化

        App.camera.resolution = (320, 240)
        self.output = np.empty((240, 320, 3), dtype=np.uint8)

        # Load a sample picture and learn how to recognize it.
        robert_image = face_recognition.load_image_file("robert.jpeg")
        obama_image = face_recognition.load_image_file("obama_small.jpg")

        self.obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        self.robert_face_encoding = face_recognition.face_encodings(robert_image)[0]
        # Initialize some variables
        face_locations = []
        face_encodings = []
        print("載入已知的大頭照")
        #顯示初始化
        #Button
        myFont = font.Font(family='Helvetica',size=20)
        btn = Button(window, text='臉部辦識',font=myFont, command=self.buttonClick).pack(expand=YES,fill=BOTH)

        #畫布初始化
        self.canvas = Canvas(window, width=320, height=240)
        #PhotoImage的實體一定要keep住,所有一定要使用self來保持參考，不然記憶體會回收
        self.img = ImageTk.PhotoImage(Image.open("loaded.jpg"))
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.pack()
        self.message = StringVar()
        Message(window,textvariable=self.message,bg='royalblue', fg='white',anchor=NW, width=100).pack(expand=YES,fill=BOTH)
        self.message.set('等待辦識中......')

    def buttonClick(self):
        self.message.set('辦識中......')
        # Grab a single frame of video from the RPi camera as a numpy array
        #辦識用
        App.camera.capture(self.output, format="rgb")
        #顯示用
        sleep(2)
        App.camera.capture(App.face_path);
        sleep(1)
        self.img = ImageTk.PhotoImage(Image.open(App.face_path))
        #更新canvas image
        self.canvas.itemconfig(self.image_on_canvas, image=self.img)

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(self.output)
        # print("Found {} faces in image.".format(len(face_locations)))
        face_encodings = face_recognition.face_encodings(self.output, face_locations)

        # Loop over each face found in the frame to see if it's someone we know.
        names = [];
        #如果是空的就沒有可以辦識的
        if len(face_encodings) == 0:
            self.message.set("沒有可以辦識的臉")
        else:
            #上傳圖片
            #抓現在時間
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%Y_%m_%d_%H_%M_%S")
            print('Current Timestamp : ', timestampStr)
            saveFileName = timestampStr + ".jpg"
            imageBlob = self.bucket.blob("camera/{:s}".format(saveFileName))
            try:
                imageBlob.upload_from_filename(filename=App.face_path, content_type="image/jpeg");
                print("uploaded")
                self.cameraRef.set(saveFileName)
            except:
                print("upload error")

        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([self.obama_face_encoding, self.robert_face_encoding],face_encoding)            
            
            if match[0]:
                names.append("美國前總統")
            elif match[1]:
                names.append("徐國堂")
            else:
                names.append("不認識的臉")

            self.message.set("我找到{}人: {}!".format(len(face_locations), ",".join(names)))


if __name__ == '__main__':
    window = Tk()
    window.title("Camera")
    #window.geometry("1024x810")
    window.configure(background="blue")
    app = App(window)
    window.mainloop()

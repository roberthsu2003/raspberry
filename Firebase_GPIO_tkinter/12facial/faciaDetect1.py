from tkinter import *
from PIL import ImageTk, Image
from picamera import PiCamera
from time import sleep;
import face_recognition

camera = PiCamera();

def takePicture():
    camera.resolution = (1024, 768);
    camera.start_preview();
    sleep(1);
    camera.capture(path);
    openImage = Image.open(path);
    img = ImageTk.PhotoImage(openImage);
    panel.configure(image=img);
    panel.image = img;
    
    known_image = face_recognition.load_image_file("trueFace.jpeg")
    unknown_image = face_recognition.load_image_file("foo.jpeg")

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    #print(results);
    if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")
    

if __name__ == "__main__":
    window = Tk();
    window.title("Camera");
    window.geometry("1024x810");
    window.configure(background="blue");
    path = "foo.jpeg"
    
    openImage = Image.open(path);
    img = ImageTk.PhotoImage(openImage);
    
    mainFrame = Frame(window);
    panel = Label(mainFrame, image=img, height=710, width=1024);
    panel.pack(fill=BOTH, expand = YES);
    Button(mainFrame,text="take picture", command=takePicture, height=30,width=100).pack();
    
    mainFrame.pack(expand=YES, fill=BOTH);
    window.mainloop();
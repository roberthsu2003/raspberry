import face_recognition
import picamera
import numpy as np
from tkinter import *
from time import sleep
from PIL import ImageTk, Image

class App:
    camera = picamera.PiCamera()
    face_path = 'captureFace.jpg'
    
    def __init__(self,window):
        #初始化相機
        App.camera.resolution = (320,240)
        self.output = np.empty((240,320,3),dtype=np.uint8)
        
        #load sample image
        robert_image = face_recognition.load_image_file('robert.jpeg')
        obama_image = face_recognition.load_image_file('obama_small.jpg')
        #初始化tkinter
        myFont = font.Font(family='Helvetica',size=20)
        btn = Button(window,text='臉部辨識',font=myFont,command=self.buttonClick).pack(expand=YES,fill=BOTH,padx=10,pady=10)
    
    def buttonClick(self):
        App.camera.capture(self.output, format='rgb') #辦識用的
        sleep(2)
        App.camera.capture(App.face_path) #辦識用的
        sleep(1)
        self.img = ImageTk.PhotoImage(Image.open(App.face_path))

if __name__ == '__main__':
    window = Tk()
    window.title("Camera")
    window.configure(background='lightgray')
    window.geometry("320x200")
    app = App(window)
    window.mainloop()

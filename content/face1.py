import face_recognition
import picamera
import numpy as np
from tkinter import *

class App:
    
    def __init__(self,window):
        myFont = font.Font(family='Helvetica',size=20)
        btn = Button(window,text='臉部辨識',font=myFont,command=self.buttonClick).pack(expand=YES,fill=BOTH,padx=10,pady=10)
    
    def buttonClick(self):
        print("userClick")

if __name__ == '__main__':
    window = Tk()
    window.title("Camera")
    window.configure(background='lightgray')
    window.geometry("320x200")
    app = App(window)
    window.mainloop()

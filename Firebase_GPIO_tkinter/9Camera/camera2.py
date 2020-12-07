'''
import
sudo pip3 install Pillow

import ImageTk
sudo apt-get install python3-pil python3-pil.imagetk
'''

from tkinter import *
from picamera import PiCamera
from PIL import Image, ImageTk  #python3 -m pip install Pillow
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

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
    try:
        imageBlob.upload_from_filename(filename=path,content_type = "image/jpg");
    except:
        print("upload error");

if __name__ == "__main__":
    window = Tk();
    window.title("Camera");
    window.geometry("1024x810");
    window.configure(background="#cccccc");
    path = "foo.jpg";
    #firebase init
    cred = credentials.Certificate("raspberryfirebase-firebase-adminsdk-q4ht6-1608c845ce.json");
    firebase_admin.initialize_app(cred,{
            'storageBucket':'raspberryfirebase.appspot.com'
        });
    bucket = storage.bucket();
    imageBlob = bucket.blob("camera/foo.jpg");
    imageBlob.download_to_filename(path);
    
    
    
    openImage = Image.open(path);
    img = ImageTk.PhotoImage(openImage);
    
    mainFrame = Frame(window);
    panel = Label(mainFrame, image=img, height=710, width=1024);
    
    panel.pack(fill=BOTH, expand=YES);
    button = Button(mainFrame,text="Picture",command=takePicture,height=100,width=100).pack();
    mainFrame.pack(fill=BOTH, expand=YES);
    window.mainloop();

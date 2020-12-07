from tkinter import *
from tkinter import font
from gpiozero import PWMLED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading


class App:
    '''這是app的class用來做控制pwm的介面'''
    
    def __init__(self,master):
        #init
        self.pin = 25
        self.master = master;
        self.led = PWMLED(self.pin);
        self.job = None;
        self.scaleValue = IntVar();
        cred = credentials.Certificate('../raspberryfirebase-firebase-adminsdk-q4ht6-296b3b1772.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://raspberryfirebase.firebaseio.com/'})
        self.pwmLedRef = db.reference('raspberrypi/PWM_Led')
        #interface
        mainFrame = Frame(master);
        subFrame = Frame(mainFrame,relief=GROOVE,borderwidth=2);
        
        title = Label(subFrame,text="PWM_LED").pack(pady=20);
        smallFont = font.Font(family="Helvetica",size=12);
        self.scale = Scale(subFrame,orient=HORIZONTAL,from_=0,to=100,tickinterval=10,font=smallFont,command=self.userUpdateValue,variable=self.scaleValue);
        self.scale.pack(expand=YES,fill=BOTH,padx=10,pady=10);
        subFrame.pack(expand=YES,fill = BOTH,padx=10,pady=10);
        mainFrame.pack(expand=YES,fill = BOTH);
        
        self.getFirebaseLedControl();
        
    def userUpdateValue(self,event):
        if self.job:
            self.master.after_cancel(self.job);
        
        self.job = self.master.after(100,self.do_something);
    
    def do_something(self):
        value = self.scaleValue.get();
        try:
            self.pwmLedRef.update({'pwm_value': value});
        except:
            print("update failure");
    
    def getFirebaseLedControl(self):
        try:
            data = self.pwmLedRef.get();
            value = data['pwm_value'];
            print(value);
            self.scaleValue.set(value);
            self.led.value = value/100.0;
        except:
            print("get failure");
        
        threading.Timer(0.2,self.getFirebaseLedControl).start();
            


if __name__ == "__main__":
    tk = Tk();
    tk.title("PWMLED");
    tk.option_add("*font",("verdana",18,"bold"));
    tk.option_add("*background","#000000");
    tk.option_add("*foreground","#ffffff");
    tk.geometry("500x200");
    root = App(tk);
    tk.mainloop();
    

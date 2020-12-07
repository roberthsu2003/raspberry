from tkinter import *;
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from HR04 import HR04
from gpiozero import AngularServo;
import threading


class App:
    def __init__(self,master):
       self.master = master;
       self.valueVariable = IntVar();
       self.distanceValue = StringVar();
       #for firebase
       cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json');
       firebase_admin.initialize_app(cred, {'databaseURL': 'https://raspberryfirebase.firebaseio.com/'});
       self.servoRef = db.reference('raspberrypi/servo');
       #for HR04
       self.hr04 = HR04(23,24);
       
       #for servo
       self.servo = AngularServo(18,min_angle=0,max_angle=90);
       self.servo.angle = 0;
       #for tk
       mainFrame = Frame(self.master);
       servoFrame = Frame(mainFrame);
       borderFrame = Frame(servoFrame,borderwidth=2,relief=GROOVE,pady=30,padx=10);
       Label(servoFrame,text="Servo").place(relx=0.03,anchor=NW);
       self.button0 = Radiobutton(borderFrame,text="0",variable=self.valueVariable,value=0,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
       self.button25 = Radiobutton(borderFrame,text="25",variable=self.valueVariable,value=25,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
       self.button50 = Radiobutton(borderFrame,text="50",variable=self.valueVariable,value=50,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
       self.button75= Radiobutton(borderFrame,text="75",variable=self.valueVariable,value=75,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
       self.button90 = Radiobutton(borderFrame,text="90",variable=self.valueVariable,value=90,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
       borderFrame.pack(padx=10,pady=10);
       self.valueVariable.set(75);
       servoFrame.pack();
       
       #distance frame
       distanceFrame = Frame(mainFrame);
       Label(distanceFrame,textvariable = self.distanceValue).pack();
       self.distanceValue.set('distance:0cm');
       distanceFrame.pack();
       mainFrame.pack();
       
       #keep doing geting data
       self.distanceHandler();
       
       
       
    
    def changeDegree(self):
        self.angleValue = self.valueVariable.get();
        print("this value:{0:4d}".format(self.angleValue));
        try:
            self.servoRef.update({
                'angle':self.valueVariable.get()
                });
        except:
            print("update angel triger Error");
    
    def distanceHandler(self):
        self.angleHandler();
        try:
            distance = self.hr04.getCmDistance();
            if distance != None:
                self.distanceValue.set("distance:{0:3d}cm".format(distance));
                self.servoRef.update({'distance':distance});
        except:
            print('get distance is Error');
        finally:
            threading.Timer(1,self.distanceHandler).start();
    
    def angleHandler(self):
        servoValues = self.servoRef.get();
        angleValue = servoValues['angle'];
        self.servo.angle = angleValue;
        self.valueVariable.set(angleValue);
        

if __name__ == "__main__":
    root = Tk();
    root.title("Servo And HC-HR04");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    display = App(root);
    root.mainloop();

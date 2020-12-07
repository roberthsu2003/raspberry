from tkinter import *;
from gpiozero import MCP3008;
from gpiozero import DistanceSensor;
from gpiozero import AngularServo;
from threading import Timer;
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json')
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
    })
vrRef= db.reference('raspberrypi/vr');
disRef = db.reference('raspberrypi/dis');
print(vrRef.get());
class App:
    def __init__(self,window):
        self.vrText = StringVar();
        self.distanceValue = IntVar();
        self.gpioInit();
        mainFrame = Frame(window,borderwidth=2,relief=GROOVE);
        Label(mainFrame, text="可變電阻的值:").grid(row=0,column=0,padx=5,pady=20);
        Entry(mainFrame,width=16,state=DISABLED,textvariable=self.vrText).grid(row=0,column=1,padx=5,pady=20);
        
        Label(mainFrame, text="超音波距離:").grid(row=1,column=0,padx=5,pady=20);
        Entry(mainFrame,width=16,state=DISABLED,textvariable=self.distanceValue).grid(row=1,column=1,padx=5,pady=20);
        mainFrame.pack(padx=30,pady=30);
    
    def gpioInit(self):
        self.vrChannel = MCP3008(channel=7);
        self.distanceSensor = DistanceSensor(23, 24);
        self.servo = AngularServo(18,min_angle=-45,max_angle=45);
        self.servo.angle = 0.0;
        
        Timer(1,self.gpioAutoUpdate).start();
        
    def gpioAutoUpdate(self):
        #print("pot={}".format(self.vrChannel.value));
        vrValue = round(self.vrChannel.value,2);
        vrRef.set(vrValue);
        self.vrText.set("{:.0f}".format(self.vrChannel.value*100)) ;
        distanceValue = round(self.distanceSensor.distance*100,0);
        disRef.set(distanceValue);
        self.distanceValue.set(distanceValue);
        Timer(1,self.gpioAutoUpdate).start();
        
       

if __name__ == "__main__":
    window = Tk();
    window.title("MCP3008");
    window.option_add("*font",("verdana",18,"bold"));
    window.option_add("*background","#068587");
    window.option_add("*foreground", "#ffffff");
    root = App(window);
    window.mainloop();
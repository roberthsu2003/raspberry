from tkinter import *;
from HR04 import HR04;
import threading
from gpiozero import AngularServo;

class App:
    def __init__(self,master):
        self.hr04 = HR04(23,24);        
        self.servo = AngularServo(18,min_angle=0,max_angle=90);
        self.servo.angle=0;
        self.getDistance();
        
    def getDistance(self):
        distanceCm = self.hr04.getCmDistance();
        if distanceCm == None:
            print("over distance");
        elif distanceCm <= 6:
            self.servo.angle = 90;
        else:
            self.servo.angle = 0;
        
        threading.Timer(1,self.getDistance).start();

if __name__ == "__main__":
    root = Tk();
    root.title("Servo And HC-HR04");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    display = App(root);
    root.mainloop();
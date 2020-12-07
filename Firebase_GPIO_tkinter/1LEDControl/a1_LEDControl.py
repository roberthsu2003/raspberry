from tkinter import *
from gpiozero import LED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading

class App:
    
    def __init__(self,master):
        #初始化firebase Admin database
        cred = credentials.Certificate("raspberryfirebase-firebase-adminsdk-q4ht6-1608c845ce.json");
        firebase_admin.initialize_app(cred,{
            'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
        });

        #建立標題和最小大小
        master.title("LED Control");
        master.geometry("300x200+10+10");
        master.option_add("*Font",("verdana",18,"bold"));
        master.option_add("*Label.Font",("verdana",18));
        master.option_add("*Button.Background","dark gray");

        self.buttonText = StringVar();
        self.buttonText.set("OPEN");

        #led state
        self.ledState = "";

        #gpio led
        self.led=LED(25);
        
        #建立最外部的Frame
        self.mainFrame = Frame(master);
        self.mainFrame.pack(expand=YES,fill=BOTH);
        self.createSubFrame();

        #連線資料庫，取得資料
        self.ledControlRef = db.reference('raspberrypi/LED_Control')
        self.getFirebaseLedControl();
    
    def createSubFrame(self):
        subFrame = Frame(self.mainFrame,relief=GROOVE,borderwidth=2);
        titleLabel = Label(self.mainFrame,text="LED Control").place(relx=0.05,rely=0.025,anchor=NW);
        self.createButton(subFrame);
        subFrame.pack(expand=YES,fill=BOTH,padx=5,pady=20);
    
    

    def createButton(self,subFrame):
        button = Button(subFrame,textvariable=self.buttonText,command=self.userClick).pack(expand=YES,fill=BOTH,padx=40,pady=25);
        
    def userClick(self):
        
        if self.ledState == "OPEN":
            newState = "CLOSE";            
        else:
            newState = "OPEN";
        try:
            self.ledControlRef.update({'LED25': newState});
        except:
            print("update failure");
            return;
    
        
    def getFirebaseLedControl(self):
        try:
            data = self.ledControlRef.get();
        except (ValueError,ApiCallError):
            print("raise exception");
            threading.Timer(0.2,self.getFirebaseLedControl).start();
            return;
        except:
            print("raise exception");
            threading.Timer(0.2,self.getFirebaseLedControl).start();
            return;
        
        self.ledState = data['LED25'];
        if self.ledState == "OPEN":
            self.led.on();
            self.buttonText.set("LED CLOSE");
        elif self.ledState == "CLOSE":
            self.led.off();
            self.buttonText.set("LED OPEN");
        
        print("led25={0},date={1}".format(data['LED25'],data['date']));
        threading.Timer(0.2,self.getFirebaseLedControl).start();

if __name__ == "__main__":
    root = Tk();
    app = App(root);
    root.mainloop();


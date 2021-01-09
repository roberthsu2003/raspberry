# 1. LED Control

## 線路圖
![](a1_LEDControl_bb.png)

## function base with realtime database

```python
#! usr/bin/python3
import RPi.GPIO as GPIO
from tkinter import *

class App():
    def __init__(self, main):
        self.ledState = False
        main.title("Led Control")
        main.geometry("300x200")
        main.option_add("*Font",("verdana",18,"bold"))
        main.option_add("*Label.Font",("verdana",18))
        main.option_add("*Button.Background", "dark gray")
        mainFrame = Frame(main)
        self.button = Button(mainFrame,text="LED OPEN",padx=40,pady=40,command=self.userClick)
        self.button.pack(expand=YES)
        mainFrame.pack(expand=YES, fill=BOTH)

    def userClick(self):
        if self.ledState:
            self.ledState = False
            self.button.config(text = "LED 開")
            GPIO.output(25, GPIO.LOW)
        else:
            self.ledState = True 
            self.button.config(text = "LED 關")
            GPIO.output(25, GPIO.HIGH)

def on_closing():
    print("closing")
    GPIO.cleanup()
    window.destroy()   
    

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)

    window = Tk()
    app = App(window)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
```

## class base with firebase

```python
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


```

```python
from tkinter import *
from gpiozero import LED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class App:
    def __init__(self,window):
        self.led = LED(25);
        #firebase initial
        cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json');
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://raspberryfirebase.firebaseio.com/'});
        self.ledControlRef = db.reference('raspberrypi/LED_Control');
        self.ledControlRef.listen(self.firebaseDatachanges);
        
        
        #interface        #button_text
        self.buttonText = StringVar();
        
        mainFrame = Frame(window,borderwidth=2,relief=GROOVE);
        Label(window,text="LED Control").place(relx=0.05,rely=0.025,anchor=NW);
        Button(mainFrame,textvariable=self.buttonText,command=self.userClick).pack(expand=YES,fill=BOTH,padx=40,pady=25);
        self.buttonText.set("OPEN");
        mainFrame.pack(expand=YES,fill=BOTH,padx=5,pady=20);
        
        #ledControl
        #self.led = LED(25);
        self.led.off();
    
    def userClick(self):
        if self.buttonText.get() == "CLOSE":
            self.buttonText.set("OPEN");
            self.ledControlRef.update({"LED25":"CLOSE"});
        else:
            self.buttonText.set("CLOSE");
            self.ledControlRef.update({"LED25":"OPEN"});
    
    def firebaseDatachanges(self,event):
        print("Event type:{},Event path:{}".format(event.data,event.path));
        if event.path == "/" :
            if event.data['LED25'] == "OPEN":
                self.led.on();
            elif event.data['LED25'] == "CLOSE":
                self.led.off();
        elif event.path == "/LED25":
            if event.data == "OPEN":
                self.led.on();
            elif event.data == "CLOSE":
                self.led.off();

        

if __name__ == "__main__":
    window = Tk();
    window.title("LED Control");
    window.geometry("300x200");
    window.option_add("*Font",("verdana",18,"bold"));
    window.option_add("*Label.Font",("verdana",18));
    window.option_add("*Button.Background","dark gray");
    app = App(window);
    window.mainloop();

```

```python
from tkinter import *

def ledClose():
    print("ledClose");
    
def ledOpen():
    print("ledOpen");

def appInterface(window):
    frame = Frame(window,borderwidth=1,relief=GROOVE);
    Label(frame,
          text="LED Controler",
          font=("Helvetica", 20)
          ,anchor=W).pack(fill=X);
    
    Button(frame,text="open",
           pady=50,
           font=("Helvetica", 20),
           command=ledOpen).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(frame,text="close"
           ,pady=50,           
           font=("Helvetica", 20),command=ledClose).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    frame.pack(padx=10,pady=10,fill=X);
    
    rgbFrame = Frame(window,borderwidth=1,relief=GROOVE);
    Button(rgbFrame,text="RED"
           ,pady=50,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(rgbFrame,text="GREEN"
           ,pady=50,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(rgbFrame,text="BLUE"
           ,pady=50,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    rgbFrame.pack(padx=10,pady=10,fill=X);
    
    numberFrame = Frame(window,borderwidth=1,relief=GROOVE);
    Button(numberFrame,text="1"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(numberFrame,text="2"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(numberFrame,text="3"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    Button(numberFrame,text="4"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    Button(numberFrame,text="5"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    numberFrame.pack(padx=10,pady=10,fill=X);


if __name__ == '__main__':
    app = Tk();
    
    app.title("LEDControl");
    app.geometry("500x600");
    app.option_add("*Button.Background","#007A9B");
    app.option_add("*Button.Foreground","white");
    appInterface(window=app);
    app.mainloop();
```

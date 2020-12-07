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

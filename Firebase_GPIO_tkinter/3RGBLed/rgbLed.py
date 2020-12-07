from gpiozero import RGBLED;
from tkinter import *;
import firebase_admin
from firebase_admin import credentials;
from firebase_admin import db;
import threading;

class App:
    def __init__(self,root):
        #initial firebase
        cred = credentials.Certificate("raspberryfirebase-firebase-adminsdk-q4ht6-1608c845ce.json");
        firebase_admin.initialize_app(cred,{'databaseURL':'https://raspberryfirebase.firebaseio.com/'});
        self.rgbRef = db.reference('raspberrypi/RGB_LED');
        #initial rgbLed
        self.rgbLed = RGBLED(red=22,green=27,blue=17);
        self.rgbLed.red = 1;
        self.rgbLed.green = 1;
        self.rgbLed.blue = 1;
        
        self.redScaleValue = IntVar();
        self.greenScaleValue = IntVar();
        self.blueScaleValue = IntVar();
        
        mainFrame = Frame(root,width=700,height=400);
        #leftFrame
        leftFrame = Frame(mainFrame,bg="#bbbbbb",width=200);
        resultCanvas = Canvas(leftFrame,width=200,height=200,bg="#bbbbbb");
        rectangleItem = resultCanvas.create_rectangle(15,15,185,185,fill="blue");
        resultCanvas.pack(side=LEFT);
        leftFrame.pack(side=LEFT);
        
        #rightFrame
        rightFrame = Frame(mainFrame, bg="#bbbbbb",width=500);
        
        #red
        redLabel = Label(rightFrame,text="Red",fg="red",justify=LEFT).pack(fill=X,pady=10);
        self.redScale = Scale(rightFrame,from_=0,to=255,orient=HORIZONTAL,length=500,bg="red",foreground="white",relief=FLAT,borderwidth=0,command=self.redChange,variable=self.redScaleValue);
        self.redScale.pack(fill=X,pady=10,padx=5);
        self.redScale.bind("<ButtonPress>",self.buttonPress);
        self.redScale.bind("<ButtonRelease>",self.buttonRelease);
        
        #green
        greenLabel = Label(rightFrame,text="Green",fg="green",justify=LEFT).pack(fill=X,pady=10);
        self.greenScale = Scale(rightFrame,from_=0,to=255,orient=HORIZONTAL,length=500,bg="green",foreground="white",command=self.greenChange,relief=FLAT,borderwidth=0,variable=self.greenScaleValue);
        self.greenScale.pack(fill=X,pady=10,padx=5);
        self.greenScale.bind("<ButtonPress>",self.buttonPress);
        self.greenScale.bind("<ButtonRelease>",self.buttonRelease);
        
        #blue
        blueLabel = Label(rightFrame,text="Blue",fg="blue",justify=LEFT).pack(fill=X,pady=10);
        self.blueScale = Scale(rightFrame,from_=0,to=255,orient=HORIZONTAL,length=500,bg="blue",foreground="white",relief=FLAT,borderwidth=0,command=self.blueChange,variable=self.blueScaleValue);
        self.blueScale.pack(fill=X,pady=10,padx=5);
        self.blueScale.bind("<ButtonPress>",self.buttonPress);
        self.blueScale.bind("<ButtonRelease>",self.buttonRelease);
        
        rightFrame.pack(side=LEFT,expand=YES,fill=BOTH);
        
        mainFrame.pack(expand=YES,fill=BOTH);
        threading.Timer(0.2,self.getFirebaseRGBLed).start();
        
        
        
    
    def buttonPress(self,event):
        print("buttonPress");
        
    
    def buttonRelease(self,event):
        self.sendToFirebase();
    
    def redChange(self,event):
        pass;
        
    
    def greenChange(self,event):
        pass;
    
    def blueChange(self,event):
        pass;
        
    def sendToFirebase(self):
        self.rgbRef.update({
            'red':self.redScaleValue.get(),
            'green':self.greenScaleValue.get(),
            'blue':self.blueScaleValue.get()
        });
        
    def getFirebaseRGBLed(self):
        try:
            rgbData = self.rgbRef.get();
        except:
            threading.Timer(0.2,self.getFirebaseRGBLed).start();
            return;
        
        redValue = rgbData['red'];
        greenValue = rgbData['green'];
        blueValue = rgbData['blue'];  
            
        redPercent = 1-(redValue/255);
        print(redPercent);
        self.rgbLed.red = redPercent;
        self.redScaleValue.set(redValue);
        
        greenPercent = 1-(greenValue/255);
        print(greenPercent);
        self.rgbLed.green = greenPercent;
        self.greenScaleValue.set(greenValue);
        
        bluePercent = 1-(blueValue/255);
        print(bluePercent);
        self.rgbLed.blue = bluePercent;
        self.blueScaleValue.set(blueValue);
        
        threading.Timer(0.2,self.getFirebaseRGBLed).start();

if __name__ == "__main__":
    root = Tk();
    root.geometry("700x400");
    root.title("RBG_LED");
    root.option_add("*Font",("Helvetica", 18, "bold"));
    root.option_add("*background","#bbbbbb");
    display = App(root);
    print(type(display));
    root.mainloop();


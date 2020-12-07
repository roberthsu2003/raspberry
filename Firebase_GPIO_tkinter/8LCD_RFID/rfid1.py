'''
https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/
'''
from MFRC522 import MFRC522
import signal
from tkinter import *
import RPi.GPIO as GPIO
import threading
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import datetime

def end_read(signal, frame):
    print("ctrl+c captured, ending read.");
    GPIO.cleanup()
    sys.exit(0)

class App:
    MIFAREReader = MFRC522();
    preUid0 = 0;
    preUid1 = 0;
    preUid2 = 0;
    preUid3 = 0;
    
    def __init__(self,window):
        #fireStore
        cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json')
        firebase_admin.initialize_app(cred)
        self.firestoreDb = firestore.client()
        
        #tkinter
        self.window = window;
        self.mainFrame = Frame(window);
        docs = self.firestoreDb.collection('門禁資料1').order_by('datatime',direction=firestore.Query.DESCENDING).limit(5).get();
        for (index,doc) in enumerate(docs):
            Label(self.mainFrame,text=doc.get('uid'),width=20).grid(row=index,column=0,sticky=W);
            Label(self.mainFrame,text=doc.get('datatime'),width=20).grid(row=index,column=1,sticky=W);
        self.mainFrame.pack();
        
        secondFrame = Frame(window);
        listbox = Listbox(secondFrame);
        listbox.pack();
        secondFrame.pack();
        
        #interrupt
        signal.signal(signal.SIGINT, end_read);
        
        #rfid init
        self.rfid_sensor();
    
    def rfid_sensor(self):
        #checkuid
        uid = [];
        
        (status,TagType) = App.MIFAREReader.MFRC522_Request(App.MIFAREReader.PICC_REQIDL)
        if status == App.MIFAREReader.MI_OK:
            print("Card detected")
        
        # Get the UID of the card
        (status,uid) = App.MIFAREReader.MFRC522_Anticoll()
        
        if status == App.MIFAREReader.MI_OK:
            uid0 = uid[0];
            uid1 = uid[1];
            uid2 = uid[2];
            uid3 = uid[3];
            
            if uid0 != App.preUid0 or uid1 != App.preUid1 or uid2 != App.preUid2 or uid3 != App.preUid3:
                App.preUid0 = uid0;
                App.preUid1 = uid1;
                App.preUid2 = uid2;
                App.preUid3 = uid3;
                
                print("check card");
                uidString = str(uid0) + "," + str(uid1) + "," + str(uid2) + "," + str(uid3);
                print(uidString);
                
                #save to firestore
                t = time.time();
                date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S");
                newDoc_ref = self.firestoreDb.collection('門禁資料1').document(str(t))
                newDoc_ref.set({'datatime':date,'uid':uidString})
                
                #firestore
                #add Car Infomation
                
                carInfoRefs = self.firestoreDb.collection('卡片資訊1').where('cardID', '==', uidString).get();
                i = 0;
                for carInfo in carInfoRefs:
                    i += 1;
                    print("Card="+carInfo.get('cardID'));
                
                if i==0:
                    newCard = self.firestoreDb.collection('卡片資訊1').document();
                    newCard.set({'cardID':uidString});
                
                if self.mainFrame != None:
                    self.mainFrame.pack_forget();
                
                self.mainFrame = Frame(self.window);
                docs = self.firestoreDb.collection('門禁資料1').order_by('datatime',direction=firestore.Query.DESCENDING).limit(5).get();
                
                for (index,doc) in enumerate(docs):
                    Label(self.mainFrame,text=doc.get('uid'),width=20).grid(row=index,column=0,sticky=W);
                    Label(self.mainFrame,text=doc.get('datatime'),width=20).grid(row=index,column=1,sticky=W);
                self.mainFrame.pack();
        
                
        
        threading.Timer(1,self.rfid_sensor).start();
    
        

if __name__ == "__main__":
    root = Tk();
    root.title("RFID");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    
    GPIO.setwarnings(False)
    app = App(root);
    
    root.mainloop();


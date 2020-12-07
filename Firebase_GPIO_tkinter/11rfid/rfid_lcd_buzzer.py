<<<<<<< HEAD
from tkinter import *
from threading import Timer
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from lcd_display import lcd as Lcd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import firestore

import time
import datetime






class App:
    def __init__(self,window):
        #init firebase
        self.cred = credentials.Certificate('/home/pi/Documents/raspberryfirebase-firebase-adminsdk-q4ht6-3282b25b5b.json')
        firebase_admin.initialize_app(self.cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/',
    'databaseAuthVariableOverride': {'uid': 'NatxhTYp4AaiI2Uge648cNQjSIE3'}
    })
        self.firestore = firestore.client()

        #buzzer frame button
        buzzerFrame = Frame(window);
        Button(buzzerFrame,text="Buzzer Control", padx=10, pady=10,command=self.userClickBuzzer).pack(expand=YES, fill=BOTH,padx=30,pady=10);
        buzzerFrame.pack(expand=YES, fill=BOTH);
        
        #lcd frame
        Label(window,text="validate").pack(padx=10,pady=20,expand=YES, fill=BOTH);
        lcdFrame = Frame(window);
        self.entryString1 = StringVar();
        self.entryString2 = StringVar();
        
        #grid
        #entry1Frame
        
        Label(lcdFrame,text="name").grid(row=0, column=0, sticky=W,padx=5,pady=5);
        Entry(lcdFrame,textvariable=self.entryString1,width=16).grid(row=0, column=1, sticky=W,padx=5,pady=5);
        self.entryString1.set("First Line");
        
        Label(lcdFrame,text="pwd").grid(row=1, column=0, sticky=W,padx=5, pady=5);
        Entry(lcdFrame,textvariable=self.entryString2,width=16).grid(row=1, column=1, sticky=W,padx=5,pady=5);
        self.entryString2.set("Second Line");
        
        Button(lcdFrame,text="send",command=self.userClickSend,padx=10,pady=10).grid(row=2,column=0, columnspan=2,sticky=NSEW,padx=5,pady=5);
        lcdFrame.pack();
        
        #member frame
        Label(window,text="add Member").pack(padx=10,pady=20,expand=YES, fill=BOTH);
        memberFrame = Frame(window);
        self.entryString3= StringVar();
        self.entryString4 = StringVar();
        
        #grid
        #entry1Frame
       
        Label(memberFrame,text="name").grid(row=0, column=0, sticky=W,padx=5,pady=5);
        Entry(memberFrame,textvariable=self.entryString3,width=16).grid(row=0, column=1, sticky=W,padx=5,pady=5);
        self.entryString3.set("input Name");
        
        Label(memberFrame,text="card").grid(row=1, column=0, sticky=W,padx=5, pady=5);
        Entry(memberFrame,textvariable=self.entryString4,width=16).grid(row=1, column=1, sticky=W,padx=5,pady=5);
        self.entryString4.set("Second Line");
        
        Button(memberFrame,text="send",command=self.addMember,padx=10,pady=10).grid(row=2,column=0, columnspan=2,sticky=NSEW,padx=5,pady=5);
        memberFrame.pack();
        
        #buzzer init
        #self.buzzer = Buzzer(16);
        GPIO.setwarnings(False);
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(36,GPIO.OUT);
        self.buzzer = GPIO.PWM(36, 50);
        
        
        #lcd init
        self.lcd = Lcd()
        
        #rfid init
        self.uid = [];
        self.preUid0 = 0
        self.preUid1 = 0
        self.preUid2 = 0
        self.preUid3 = 0
        self.MIFAREReader = MFRC522.MFRC522();
        self.rfidHandler();
        
        #addMember 
        self.uid1 = [];
        self.preUid10 = 0
        self.preUid11 = 0
        self.preUid12 = 0
        self.preUid13 = 0
        
        
    def userClickBuzzer(self):
        print("user click");
        self.buzzer.start(100);
        
        t = Timer(0.1,self.closeBuzzer);
        t.start();
        
        
        
        
    
    def closeBuzzer(self):
        self.buzzer.stop();
    
    def userClickSend(self):
        '''
        entry1Words = self.entryString1.get();
        entry2Words = self.entryString2.get();
        self.lcd.display_string(entry1Words,1);
        self.lcd.display_string(entry2Words,2);
        '''
        try:
            entryEmail = self.entryString1.get();        
            user = auth.get_user_by_email(entryEmail);
            self.lcd.display_string(user.uid,1);
            self.lcd.display_string('success',2);
            print(user.uid);
        except:
            self.lcd.display_string('incorrect',1);
            self.lcd.display_string('who are you?',2);
            
    def rfidHandler(self):
        #scan for cards
        
        (status,tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL);
        
        if status == self.MIFAREReader.MI_OK:
            (status,self.uid) = self.MIFAREReader.MFRC522_Anticoll();
            if status == self.MIFAREReader.MI_OK:
                uid0 = self.uid[0]
                uid1 = self.uid[1]
                uid2 = self.uid[2]
                uid3 = self.uid[3]
                
                if uid0 != self.preUid0 or uid1 != self.preUid1 or uid2 != self.preUid2 or uid3 != self.preUid3:
                    self.preUid0 = uid0;
                    self.preUid1 = uid1;
                    self.preUid2 = uid2;
                    self.preUid3 = uid3;
                    uidString= str(uid0) + str(uid1) + str(uid2) + str(uid3)
                    
                    #firebase
                    member_ref = self.firestore.collection('members').document(uidString)
                    
                    print('uid:{}'.format(uidString));
                    try:
                        doc = member_ref.get()
                        print('Document data: {}'.format(doc.to_dict()))
                        current = time.time()
                        date = datetime.datetime.fromtimestamp(current).strftime("%Y-%m-%d-%H-%M-%S");
                        info = doc.to_dict()
                        print(info)
                        if info != None:
                            member = {
                                'id': uidString,
                                'timestamp': current,
                                'time': date,
                                'name': info["name"]
                            }
                            
                            self.firestore.collection('Door').document().set(member)
                            self.lcd.display_string("success",1);
                            
                    except:
                        pass

                    #lcd
                    self.lcd.display_string(uidString,1);
                    
                    #buzzer 
                    print(uidString);
                    self.buzzer.start(50)
                    self.buzzer.ChangeFrequency(3500)
                    time.sleep(0.1)
                    self.buzzer.stop();
                    #Timer(0.1,self.closeBuzzer).start();
        
                
                
        
        Timer(0.1,self.rfidHandler).start();
        
    def addMember(self):
        print("addMember")
        (status,tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL);
        
        if status == self.MIFAREReader.MI_OK:
            
            (status,self.uid1) = self.MIFAREReader.MFRC522_Anticoll();
            if status == self.MIFAREReader.MI_OK:
                
                uid0 = self.uid1[0]
                uid1 = self.uid1[1]
                uid2 = self.uid1[2]
                uid3 = self.uid1[3]
                
                if uid0 != self.preUid10 or uid1 != self.preUid11 or uid2 != self.preUid12 or uid3 != self.preUid13:
                    self.preUid10 = uid0;
                    self.preUid11 = uid1;
                    self.preUid12 = uid2;
                    self.preUid13 = uid3;
                    uidString= str(uid0) + str(uid1) + str(uid2) + str(uid3)
                    member_ref = self.firestore.collection('members').document(uidString)
                    print('uid:{}'.format(uidString));
                    try:
                        doc = member_ref.get()
                        print('Document data: {}'.format(doc.to_dict()))
                        current = time.time()
                        date = datetime.datetime.fromtimestamp(current).strftime("%Y-%m-%d-%H-%M-%S");
                        
                        if doc.to_dict() == None:
                            member = {
                                'id': uidString,
                                'timestamp': current,
                                'time': date,
                                'name': self.entryString3.get()
                            }
                            
                            self.firestore.collection('members').document(uidString).set(member)
                            self.lcd.display_string("success",1);
                        
                            
                    except google.cloud.exceptions.NotFound:
                        print('No such document!')
            
        

           
                    #lcd
                    
                    self.lcd.display_string(uidString,1);
                    
                    #buzzer 
                    print(uidString);
                    self.buzzer.start(100)
                    self.buzzer.ChangeFrequency(1452)
                    time.sleep(0.1)
                    self.buzzer.stop();
                    #Timer(0.1,self.closeBuzzer).start();

if __name__ == "__main__":
    root = Tk();
    root.title("RFID_LCD_BUZZER");
    root.option_add("*font",("verdana", 18));
    root.option_add("*background", "#cccccc");
    root.option_add("*forground","#888888");
    app = App(root);
=======
from tkinter import *
from threading import Timer
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from lcd_display import lcd as Lcd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import firestore

import time
import datetime






class App:
    def __init__(self,window):
        #init firebase
        self.cred = credentials.Certificate('/home/pi/Documents/raspberryfirebase-firebase-adminsdk-q4ht6-3282b25b5b.json')
        firebase_admin.initialize_app(self.cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/',
    'databaseAuthVariableOverride': {'uid': 'NatxhTYp4AaiI2Uge648cNQjSIE3'}
    })
        self.firestore = firestore.client()

        #buzzer frame button
        buzzerFrame = Frame(window);
        Button(buzzerFrame,text="Buzzer Control", padx=10, pady=10,command=self.userClickBuzzer).pack(expand=YES, fill=BOTH,padx=30,pady=10);
        buzzerFrame.pack(expand=YES, fill=BOTH);
        
        #lcd frame
        Label(window,text="validate").pack(padx=10,pady=20,expand=YES, fill=BOTH);
        lcdFrame = Frame(window);
        self.entryString1 = StringVar();
        self.entryString2 = StringVar();
        
        #grid
        #entry1Frame
        
        Label(lcdFrame,text="name").grid(row=0, column=0, sticky=W,padx=5,pady=5);
        Entry(lcdFrame,textvariable=self.entryString1,width=16).grid(row=0, column=1, sticky=W,padx=5,pady=5);
        self.entryString1.set("First Line");
        
        Label(lcdFrame,text="pwd").grid(row=1, column=0, sticky=W,padx=5, pady=5);
        Entry(lcdFrame,textvariable=self.entryString2,width=16).grid(row=1, column=1, sticky=W,padx=5,pady=5);
        self.entryString2.set("Second Line");
        
        Button(lcdFrame,text="send",command=self.userClickSend,padx=10,pady=10).grid(row=2,column=0, columnspan=2,sticky=NSEW,padx=5,pady=5);
        lcdFrame.pack();
        
        #member frame
        Label(window,text="add Member").pack(padx=10,pady=20,expand=YES, fill=BOTH);
        memberFrame = Frame(window);
        self.entryString3= StringVar();
        self.entryString4 = StringVar();
        
        #grid
        #entry1Frame
       
        Label(memberFrame,text="name").grid(row=0, column=0, sticky=W,padx=5,pady=5);
        Entry(memberFrame,textvariable=self.entryString3,width=16).grid(row=0, column=1, sticky=W,padx=5,pady=5);
        self.entryString3.set("input Name");
        
        Label(memberFrame,text="card").grid(row=1, column=0, sticky=W,padx=5, pady=5);
        Entry(memberFrame,textvariable=self.entryString4,width=16).grid(row=1, column=1, sticky=W,padx=5,pady=5);
        self.entryString4.set("Second Line");
        
        Button(memberFrame,text="send",command=self.addMember,padx=10,pady=10).grid(row=2,column=0, columnspan=2,sticky=NSEW,padx=5,pady=5);
        memberFrame.pack();
        
        #buzzer init
        #self.buzzer = Buzzer(16);
        GPIO.setwarnings(False);
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(36,GPIO.OUT);
        self.buzzer = GPIO.PWM(36, 50);
        
        
        #lcd init
        self.lcd = Lcd()
        
        #rfid init
        self.uid = [];
        self.preUid0 = 0
        self.preUid1 = 0
        self.preUid2 = 0
        self.preUid3 = 0
        self.MIFAREReader = MFRC522.MFRC522();
        self.rfidHandler();
        
        #addMember 
        self.uid1 = [];
        self.preUid10 = 0
        self.preUid11 = 0
        self.preUid12 = 0
        self.preUid13 = 0
        
        
    def userClickBuzzer(self):
        print("user click");
        self.buzzer.start(100);
        
        t = Timer(0.1,self.closeBuzzer);
        t.start();
        
        
        
        
    
    def closeBuzzer(self):
        self.buzzer.stop();
    
    def userClickSend(self):
        '''
        entry1Words = self.entryString1.get();
        entry2Words = self.entryString2.get();
        self.lcd.display_string(entry1Words,1);
        self.lcd.display_string(entry2Words,2);
        '''
        try:
            entryEmail = self.entryString1.get();        
            user = auth.get_user_by_email(entryEmail);
            self.lcd.display_string(user.uid,1);
            self.lcd.display_string('success',2);
            print(user.uid);
        except:
            self.lcd.display_string('incorrect',1);
            self.lcd.display_string('who are you?',2);
            
    def rfidHandler(self):
        #scan for cards
        
        (status,tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL);
        
        if status == self.MIFAREReader.MI_OK:
            (status,self.uid) = self.MIFAREReader.MFRC522_Anticoll();
            if status == self.MIFAREReader.MI_OK:
                uid0 = self.uid[0]
                uid1 = self.uid[1]
                uid2 = self.uid[2]
                uid3 = self.uid[3]
                
                if uid0 != self.preUid0 or uid1 != self.preUid1 or uid2 != self.preUid2 or uid3 != self.preUid3:
                    self.preUid0 = uid0;
                    self.preUid1 = uid1;
                    self.preUid2 = uid2;
                    self.preUid3 = uid3;
                    uidString= str(uid0) + str(uid1) + str(uid2) + str(uid3)
                    
                    #firebase
                    member_ref = self.firestore.collection('members').document(uidString)
                    
                    print('uid:{}'.format(uidString));
                    try:
                        doc = member_ref.get()
                        print('Document data: {}'.format(doc.to_dict()))
                        current = time.time()
                        date = datetime.datetime.fromtimestamp(current).strftime("%Y-%m-%d-%H-%M-%S");
                        info = doc.to_dict()
                        print(info)
                        if info != None:
                            member = {
                                'id': uidString,
                                'timestamp': current,
                                'time': date,
                                'name': info["name"]
                            }
                            
                            self.firestore.collection('Door').document().set(member)
                            self.lcd.display_string("success",1);
                            
                    except:
                        pass

                    #lcd
                    self.lcd.display_string(uidString,1);
                    
                    #buzzer 
                    print(uidString);
                    self.buzzer.start(50)
                    self.buzzer.ChangeFrequency(3500)
                    time.sleep(0.1)
                    self.buzzer.stop();
                    #Timer(0.1,self.closeBuzzer).start();
        
                
                
        
        Timer(0.1,self.rfidHandler).start();
        
    def addMember(self):
        print("addMember")
        (status,tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL);
        
        if status == self.MIFAREReader.MI_OK:
            
            (status,self.uid1) = self.MIFAREReader.MFRC522_Anticoll();
            if status == self.MIFAREReader.MI_OK:
                
                uid0 = self.uid1[0]
                uid1 = self.uid1[1]
                uid2 = self.uid1[2]
                uid3 = self.uid1[3]
                
                if uid0 != self.preUid10 or uid1 != self.preUid11 or uid2 != self.preUid12 or uid3 != self.preUid13:
                    self.preUid10 = uid0;
                    self.preUid11 = uid1;
                    self.preUid12 = uid2;
                    self.preUid13 = uid3;
                    uidString= str(uid0) + str(uid1) + str(uid2) + str(uid3)
                    member_ref = self.firestore.collection('members').document(uidString)
                    print('uid:{}'.format(uidString));
                    try:
                        doc = member_ref.get()
                        print('Document data: {}'.format(doc.to_dict()))
                        current = time.time()
                        date = datetime.datetime.fromtimestamp(current).strftime("%Y-%m-%d-%H-%M-%S");
                        
                        if doc.to_dict() == None:
                            member = {
                                'id': uidString,
                                'timestamp': current,
                                'time': date,
                                'name': self.entryString3.get()
                            }
                            
                            self.firestore.collection('members').document(uidString).set(member)
                            self.lcd.display_string("success",1);
                        
                            
                    except google.cloud.exceptions.NotFound:
                        print('No such document!')
            
        

           
                    #lcd
                    
                    self.lcd.display_string(uidString,1);
                    
                    #buzzer 
                    print(uidString);
                    self.buzzer.start(100)
                    self.buzzer.ChangeFrequency(1452)
                    time.sleep(0.1)
                    self.buzzer.stop();
                    #Timer(0.1,self.closeBuzzer).start();

if __name__ == "__main__":
    root = Tk();
    root.title("RFID_LCD_BUZZER");
    root.option_add("*font",("verdana", 18));
    root.option_add("*background", "#cccccc");
    root.option_add("*forground","#888888");
    app = App(root);
>>>>>>> 4ea6a5fdde087cc63439b9998cf5980402a059a5
    root.mainloop();
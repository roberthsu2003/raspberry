# RFID 和 LCD 和 蜂鳴器

## 線路圖
![](./rfid_bb.png)
### [LCD設定的網址](https://sites.google.com/site/zsgititit/home/raspberry-shu-mei-pai/raspberry-shi-yongi2c-kong-zhi2x16lcd)

## Raspberry使用 I2C 控制2*16 LCD
1. Raspberry啟用i2c
2. 連接Raspberry與LCD

| LCD | Raspberry Pi |
|:--|:--|
| Vcc | 5V |
| Gnd | Gnd |
| SDA | SDA |
| SCL | SCL |

3. 檢查Raspberry的i2c是否有連結到2x16LCD,並查尋address

```
$ i2cdetect -y l

結果:================
位址為:0x27
```

![](LCD1.jpg)

4. 下載Python[驅動程式](https://github.com/paulbarber/raspi-gpio)

```
$ git clone  https://github.com/paulbarber/raspi-gpio
$ cd raspi-gpio
$ vim lcd_display.py
將ADDRESS修改為0x27
```

5.python測試

```python
from lcd_display import lcd

my_lcd = lcd()
my_lcd.display_string("Raspberry Pi", 1)
my_lcd.display_string("Hello", 2)
```

### Raspberry 設定 RFID

#### 1. 在目錄的MFRC522.PY已經是Python3.0版
#### 2. pip install MFRC522(在虛擬環境安裝)
#### 3. 開啟raspberry的SPI介面

```
$ sudo raspi-config
```

#### 4. 安裝支援SPI的libraries

```
$ sudo apt-get install python3-spidev
```

#### 5. 安裝SPI-Py,會安裝在global

```
$ cd ~
$ git clone https://github.com/lthiery/SPI-Py.git
$ cd SPI-Py
$ sudo python3 setup.py install

```


#### 6.測試硬體，請先使用ready.py進行測試
```
#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

import RPi.GPIO as GPIO
import mfrc522 as MFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print ("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print ("Authentication error")


```

#### RFID 和 Firebase

```python
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


```

#### RFID LCD Firebase

```python
from LCD.lcd_display import lcd
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from tkinter import *
import sys
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import datetime

def on_closing():
    print("ctrl+c captured, ending read.")
    GPIO.cleanup()
    sys.exit(0)

class App():
    def __init__(self,window):
        #init fireStore
        cred = credentials.Certificate('/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-cf4be2ca1a.json')
        firebase_admin.initialize_app(cred)
        self.firestore = firestore.client()

        #init lcd
        self.my_lcd = lcd()


        #init Rfid
        self.previousUid = []
        self.MIFAREReader = MFRC522.MFRC522()
        self.rfidStatusHandler()


    def rfidStatusHandler(self):
        (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        if status == self.MIFAREReader.MI_OK:
            print("status success")
            self.my_lcd.display_string("status success", 1)
            self.my_lcd.display_string("..........", 2)
            self.cardRuning()
        else:
            self.my_lcd.display_string("Put On Card", 1)
            self.my_lcd.display_string("..........", 2)

        threading.Timer(3, self.rfidStatusHandler).start()

    def cardRuning(self):
        (status, currentUid) = self.MIFAREReader.MFRC522_Anticoll()
        if status == self.MIFAREReader.MI_OK and set(currentUid) != set(self.previousUid):
            self.previousUid = currentUid
            cardCode = ""
            for singleId in currentUid:
                cardCode += "{:x}.".format(singleId)

            self.my_lcd.display_string("Card ID:", 1)
            self.my_lcd.display_string(cardCode.upper(), 2)
            print(cardCode)
            self.saveToFireStore(cardCode)

    def saveToFireStore(self,cardCode):
        doc_ref = self.firestore.collection('Doors').document()
        currentTime = time.time()
        timestamp = datetime.datetime.fromtimestamp(currentTime)
        date = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        print(date)
        doc_ref.set({
            'timestamp':timestamp,
            'cardID': cardCode,
            'date':date
        })





    
    

if __name__ == "__main__":
    GPIO.setwarnings(False);
    root = Tk()
    root.title("RFID_LCD")
    root.protocol("WM_DELETE_WINDOW",on_closing)
    app = App(root)
    root.mainloop()

```

#### RFID LCD Buzzer Firebase

```python
from LCD.lcd_display import lcd
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from tkinter import *
import sys
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import datetime

def on_closing():
    print("ctrl+c captured, ending read.")
    GPIO.cleanup()
    sys.exit(0)

class App():
    def __init__(self,window):
        #init fireStore
        cred = credentials.Certificate('/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-cf4be2ca1a.json')
        firebase_admin.initialize_app(cred)
        self.firestore = firestore.client()

        #init lcd
        self.my_lcd = lcd()


        #init Rfid
        self.previousUid = []
        self.MIFAREReader = MFRC522.MFRC522()
        self.rfidStatusHandler()


    def rfidStatusHandler(self):
        (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        if status == self.MIFAREReader.MI_OK:
            print("status success")
            self.my_lcd.display_string("status success", 1)
            self.my_lcd.display_string("..........", 2)
            self.cardRuning()
        else:
            self.my_lcd.display_string("Put On Card", 1)
            self.my_lcd.display_string("..........", 2)

        threading.Timer(3, self.rfidStatusHandler).start()

    def cardRuning(self):
        (status, currentUid) = self.MIFAREReader.MFRC522_Anticoll()
        if status == self.MIFAREReader.MI_OK and set(currentUid) != set(self.previousUid):
            self.previousUid = currentUid
            cardCode = ""
            for singleId in currentUid:
                cardCode += "{:x}.".format(singleId)

            self.my_lcd.display_string("Card ID:", 1)
            self.my_lcd.display_string(cardCode.upper(), 2)
            print(cardCode)
            self.saveToFireStore(cardCode)

    def saveToFireStore(self,cardCode):
        doc_ref = self.firestore.collection('Doors').document()
        currentTime = time.time()
        timestamp = datetime.datetime.fromtimestamp(currentTime)
        date = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        print(date)
        doc_ref.set({
            'timestamp':timestamp,
            'cardID': cardCode,
            'date':date
        })





    
    

if __name__ == "__main__":
    GPIO.setwarnings(False);
    root = Tk()
    root.title("RFID_LCD")
    root.protocol("WM_DELETE_WINDOW",on_closing)
    app = App(root)
    root.mainloop()

```



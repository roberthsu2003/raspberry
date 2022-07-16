import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import time

import tkinter as tk
from tkinter import ttk 
import RPi.GPIO as GPIO
import sys
import mfrc522 as MFRC522


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #---------------Firebase realtime database 初始化---------------
        cred = credentials.Certificate("firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-0eebb63a53.json")
        firebase_admin.initialize_app(cred)
        self.firestore = firestore.client()

        #----------------init Rfid--------------------------
        self.previousUid = []
        self.MIFAREReader = MFRC522.MFRC522()
        self.rfidStatusHandler()
        
        

        #-----------建立tkinter----------------------        
        self.title("python視窗和FireStore資料庫")
        mainFrame  = tk.Frame(self, relief="groove", borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame,text="python視窗和FireStore資料庫\n\nRFID系統",font=("Arial",15),fg="#555555").pack(padx=10)
        titleFrame.pack(pady=30)
        mainFrame.pack(pady=30,padx=30,ipadx=30,ipady=30) 
        
        #-------------建立labelFrame-------------------
        labelFrame = tk.Frame(mainFrame,width=50)        
        
        self.num1Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        self.num1Label.pack(side=tk.LEFT,padx=(0,5))

        self.num2Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        self.num2Label.pack(side=tk.LEFT,padx=(0,5))

        self.num3Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        self.num3Label.pack(side=tk.LEFT,padx=(0,5))

        self.num4Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        self.num4Label.pack(side=tk.LEFT,padx=(0,5))

        self.num5Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        self.num5Label.pack(side=tk.LEFT,padx=(0,5))       
        labelFrame.pack(pady=10)
       
        #-----------------建立TreeView-----------------------
        columns = ['#1','#2','#3','#4','#5','#6']
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.heading('#1',text='時間')
        self.tree.heading('#2',text='號碼1')
        self.tree.heading('#3',text='號碼2')
        self.tree.heading('#4',text='號碼3')
        self.tree.heading('#5',text='號碼4')
        self.tree.heading('#6',text='號碼5')       
        self.tree.column('#1',width=200)
        self.tree.column('#2',width=50)
        self.tree.column('#3',width=50)
        self.tree.column('#4',width=50)
        self.tree.column('#5',width=50)
        self.tree.column('#6',width=50)        
        self.tree.pack()
        
        #建立realtime update
        self.callback_done = threading.Event()
        ##每次只取得最新的10筆
        query_ref = self.firestore.collection('Doors').order_by('date',direction=firestore.Query.DESCENDING).limit(10)       
        ##註冊callback
        col_watch = query_ref.on_snapshot(self.on_snapshot)

    def on_snapshot(self,doc_snapshot, changes, read_time):
        # 清除tree內容
        for i in self.tree.get_children():
            self.tree.delete(i) 
        #這是firestore的callback,doc_snapshot參數是list,只有10筆,順序必需相反   
        doc_snapshot.reverse()   
        for doc in doc_snapshot:
            print(doc.__class__)
            print(f'接收到的資料:{doc.id}')
            #更新treeView資料
            data_time = doc.get('date')          
            numsString = doc.get('cardID')
            nums = numsString.split('.')
            self.tree.insert('',tk.END,values=[data_time] + nums)
        self.callback_done.set()


    
    def rfidStatusHandler(self):
        (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        if status == self.MIFAREReader.MI_OK:
            print("status success")            
            self.cardRuning()     
            
        threading.Timer(3, self.rfidStatusHandler).start()
    
    def cardRuning(self):
        (status, currentUid) = self.MIFAREReader.MFRC522_Anticoll()
        if status == self.MIFAREReader.MI_OK and set(currentUid) != set(self.previousUid):
            self.previousUid = currentUid
            cardCode = ""
            self.num1Label.configure(text=f'{currentUid[0]:x}')
            self.num2Label.configure(text=f'{currentUid[1]:x}')
            self.num3Label.configure(text=f'{currentUid[2]:x}')
            self.num4Label.configure(text=f'{currentUid[3]:x}')
            self.num5Label.configure(text=f'{currentUid[4]:x}')
            for singleId in currentUid:
                cardCode += "{:x}.".format(singleId)
                

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
        
        

def closeWindow():    
    GPIO.cleanup()
    sys.exit(0)
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.resizable(width=0,height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()


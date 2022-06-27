import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin.exceptions import FirebaseError
import random
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #---------------Firebase realtime database 初始化
        cred = credentials.Certificate("firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-e21c25a365.json")

        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.lotList = []
        
        

        #-----------建立tkinter----------------------        
        self.title("python視窗和FireStore資料庫")
        mainFrame  = tk.Frame(self, relief="groove", borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame,text="python視窗和FireStore資料庫\n\n大樂透電腦選號",font=("Arial",15),fg="#555555").pack(padx=10)
        titleFrame.pack(pady=30)
        mainFrame.pack(pady=30,padx=30,ipadx=30,ipady=30) 
        
        #-------------建立labelFrame-------------------
        labelFrame = tk.Frame(mainFrame,width=50)        
        
        num1Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        num1Label.pack(side=tk.LEFT,padx=(0,5))

        num2Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        num2Label.pack(side=tk.LEFT,padx=(0,5))

        num3Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        num3Label.pack(side=tk.LEFT,padx=(0,5))

        num4Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        num4Label.pack(side=tk.LEFT,padx=(0,5))

        num5Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        num5Label.pack(side=tk.LEFT,padx=(0,5))

        num6Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        num6Label.pack(side=tk.LEFT,padx=(0,5))

        num7Label = tk.Label(labelFrame,text='00',font=("Arial",15))
        num7Label.pack(side=tk.LEFT,padx=(0,5))
        labelFrame.pack(pady=10)

        #-------------------ButtonFrame---------------------
        buttonFrame = tk.Frame(mainFrame,width=50)        
        tk.Button(buttonFrame,text="更新",padx=20,pady=10,command=lambda:self.lot_update([num1Label,num2Label,num3Label,num4Label,num5Label,num6Label,num7Label])).pack(side=tk.LEFT)

        tk.Button(buttonFrame,text="送出",padx=20,pady=10,command=self.submit).pack(side=tk.LEFT)        
        buttonFrame.pack(pady=10)

    def lot_update(self,labels):
        lot = set()
        while(len(lot) < 7):
            rValue = random.randint(1, 49)
            lot.add(rValue)
        self.lotList = list(lot)
        for i,num in enumerate(self.lotList):
            label = labels[i]
            label.configure(text=str(num).zfill(2))

    def submit(self):
        print(self.lotList)
        data = {
            'lotos':self.lotList,
            'datetime':datetime.now(tz=timezone(timedelta(hours=8)))
        }
        now = datetime.now()
        document_name = now.strftime('%Y-%m-%d_%H:%M:%S')
        self.db.collection('loto').document(document_name).set(data)
        
        


    
def closeWindow():
    print("close window")
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.resizable(width=0,height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()


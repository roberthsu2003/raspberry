import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin.exceptions import FirebaseError

import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #---------------Firebase realtime database 初始化
        cred = credentials.Certificate("firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-e21c25a365.json")

        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
        })

        self.ref = db.reference('raspberrypi/Radiobutton')
        

        #-----------建立tkinter----------------------

        self.radio_item_value = tk.IntVar()
        self.title("python視窗和Firebase及時資料庫")
        mainFrame  = tk.Frame(self, relief="groove", borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame,text="python視窗和Firebase及時資料庫",font=("Arial",20,'bold'),fg="#555555").pack(padx=10)
        titleFrame.pack(pady=30)
        mainFrame.pack(pady=30,padx=30,ipadx=30,ipady=30)
    
        #-------------建立inputFrame-------------------
        inputFrame = tk.Frame(mainFrame,width=50)
        red=tk.Radiobutton(inputFrame, text='紅燈', value=1, variable=self.radio_item_value,command=self.getEvent,font=("Arial",15)).pack(side=tk.LEFT)
        
        green=tk.Radiobutton(inputFrame, text='綠燈', value=2, variable=self.radio_item_value,command=self.getEvent,font=("Arial",15)).pack(side=tk.LEFT)
        blue=tk.Radiobutton(inputFrame, text='藍燈', value=3, variable=self.radio_item_value,command=self.getEvent,font=("Arial",15)).pack(side=tk.LEFT)
        inputFrame.pack()

        #註冊完後,會立刻執行一次，所以放在最後面比較好
        try:
            self.ref.listen(self.colorChanged)
        except FirebaseError as e:
            print(e)

    def getEvent(self):        
        self.ref.set({
            'color':self.radio_item_value.get()
        })

    def colorChanged(self,event):
        #print(event.path)
        #print(event.data)
        self.radio_item_value.set(event.data['color'])

        


def closeWindow():
    print("close window")
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.resizable(width=0,height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()


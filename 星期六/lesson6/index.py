import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from gpiozero import RGBLED

led = RGBLED(red=22, green=27, blue=17)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #----------- Firebase RealTime DataBase 初始化--------------
        cred = credentials.Certificate('firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-e21c25a365.json')

        firebase_admin.initialize_app(cred, {
                    'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
        })
        self.ref = db.reference('raspberrypi/Radiobutton')        
        mainFrame = tk.Frame(self, relief="groove", borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame,text="python視窗和Firebase及時資料庫_RGBLED",font=("Arial",20),fg="#555555").pack(padx=10)
        titleFrame.pack(pady=30)
        mainFrame.pack(padx=30, pady=30, ipadx=30, ipady=30)

        #-----------建立inputFrame-----------------------
        inputFrame = tk.Frame(mainFrame)
        self.radion_item_value = tk.IntVar()
        tk.Radiobutton(inputFrame,text="紅燈",value=1,variable=self.radion_item_value,font=("Arial",15),command=self.getEvent).pack(side=tk.LEFT)
        tk.Radiobutton(inputFrame,text="綠燈",value=2,variable=self.radion_item_value,font=("Arial",15),command=self.getEvent).pack(side=tk.LEFT)
        tk.Radiobutton(inputFrame,text="藍燈",value=3,variable=self.radion_item_value,font=("Arial",15),command=self.getEvent).pack(side=tk.LEFT)
        inputFrame.pack()
        
        self.ref.listen(self.colorChanged)
        

    def getEvent(self):
        #print(self.radion_item_value.get())
        self.ref.child('color').set(self.radion_item_value.get())

    def colorChanged(self,event):
        value = event.data
        self.radion_item_value.set(value)
        if value == 1:
            led.color = (1,0,0)
        elif value == 2:
            led.color = (0,1,0)
        elif value == 3:
            led.color = (0,0,1)

def closeWindow():
    print("close window")
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.title("python視窗和Firebase及時資料庫")
    window.resizable(width=0, height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()
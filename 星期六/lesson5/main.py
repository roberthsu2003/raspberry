import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk
import tk_tools




class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        cred = credentials.Certificate('firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-e21c25a365.json')
        firebase_admin.initialize_app(cred,{
            'databaseURL':'https://raspberryfirebase.firebaseio.com/'
        })

        self.ref = db.reference('raspberry2022')
        self.ref.listen(self.switch_light)    
        self.led = tk_tools.Led(self, size=50)       
        self.led.pack()
        tk.Button(self, text="SWITCH",command=self.buttonClick).pack(padx=5, pady=8)
        

    def switch_light(self,event):
        led_state =  self.ref.get()['led']
        if led_state == False:
            self.led.to_grey()
        else:
            self.led.to_green()

    def buttonClick(self):
        value  =  not self.ref.get()['led']
        self.ref.update({'led':value})


if __name__ == "__main__":
    window = Window()
    window.title("LED控制")
    window.geometry("300x300")
    window.mainloop()

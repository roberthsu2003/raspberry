import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk
import tk_tools

cred = credentials.Certificate('firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-e21c25a365.json')

firebase_admin.initialize_app(cred,{
    'databaseURL':'https://raspberryfirebase.firebaseio.com/'
})

ref = db.reference('raspberry2022')


class Window(tk.Tk):
    def __init__(self):
        super().__init__()        
        self.led = tk_tools.Led(self, size=50)       
        self.led.pack()
        tk.Button(self, text="SWITCH",command=self.buttonClick).pack(padx=5, pady=8)
        

    def switch_light(self):
        led_state =  ref.get()
        if led_state == False:
            self.led.to_grey()
        else:
            self.led.to_green()

    def buttonClick(self):
        value  =  not ref.get()['led']
        ref.update({'led':value})


if __name__ == "__main__":
    window = Window()
    window.title("LED控制")
    window.geometry("300x300")
    window.mainloop()

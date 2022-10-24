import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("private/raspberry1-58efc-firebase-adminsdk-tzk5o-2743aa1e4a.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://raspberry1-58efc-default-rtdb.firebaseio.com/'
})

led = db.reference('ledControl')

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立title
        self.title("LED Controller")
        #建立按鈕
        self.btn = tk.Button(self,text="開關",padx=50,pady=30,font=('arial',18),command=self.userClick)
        self.btn.pack(padx=50,pady=30)
        currentState = led.get()['led']
        if currentState:
           self.btn.config(text="關")
        else:
           self.btn.config(text="開")
    
    def userClick(self):
        currentState = led.get()['led']
        led.update({'led':not currentState})
        if currentState:
           self.btn.config(text="開")
        else:
           self.btn.config(text="關")


def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()
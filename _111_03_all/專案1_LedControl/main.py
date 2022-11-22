import tkinter as tk
import firebase_admin
import RPi.GPIO as GPIO
from firebase_admin import credentials
from firebase_admin import db
from tools import LightButton

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

        self.btn = LightButton(self,padx=50,pady=30,command=self.userClick)
        self.btn.pack(padx=50,pady=30)
        currentState = led.get()['led']
        if currentState:
           self.btn.light_state = True
           GPIO.output(25,GPIO.HIGH)
        else:
           self.btn.light_state = False
           GPIO.output(25,GPIO.LOW)
    
    def userClick(self):
        currentState = led.get()['led']
        led.update({'led':not currentState})
        if currentState:
           self.btn.light_state = False
           GPIO.output(25,GPIO.LOW)
        else:
           self.btn.light_state = True
           GPIO.output(25,GPIO.HIGH)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25,GPIO.OUT)
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()
# 1. LED Control

## 線路圖
![](a1_LEDControl_bb.png)

## 使用Rpi.GPIO,tkinter

```python
#! usr/bin/python3
import RPi.GPIO as GPIO
from tkinter import *

class App():
    def __init__(self, main):
        self.ledState = False
        main.title("Led Control")
        main.geometry("300x200")
        main.option_add("*Font",("verdana",18,"bold"))
        main.option_add("*Label.Font",("verdana",18))
        main.option_add("*Button.Background", "dark gray")
        mainFrame = Frame(main)
        self.button = Button(mainFrame,text="LED OPEN",padx=40,pady=40,command=self.userClick)
        self.button.pack(expand=YES)
        mainFrame.pack(expand=YES, fill=BOTH)

    def userClick(self):
        if self.ledState:
            self.ledState = False
            self.button.config(text = "LED 開")
            GPIO.output(25, GPIO.LOW)
        else:
            self.ledState = True 
            self.button.config(text = "LED 關")
            GPIO.output(25, GPIO.HIGH)

def on_closing():
    print("closing")
    GPIO.cleanup()
    window.destroy()   
    

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)

    window = Tk()
    app = App(window)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
```

## firebas_database只有單獨更新資料
```python
#! usr/bin/python3
import RPi.GPIO as GPIO
from gpiozero import LED
from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class App():
    def __init__(self, main):
        #firebase
        cred = credentials.Certificate("/home/pi/raspberryfirebase-firebase-adminsdk-y4f0x-ce1ddd9e4b.json")
        firebase_admin.initialize_app(cred,{
            'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
            })
        self.ledControlRef = db.reference('raspberrypi/LED_Control')
        

        #tkinter
        self.ledState = False
        main.title("Led Control")
        main.geometry("300x200")
        main.option_add("*Font",("verdana",18,"bold"))
        main.option_add("*Label.Font",("verdana",18))
        main.option_add("*Button.Background", "dark gray")
        mainFrame = Frame(main)
        self.button = Button(mainFrame,text="LED OPEN",padx=40,pady=40,command=self.userClick)
        self.button.pack(expand=YES)
        mainFrame.pack(expand=YES, fill=BOTH)

    def userClick(self):
        if self.ledState:
            self.ledState = False
            self.ledControlRef.update({"LED25":"CLOSE"})
            self.button.config(text = "LED 開")
            bigLed.off()
        else:
            self.ledState = True 
            self.button.config(text = "LED 關")
            self.ledControlRef.update({"LED25":"OPEN"})
            bigLed.on()

def on_closing():
    print("closing")
    GPIO.cleanup()
    window.destroy()
    

if __name__ == '__main__':
    bigLed = LED(25)

    window = Tk()
    app = App(window)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
```

## 使用Rpi.GPIO,tkinter,自訂Button Class,使用LED圖片檔

```python
import tkinter as tk
from PIL import Image,ImageTk
import firebase_admin
import RPi.GPIO as GPIO
from firebase_admin import credentials
from firebase_admin import db



class LightButton(tk.Button):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        #建立圖片
        ##建立close的圖片
        close_image = Image.open('light_close.png')
        self.close_photo = ImageTk.PhotoImage(close_image)
        ##建立open的圖片
        open_image = Image.open('light_open.png')
        self.open_photo = ImageTk.PhotoImage(open_image)
        self.config(borderwidth=0)
        self.config(state="disabled")
        

    def open(self):
        self.config(image=self.open_photo)
        

    def close(self):
        self.config(image=self.close_photo);
        

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立firebase 連線
        cred = credentials.Certificate("private1/raspberry1-58efc-firebase-adminsdk-tzk5o-2743aa1e4a.json")
        firebase_admin.initialize_app(cred,{
            'databaseURL': 'https://raspberry1-58efc-default-rtdb.firebaseio.com/'
        })

        led = db.reference('ledControl')       

        #建立title
        self.title("LED Controller")

        #建立按鈕

        self.btn = LightButton(self,padx=50,pady=30)
        self.btn.pack(padx=50,pady=30)
        currentState = led.get()['led']
        if currentState:
           self.btn.open()
           GPIO.output(25,GPIO.HIGH)
        else:
           self.btn.close()
           GPIO.output(25,GPIO.LOW)

        #註冊監聽
        #監聽必需在最後面
        led.listen(self.firebaseDataChange)
    
    def firebaseDataChange(self,event):
        print(f"資料內容:{event.data}")
        print(f"資料路徑:{event.path}")
        if event.path == "/":
            state = event.data['led']
        elif event.path ==  "/led":
            state = event.data
        
        if state:
            self.btn.open()
            GPIO.output(25,GPIO.HIGH)
        else:
            self.btn.close()
            GPIO.output(25,GPIO.LOW)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25,GPIO.OUT)
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()
```


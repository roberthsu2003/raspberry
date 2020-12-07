#!/usr/bin/python3.7
'''
MCP3008 , 可變電阻, pwmLed
程式重點
1程式每0.2秒會執行一次method
2.只有可變電阻值改變時才會執行程式
3.值快速連續改變非常多次時，只執行最後一次，這樣就可以最後一次才update firebase內的資料，而不是快速連續多次的更新
'''

from gpiozero import MCP3008
from tkinter import *
from threading import Timer
from gpiozero import PWMLED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


channel0 = MCP3008(0)
led = PWMLED(18)

class App():
    def __init__(self,win):
        #firebase realtimedataBase_PWM
        self.master = win
        self.job = None
        self.outputValue = 0
        cred = credentials.Certificate('/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-cf4be2ca1a.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
        })
        self.pwmRef = db.reference('iot20191126/PWM')
        print(self.pwmRef)
        #tkinter
        self.displayValue = IntVar()
        mainFrame = Frame(win,borderwidth=2,relief=GROOVE)
        displayBar = Scale(mainFrame, from_=0, to=100, orient=HORIZONTAL, variable=self.displayValue,length=300)
        displayBar.pack()
        mainFrame.pack()
        self.displayValue.set(50)
        self.auotUpdate()
        
    def userCreateJob(self):
        #這裏的寫法是連續快速執行時，只執行最後一次
        print("userCreateJob")
        if self.job:
            self.master.after_cancel(self.job);        
        self.job = self.master.after(500,self.firebaseDoSomeThing)
    
    def firebaseDoSomeThing(self):
        print('doSomethine')
        self.pwmRef.update({'value':self.displayValue.get()})

    def auotUpdate(self):
        #print('update')
        outputValue = int(channel0.value * 100)
        #只有先前的值有改變，才會執行if內的程式
        if self.outputValue != outputValue:
            self.outputValue = outputValue
            self.userCreateJob()
            
        led.value = channel0.value
        self.displayValue.set(outputValue)
        try:
            Timer(0.2,self.auotUpdate).start()
            #self.pwmRef.update({'value':outputValue})       
            
        except:
            print("error")
            Timer(0.2, self.auotUpdate).start()

if __name__ == '__main__':
    window = Tk()
    window.title("MCP3008_可變電阻")
    window.option_add("*font",('verdana',18,'bold'))
    window.option_add('*background','#333333')
    window.option_add('*foreground','#ffffff')
    app = App(window)
    window.mainloop()

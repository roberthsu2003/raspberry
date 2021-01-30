from tkinter import *
from gpiozero import MCP3008
from threading import Timer
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Linebox():
    def __init__(self,w):
        #firebase
        cred = credentials.Certificate("/home/pi/raspberryfirebase-firebase-adminsdk-y4f0x-ce1ddd9e4b.json")
        firebase_admin.initialize_app(cred,{
            'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
            })
        self.mcp3008Ref = db.reference('raspberrypi/MCP3008')

        #設定視窗基本功能
        w.title('溫度和光線的感應')
        w.option_add("*font",("verdana",18,"bold"))
        w.option_add("*background", "#068587")
        w.option_add("*foreground", "#ffffff")

        #建立sensor
        self.lightness = MCP3008(channel=7)
        self.temperature = MCP3008(channel=6)
        self.m = MCP3008(channel=0)

        #設定介面變數
        self.temperatureText = StringVar()
        self.lightnessText = StringVar()
        self.mvariable = StringVar()

        #設定介面
        mainFrame = Frame(w,borderwidth=2,relief=GROOVE,padx=100,pady=10)
        Label(mainFrame, text="室內溫度:").grid(row=0, column=0, sticky=E, padx=5, pady=20)
        Label(mainFrame, text="室內光線:").grid(row=1, column=0, sticky=E, padx=5, pady=20)
        Label(mainFrame, text="可變電阻:").grid(row=2, column=0, sticky=E, padx=5, pady=20)
        Label(mainFrame, textvariable=self.temperatureText).grid(row=0, column=1, sticky=E, padx=5, pady=20)
        Label(mainFrame, textvariable=self.lightnessText).grid(row=1, column=1, sticky=E, padx=5, pady=20)
        Label(mainFrame, textvariable=self.mvariable).grid(row=2, column=1, sticky=E, padx=5, pady=20)
        mainFrame.pack(padx=10, pady=10)
        self.autoUpdate()
       

        

    def autoUpdate(self):
        #改變介面變數值
        self.tempValue = self.temperature.value * 3.3 * 100
        self.temperatureText.set('%.0f' % self.tempValue)
        self.lightValue = self.lightness.value * 100
        self.lightnessText.set('%.0f' % self.lightValue)
        self.mValue = self.m.value * 100
        self.mvariable.set('%.0f' % self.mValue)

        self.mcp3008Ref.update({
            'brightness':self.lightValue,
            'temperature':self.tempValue,
            'm1':self.mValue
        })
        Timer(1, self.autoUpdate).start()

    def getInfo(self):
        return (self.mValue,self.tempValue,self.lightValue)

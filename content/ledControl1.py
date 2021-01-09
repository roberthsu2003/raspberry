#! usr/bin/python3
import RPi.GPIO as GPIO
from gpiozero import LED
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
            bigLed.off()
        else:
            self.ledState = True 
            self.button.config(text = "LED 關")
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
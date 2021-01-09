#! usr/bin/python3
import RPi.GPIO as GPIO
from tkinter import *

class App():
    def __init__(self, main):
        main.title("Led Control")
        main.geometry("300x200")
        main.option_add("*Font",("verdana",18,"bold"))
        main.option_add("*Label.Font",("verdana",18))
        main.option_add("*Button.Background", "dark gray")
        mainFrame = Frame(main)
        Button(mainFrame,text="LED").pack()
        
        mainFrame.pack(expand=YES, fill=BOTH)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    #GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)

    window = Tk()
    app = App(window)
    window.mainloop()
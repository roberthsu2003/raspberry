#! usr/bin/python3
import RPi.GPIO as GPIO
from tkinter import *

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)

    window = Tk()
    window.mainloop()
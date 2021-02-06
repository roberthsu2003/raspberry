import RPi.GPIO as GPIO
from tkinter import *

class App():
    def __init__(self,window):
        pass

def on_closing():
    root.destroy()

if __name__ == "__main__":
    GPIO.setwarnings(False)
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = App(root)
    root.mainloop()

import RPi.GPIO as GPIO
from raspigpio.lcd_display import lcd
from tkinter import *
import mfrc522 as MFRC522
import threading

class App():
    def __init__(self,window):
        #初始化lcd
        self.my_lcd = lcd()

        #初始化RFID
        self.MIFAREReader= MFRC522.MFRC522()
        self.rfidStatusHandler()
    
    def rfidStatusHandler(self):
        print('偵測rfid')
        threading.Timer(1, self.rfidStatusHandler).start()

def on_closing():
    GPIO.cleanup()
    root.destroy()

if __name__ == "__main__":
    GPIO.setwarnings(False)
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = App(root)
    root.mainloop()

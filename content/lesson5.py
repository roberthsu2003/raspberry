import RPi.GPIO as GPIO
from raspigpio.lcd_display import lcd
from tkinter import *
import mfrc522 as MFRC522
import threading
import sys
from time import sleep
from gpiozero import Buzzer

class App():
    def __init__(self,window):
        #初始化lcd
        self.my_lcd = lcd()

        #初始化RFID
        self.MIFAREReader= MFRC522.MFRC522()
        self.rfidStatusHandler()

        #初始化buzzer
        self.my_buzzer = Buzzer(16)
    
    def rfidStatusHandler(self):
        (status, tagType)= self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        if status == self.MIFAREReader.MI_OK:
            print("Find Card")
            self.my_lcd.display_string("Find Card",1)
            self.my_lcd.display_string("......",2)
            #buzzer sound()
            self.my_buzzer.on()
            sleep(0.2)
            self.my_buzzer.off()

        else:
            print("Put Car on It")
            self.my_lcd.display_string("Put Car on It",1)
            self.my_lcd.display_string("",2)
        threading.Timer(1, self.rfidStatusHandler).start()

def on_closing():
    GPIO.cleanup()
    root.destroy()
    sys.exit()

if __name__ == "__main__":
    GPIO.setwarnings(False)
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = App(root)
    root.mainloop()

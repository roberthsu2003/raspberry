from tkinter import *
import RPi.GPIO as GPIO
from YourBox import Linebox
from threading import Timer
import requests

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

def on_closing():
    print("close")    
    window.destroy()
    GPIO.cleanup()

def sendLineMessage(m, t, l):
    paras = {'value1':format(m,'.2f'),
             'value2':format(l,'.2f')   
            }
    response = requests.get("https://maker.ifttt.com/trigger/over30/with/key/eDqcZfqY_i_BHCZVXCwb6aq7GLPKpdV4q1ePja35Mjq",
                params = paras,
                headers = header
               )
    print("sendLine") 
           
def checkValue():
    m,tem,lightness = rgbLed.getInfo()
    if m > 90:
        sendLineMessage(m, tem, lightness)
    Timer(60,checkValue).start()

if __name__ == "__main__":
    window = Tk()
    rgbLed = Linebox(window)
    checkValue()    
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()
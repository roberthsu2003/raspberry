from gpiozero import RGBLED, Button, MCP3008
from signal import pause
from random import random
from threading import Timer

def user_press():
    print("user Press")
    r = random()
    g = random()
    b = random()
    led.color = (r,g,b)

def user_release():
    print("user Release")
    led.color = (0,0,0)

def system_repeat():
    mValue = m1.value
    print('可變電阻值',mValue)
    led.color = (0,0,mValue)
    Timer(0.1,system_repeat).start()

if __name__ == '__main__':
    button = Button(pin=18)
    led = RGBLED(red=17, green=27, blue=22)
    m1 = MCP3008(0)    
    system_repeat()
    
    button.when_pressed = user_press
    button.when_released = user_release
pause()

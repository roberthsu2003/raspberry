from gpiozero import RGBLED, Button
from signal import pause
from random import random

def user_press():
    print("user Press")
    r = random()
    g = random()
    b = random()
    led.color = (r,g,b)

def user_release():
    print("user Release")
    led.color = (0,0,0)

if __name__ == '__main__':
    button = Button(pin=18)
    led = RGBLED(red=17, green=27, blue=22)
    button.when_pressed = user_press
    button.when_released = user_release


pause()

#http://stupidpythonideas.blogspot.com/2013/10/why-your-gui-app-freezes.html
from gpiozero import RGBLED,Button
from time import sleep
from signal import pause
from random import randint

def user_press():
    r = randint(0,100) / 100;
    g = randint(0,100) / 100;
    b = randint(0,100) / 100;
    print("R={},G={},B={}".format(r,g,b));
    led.color = (r, g, b);

button = Button(18);
led = RGBLED(red=17, green=27, blue=22);

button.when_pressed = user_press;
pause();

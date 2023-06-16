from gpiozero import Button,RGBLED
from signal import pause
from random import randint

button = Button(18)
led = RGBLED(red=17, green=27, blue=22);
def user_press():
    r = randint(0,100) / 100;
    g = randint(0,100) / 100;
    b = randint(0,100) / 100;
    print("R={},G={},B={}".format(r,g,b));
    led.color = (r, g, b);
    

button.when_pressed = user_press;
pause()
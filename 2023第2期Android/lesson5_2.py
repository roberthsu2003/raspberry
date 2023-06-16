from gpiozero import Button,RGBLED
from signal import pause
from random import randint
state = False
button = Button(18)
led = RGBLED(red=17, green=27, blue=22);

def user_press():
    global state;
    state = not state;
    if state:
        r = randint(0,100) / 100;
        g = randint(0,100) / 100;
        b = randint(0,100) / 100;
        print("R={},G={},B={}".format(r,g,b));
        led.color = (r, g, b);
    else:
        led.color = (0, 0, 0);
    

button.when_pressed = user_press;
pause()
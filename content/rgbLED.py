from gpiozero import RGBLED, Button
from signal import pause

def user_press():
    print("user Press")

if __name__ == '__main__':
    button = Button(pin=18)
    button.when_pressed = user_press

pause()

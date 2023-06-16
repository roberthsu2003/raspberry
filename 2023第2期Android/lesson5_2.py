from gpiozero import Button
from signal import pause
button = Button(18)
def user_press():
    print("User pressed")

button.when_pressed = user_press;
pause()
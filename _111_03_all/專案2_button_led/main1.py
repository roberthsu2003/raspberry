from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

button = Button(18)

button.when_pressed = say_hello
button.when_released = say_goodbye

pause()
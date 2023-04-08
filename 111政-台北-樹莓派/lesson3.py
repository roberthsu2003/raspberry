import private
import requests

#url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttKey}?value1=31c&value2=51'

#r = requests.get(url)
#if r.status_code == 200:
#    print("發送成功")

from gpiozero import Button
from signal import pause
from gpiozero import RGBLED

state = False

def user_press():
    global state
    state = not state
    if state == True:
        print("開燈")
        led.color=(1,0,0)
    else:
        print("關燈")
        led.color=(0,0,0)

button = Button(18)
led = RGBLED(red=17, green=27, blue=22)

button.when_pressed = user_press

pause()
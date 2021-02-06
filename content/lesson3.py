from raspigpio.lcd_display import lcd
from gpiozero import Buzzer
from time import sleep

my_lcd = lcd()
my_lcd.display_string("Raspberry Pi", 1)
my_lcd.display_string("Hello!", 2)
my_buzzer = Buzzer(16)

while True:
    sleep(10)
    my_buzzer.on()
    sleep(0.2)
    my_buzzer.off()
    
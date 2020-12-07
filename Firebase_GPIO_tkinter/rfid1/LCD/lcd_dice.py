#!/usr/bin/python

import random
from time import sleep
import RPi.GPIO as GPIO
from lcd_display import lcd

# use Pi board pin numbers with GPIO.BOARD
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# see http://elinux.org/Rpi_Low-level_peripherals
# see http://pypi.python.org/pypi/RPi.GPIO

def flash(d):
      GPIO.output(11, False)
      sleep(d)
      GPIO.output(11, True)
      sleep(d)

disp = lcd()
disp.display_string("Raspi Dice      ", 1)
disp.display_string("                ", 2)

flash(0.2)
flash(0.2)

while True:

  go = not(GPIO.input(7))
  stop = not(GPIO.input(12))

  if go:

    # wait for button release
    while go:
      go = not(GPIO.input(7))

    disp.display_string("Throwing ...    ", 2)

    # get a random number from 0 to 6 and convert to int for use with range
    r = int(random.random()*6)+1
#    print (r)
    for x in range(0, r):
      flash(0.2)
    
    text = "You Threw a " + str(r) + "   "
    disp.display_string(text, 2)


  if stop:

    disp.display_string("Goodbye        ", 2)
    flash(0.5)
    GPIO.cleanup()
#    print ("goodbye")

    disp.clear()
    exit()

  sleep(0.1)

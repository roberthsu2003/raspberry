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
disp.display_string("Raspi Dice 4      ", 1)
disp.display_string("                ", 2)

flash(0.2)
flash(0.2)

n = 0

while True:

  go = not(GPIO.input(7))
  stop = not(GPIO.input(12))

  if go:

    # wait for button release
    while go:
      go = not(GPIO.input(7))

    disp.display_string("Raspi Dice 4      ", 1)
    disp.display_string("Throwing ...    ", 2)

    # get a random number from 0 to 6 and convert to int for use with range
    r = int(random.random()*6)+1
#    print (r)
    for x in range(r):
      flash(0.2)

    n+=1

    if n==4:
      r4 = r
      total = r1+r2+r3+r4
      if (total<10):
        disp.display_string("Too Bad :---(   ", 2)
      elif (total<14):
        disp.display_string("Ok do better :-|", 2)
      elif (total==14):
        disp.display_string("You're average ~", 2)
      elif (total<14):
        disp.display_string("Ok do better :-|", 2)
      elif (total<14):
        disp.display_string("Ok do better :-|", 2)
      elif (total<18):
        disp.display_string("Above Average:-)", 2)
      else:
        disp.display_string("Wow! Awesome :-D", 2)
      n=0

      text = "%d+%d+%d+%d = %d      " % (r1, r2, r3, r4, total)

    elif n==1:
      r1 = r
      text = "%d               " % (r1)
    elif n==2:
      r2 = r
      text = "%d+%d             " % (r1, r2)
    elif n==3:
      r3 = r
      text = "%d+%d+%d           " % (r1, r2, r3)

    disp.display_string(text, 1)
    if n!=0: # 0 = finished game
      disp.display_string("Throw again ...  ", 2)


  if stop:

    disp.display_string("Goodbye        ", 2)
    flash(0.5)
    GPIO.cleanup()
#    print ("goodbye")

    disp.clear()
    exit()

  sleep(0.1)

#!/usr/bin/python

import time
import random
import RPi.GPIO as GPIO

# use Pi board pin numbers with GPIO.BOARD
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
# see http://elinux.org/Rpi_Low-level_peripherals
# see http://pypi.python.org/pypi/RPi.GPIO

while True:
  # get a random number from 0 to 10 and convert to int for use with range
  r = int(random.random()*10)+1
  print r
  for x in range(0, r):
    GPIO.output(11, False)
    time.sleep(0.2)
    GPIO.output(11, True)
    time.sleep(0.2)

  time.sleep(2)

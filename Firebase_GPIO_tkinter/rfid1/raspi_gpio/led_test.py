#!/usr/bin/python

import time
import random
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
  GPIO.output(17, False)
  time.sleep(random.random()/5)
  GPIO.output(17, True)
  time.sleep(random.random()/5)



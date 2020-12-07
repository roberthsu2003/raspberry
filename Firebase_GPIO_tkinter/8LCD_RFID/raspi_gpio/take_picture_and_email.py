#!/usr/bin/python

import os
import time
import random
import RPi.GPIO as GPIO
from send_gmail_attachment import sendMailWithAttachments
from lcd_display import lcd

def flash(d):
      GPIO.output(11, False)
      time.sleep(d)
      GPIO.output(11, True)
      time.sleep(d)

# use Pi board pin numbers with GPIO.BOARD
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# see http://elinux.org/Rpi_Low-level_peripherals
# see http://pypi.python.org/pypi/RPi.GPIO

# initialise the lcd display
lcd1 = lcd()
lcd1.clear()
lcd1.display_string("Picture Taker", 1)

flash(0.2)
flash(0.2)

while True:

  # Check camera is present
  while not os.path.exists('/dev/video0'):
    lcd1.display_string("No Camera", 2)
    time.sleep(1.0)

  lcd1.display_string("ready", 2)

  go = not(GPIO.input(7))
  stop = not(GPIO.input(12))

  if go:

    # wait for button release
    while go:
      go = not(GPIO.input(7))

    print "taking picture"
    lcd1.clear()
    lcd1.display_string("taking picture", 2)
    for x in range(2):
        flash(0.2)
      
    filename = "webcam%s.jpg" % (time.strftime('%d%b%H%M%S'))
    pathname = "/home/pi/pictures/" + filename
    command = "fswebcam -r 640x480 " + pathname
    os.system(command)

    if os.path.isfile(pathname):
        print "picture ok"
        lcd1.display_string("picture ok", 2)
        flash(0.2)
        time.sleep(0.5)

        print "Emailing"
        lcd1.display_string("emailing", 2)
        sendMailWithAttachments( ["email@server.co.uk"],
                                "Image from the Raspberry Pi",
                                "Someone took a picture.",
                                [pathname] )
        lcd1.display_string("done", 2)
        flash(0.2)
        flash(0.2)
    else:
        print "picture failed"        
        lcd1.display_string("failed, sorry", 2)
        flash(0.5)

    time.sleep(0.5)
    lcd1.display_string("Picture Taker", 1)
    lcd1.display_string("ready", 2)
    print "Done"

  if stop:

    print "goodbye"
    lcd1.display_string("goodbye", 2)
    flash(0.5)
    lcd1.clear()
    lcd1.backlight_off()
    GPIO.cleanup()
    exit()

  time.sleep(0.1)

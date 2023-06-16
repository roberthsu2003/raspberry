#!/usr/bin/python3
import rgbLed
import RPi.GPIO as GPIO

if __name__ == '__main__':
    rgb = rgbLed.RGBLed(22,27,17)
    rgb.redLight()
    GPIO.cleanup()
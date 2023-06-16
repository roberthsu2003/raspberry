#!/usr/bin/python3
import rgbLed

if __name__ == '__main__':
    rgb = rgbLed.RGBLed(22,27,17)    
    rgb.blueLight(second=5)
    rgb.redLight(second=5)
    rgb.greenLight(second=5)   
    rgb.clean()
    
    
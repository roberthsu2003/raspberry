import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

class RGBLed():
    def __init__(self, red_pin, green_pin, blue_pin):        
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)
        self.red = GPIO.PWM(red_pin, 75)
        self.green = GPIO.PWM(green_pin, 75)
        self.blue = GPIO.PWM(blue_pin, 75)

    def redLight(self,second=3,forever=False):
        if forever:
            try:
                while(True):
                    self.red.start(75)
            except:
                self.red.stop()
                #GPIO.cleanup()
        else:                  
            self.red.start(75)
            sleep(second)
            self.red.stop()     

    def greenLight(self,second=3,forever=False):
            if forever:
                try:
                    while(True):
                        self.green.start(75)
                except:
                    self.green.stop()
                    #GPIO.cleanup()
            else:                  
                self.green.start(75)
                sleep(second)
                self.green.stop()

    def blueLight(self,second=3,forever=False):
            if forever:
                try:
                    while(True):
                        self.blue.start(75)
                except:
                    self.blue.stop()
                    #GPIO.cleanup()
            else:                  
                self.blue.start(75)
                sleep(second)
                self.blue.stop()
      
    def clean(self):
        GPIO.cleanup()

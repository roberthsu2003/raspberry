import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class RGBLed():
    def __init__(self, red_pin, green_pin, blue_pin):        
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)
        self.red = GPIO.PWM(red_pin, 75)
        self.green = GPIO.PWM(green_pin, 75)
        self.blue = GPIO.PWM(blue_pin, 75)

    def redLight(self):
        try:
            while(True):
                self.red.start(75)
        except KeyboardInterrupt:
            self.red.stop()

    def close(self):
        self.red.stop()
        self.blue.stop()
        self.green.stop()
        GPIO.cleanup()

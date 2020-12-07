import RPi.GPIO as GPIO
import time

pins = (4,17,27,22,23,24,25,18);
digits = {    
    0:(1,1,1,0,1,1,1,0),
    1:(1,0,0,0,1,0,0,0),
    2:(1,1,0,1,0,1,1,0),
    3:(1,1,0,1,1,1,0,0),
    4:(1,0,1,1,1,0,0,0),
    5:(0,1,1,1,1,1,0,0),
    6:(0,1,1,1,1,1,1,0),
    7:(1,1,1,0,1,0,0,0),
    8:(1,1,1,1,1,1,1,0),
    9:(1,1,1,1,1,0,0,0),
    }

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);


for n in pins:
    GPIO.setup(n,GPIO.OUT);

for num in range(0,10):
    numValues = digits[num]
    i = 0
    for pin in pins:        
        GPIO.output(pin,numValues[i]);
        i += 1;
    time.sleep(1);


GPIO.cleanup();

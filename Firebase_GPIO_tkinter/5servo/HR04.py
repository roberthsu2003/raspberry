import RPi.GPIO as GPIO
import time

class HR04(object):
    def __init__(self,trig,echo):
        GPIO.setmode(GPIO.BCM);
        GPIO.setwarnings(False);
        self.trig = trig;
        self.echo = echo;
        GPIO.setup(self.trig,GPIO.OUT);
        GPIO.setup(self.echo,GPIO.IN);
        print("run");

    def __str__():
        return "control HR04";

    def getCmDistance(self):
        try:
            GPIO.setmode(GPIO.BCM);
            GPIO.setup(self.trig,GPIO.OUT);
            GPIO.setup(self.echo,GPIO.IN);
            
            GPIO.output(self.trig,False);
            time.sleep(0.01);
            GPIO.output(self.trig,True);
            time.sleep(0.00001);
            GPIO.output(self.trig,False);

            while GPIO.input(self.echo) == 0:
                self.pulse_start = time.time();
            
            while GPIO.input(self.echo) == 1:
                self.pulse_end = time.time();

            pulse_duration = self.pulse_end - self.pulse_start;
            distance = pulse_duration * 17150;
            distance = round(distance);
            
            if distance < 2 or distance > 400:
                return None;
            else:
                return distance;
        except:
            
            return None;

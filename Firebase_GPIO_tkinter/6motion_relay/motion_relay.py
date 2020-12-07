from gpiozero import Buzzer
from gpiozero import MotionSensor
from gpiozero import LED as Relay
from time import sleep

def main():
    buzzer = Buzzer(pin=17);
    motionSensor = MotionSensor(pin=18,queue_len=5,sample_rate=120,threshold=0.2);
    relay = Relay(pin=23,active_high=False);
    """
    motionSensor.when_motion = relay.on;
    motionSensor.when_no_motion = relay.off;
    """
    while True:
        if motionSensor.motion_detected:
            print("active");
            if relay.is_lit != True:
                relay.on();
        else:
            print("inactive");
            if relay.is_lit != False:
                relay.off();
       

if __name__ == "__main__" :
    main();
    

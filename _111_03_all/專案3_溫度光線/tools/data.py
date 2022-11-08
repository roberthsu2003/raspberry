from gpiozero import MCP3008
from gpiozero import DistanceSensor

#gpio23 -> echo 220,220分壓
#gpio24 -> trig

sensor = DistanceSensor(23, 24)
lightValue = MCP3008(7)

def getDistance():
    return sensor.distance * 100;

def getLightValue():    
    print(f"光線:{lightValue.value * 1000:.1f}")
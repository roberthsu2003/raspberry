from gpiozero import MCP3008
from gpiozero import DistanceSensor

#gpio23 -> echo 220,220分壓
#gpio24 -> trig

sensor = DistanceSensor(23, 24)
lightValue = MCP3008(7)

def getDistance():    
    print("距離:",sensor.distance)

def getLightValue():    
    print("光線:",lightValue.value * 1000)
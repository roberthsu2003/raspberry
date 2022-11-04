from gpiozero import MCP3008
from gpiozero import DistanceSensor

sensor = DistanceSensor(23, 24)
lightValue = MCP3008(7)

def getDistance():    
    print("距離:",sensor.distance)

def getLightValue():    
    print("光線:",lightValue.value * 1000)
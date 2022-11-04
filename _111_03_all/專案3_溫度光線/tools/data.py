from gpiozero import MCP3008
from gpiozero import DistanceSensor

#gpio23 -> echo 220,220分壓
#gpio24 -> trig

sensor = DistanceSensor(23, 24)
lightValue = MCP3008(7)

def getDistance():
    if sensor.distance < 1.0: 
        print(f"距離:{sensor.distance*100:.2f}公分")
    else:
        print(f"距離:大於100公分")

def getLightValue():    
    print(f"光線:{lightValue.value * 1000:.1f}")
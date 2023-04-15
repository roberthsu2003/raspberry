import gpiozero
from time import sleep

mcp3008_light = gpiozero.MCP3008(channel=7)
mcp3008_temperature = gpiozero.MCP3008(channel=6)
buzzer = gpiozero.Buzzer(25)

while(True):    
    lightValue = round(mcp3008_light.value*1000)
    temperature = (mcp3008_temperature.value*1000)
    print(temperature)
    
    if lightValue < 40:
        buzzer.on()
    else:
        buzzer.off()
    sleep(1)


import gpiozero
from time import sleep

mcp3008 = gpiozero.MCP3008(channel=7)
buzzer = gpiozero.Buzzer(25)

while(True):    
    lightValue = round(mcp3008.value*1000)
    print(lightValue)
    if lightValue < 40:
        buzzer.on()
    else:
        buzzer.off()
    sleep(1)


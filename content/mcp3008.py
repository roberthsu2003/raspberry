from gpiozero import MCP3008
import time

lm35 = MCP3008(6)

while True:
    value = lm35.value
    print(value*3.3*100)
    time.sleep(1)
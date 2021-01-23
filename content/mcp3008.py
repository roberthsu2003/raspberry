from gpiozero import MCP3008
import time

lm35 = MCP3008(6)
m1 = MCP3008(7)

while True:
    value = lm35.value
    print('溫度:',value*3.3*100)
    value = m1.value
    print('可變電阻度:',value*100)
    time.sleep(1)
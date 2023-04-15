import gpiozero
from time import sleep
import requests

mcp3008_light = gpiozero.MCP3008(channel=7)
mcp3008_temperature = gpiozero.MCP3008(channel=6)
buzzer = gpiozero.Buzzer(25)


while(True):    
    lightValue = round(mcp3008_light.value*1000)
    temperature = round(mcp3008_temperature.value*3.3*100,ndigits=2)
    print(lightValue)
    print(temperature)
    url = f'https://blynk.cloud/external/api/batch/update?token=CyIs--o2qa7N1CV_6YeWv2WrvMqie9Qd&A0={lightValue}&V1={temperature}'
    response = requests.get(url)
    if response.ok :
        print('連線成功')

    if lightValue < 40:
        buzzer.on()
    else:
        buzzer.off()
    sleep(5)


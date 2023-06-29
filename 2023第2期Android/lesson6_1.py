import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import requests



if __name__ == "__main__":
    mcp3008_ch7 = zero.MCP3008(channel=7)
    mcp3008_ch6 = zero.MCP3008(channel=6)
    try:
        while True:
            value = round(mcp3008_ch7.value*100)
            print("光敏電阻値: ", value)
            if value > 20:
                print("光線亮")
            else:
                print("光線暗") 

            datetimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            response = requests.get(f'https://fastapi-g07j.onrender.com/raspberry?time={datetimeStr}&light={value}&temperature={mcp3008_ch6.value * 1000}')
            
            if response.ok:
                print("上傳資料成功")
                print(response.text)
            else:
                print(response.status_code)

            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程序退函数")

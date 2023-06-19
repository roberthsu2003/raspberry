import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep



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

            print("LM35",mcp3008_ch6.value*100*3.3)    

            sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程序退函数")

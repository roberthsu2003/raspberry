import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep



if __name__ == "__main__":
    mcp3008 = zero.MCP3008(channel=7)
    try:
        while True:
            value = round(mcp3008.value*100)
            print("光敏電阻値: ", value)
            if value > 20:
                print("光線亮")
            else:
                print("光線暗")           

            sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程序退函数")

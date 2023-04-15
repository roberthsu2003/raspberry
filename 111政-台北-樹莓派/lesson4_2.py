import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000

# 讀取某 channel 類比轉換出來的數位值，須了解MCP3008的資料交換機制
# 同時也要了解 Python 的位元運算方法，才可以理解這段程式
def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# 將資料值轉換為電壓值
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts

light_channel = 6
delay = 1

try:
    while True:
        light_level = ReadChannel(light_channel)
        light_volts = ConvertVolts(light_level, 2)

        print("--------------------------------------------")
        print("Light: {} ({}V)".format(light_level,light_volts))

        time.sleep(delay)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

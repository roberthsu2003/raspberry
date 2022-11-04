from gpiozero import MCP3008

def getTemperature():
    temperature = MCP3008(7)
    print(temperature.value*3.3*100)
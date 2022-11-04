from gpiozero import MCP3008
temperature = MCP3008(6,max_voltage=5)
lightValue = MCP3008(7,max_voltage=5)

def getTemperature():    
    print("溫度:",temperature.value * 5 * 100)

def getLightValue():    
    print("光線:",lightValue.value * 1000)
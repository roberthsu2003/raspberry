import gpiozero
from signal import pause
mcp3008 = gpiozero.MCP3008(channel=7)
print(mcp3008.value)
pause()
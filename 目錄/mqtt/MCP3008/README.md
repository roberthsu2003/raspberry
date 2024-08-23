# 5.MCP3008

## MCP3008
![](./images/xxmcp3008.png)

## 線路圖
![](./images/mcp3008_bb.png)

## 40pin
![](./images/GPIO.png)

## gpiozero控制

```python
import gpiozero as zero
from time import sleep

if __name__ == "__main__":
    mcp3008 = zero.MCP3008(7);
    while True:
        print("the channel 7 vlaue is {:.2f}".format(mcp3008.value));
        sleep(1);
```

## 


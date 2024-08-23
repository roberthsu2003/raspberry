# MCP3008_光敏電阻_可變電阻

## 1. MCP3008
![](./images/xxmcp3008.png)

## 2. 線路圖
![](./images/mcp3008_bb.png)

## 3. 40pin
![](./images/GPIO.png)

## 4. gpiozero控制

### 4.1 GPIOZERO的控制(測試用)
- [gpiozero MCP3008說明]()

```python
import gpiozero as zero
from time import sleep

if __name__ == "__main__":
    mcp3008_7 = zero.MCP3008(7);
    mcp3008_6 = zero.MCP3008(6);
    while True:
        print("the channel 7 光敏電阻:{:.2f}".format(mcp3008_7.value));
        print("the channel 6 可變電阻:{:.2f}".format(mcp3008_6.value))
        sleep(1)
```

![](./images/pic2.png)


### 4.2 本地端,MQTT,REDIS
#### 4.2.1 前置作業
- **啟動MQTT Server**
- **啟動REDIS Server**

#### 4.2.2 建立發佈和接收的py檔
- **mcp3008.py負責發佈**
- **receive.py負責訂閱**



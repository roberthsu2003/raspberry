
# Raspberry

預設帳號:pi

預設密碼:raspberry

# 目錄
## [系統安裝](./目錄/系統安裝)
- 沒有RaspberryPi硬體的解決方案
- 下載Raspberry Pi OS

## [遠端連線raspberry](./目錄/遠端連線raspberry)
- 從序列埠連線至Raspberry(必需要有TTL線)
- 查詢Raspberry的 ip Address 
- PC 透過SSH連線至Raspberry  
- Mac 透過SSH連線至Raspberry
- 設定raspberry環境 
- 使用遠端桌面(Microsoft Remote Desktop) 

## [命令列](./目錄/命令列)
- 建立github SSH keys
- 使用SSH學習命令列 
- 使用apt-get安裝和移除軟體
- 安裝vim文字編輯器

## [安裝python軟體工具和建立虛擬環境](./目錄/安裝軟體工具)
- 安裝python3.x
- 安裝condamini和jupyter(要用jupyter一定必需使用condamini)
- 使用Conda建立python的虛擬環境

## [樹莓派內安裝程式編輯器](./目錄/樹莓派內安裝程式編輯器)
- 安裝pycharm comunity editor for respberry4 2GB 以上
- 安裝vscode

## 雲端服務
- [Firebase](./Firebase)
- [Blynk](./Blynk/LEDControl)
- [ifttt](./ifttt/)
- [thingSpeak](./thingSpeak)

## GPIO 操控
- [Raspberry的40pin](#Raspberry的40pin)
- [硬體一覽表](./硬體一覽表)
- [tkinter](https://github.com/roberthsu2003/pythonWindow)
- [1.led Control](./Firebase_GPIO_tkinter/1LEDControl)
- [2.PWM LED](./Firebase_GPIO_tkinter/2PWMLed)
- [3.RGB LED](./Firebase_GPIO_tkinter/3RGBLed)
- [4.Button RGBLED](./Firebase_GPIO_tkinter/4Button_RGBLED)
- [5.MCP3008 光敏電阻 LM35](./Firebase_GPIO_tkinter/5MCP3008)
- [6.Servo](./Firebase_GPIO_tkinter/6servo)
- [7.7段顯示器](./Firebase_GPIO_tkinter/7seven_segment_display)
- [8.LCD_RFID](./Firebase_GPIO_tkinter/8LCD_RFID)
- [9.Camera](./Firebase_GPIO_tkinter/9Camera)
- [10.臉部辦識](./Firebase_GPIO_tkinter/10facial_recognition)
- [自動執行程式](#autoRunProgram)  



<a name="Raspberry的40pin"></a>
## Raspberry的40pin
![](./images/pic_40pin.png)


<a name=autoRunProgram></a>	
## 自動執行程式

### 啟動時自動執行應用程式

```
sudo nano /etc/rc.local

在最後一行加入
$ /usr/bin/python /home/pi/my_program.py &
```

	

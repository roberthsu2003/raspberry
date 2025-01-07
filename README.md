
# Raspberry

預設帳號:pi

預設密碼:raspberry

# 目錄
## [系統安裝](./目錄/系統安裝)
- 沒有RaspberryPi硬體的解決方案
- 下載Raspberry Pi OS

## [手動設定local](./目錄/locale)
- 解決piOs Perl Locale Warning

## [遠端連線raspberry](./目錄/遠端連線raspberry)
- 從序列埠連線至Raspberry(必需要有TTL線)
- **建立Raspberry網路上的小名**
- **查詢windows的ip address和建立raspberry的固定ip位址**
- 查詢Raspberry的 ip Address
- 透過電腦查詢Raspberry的 ip Address
- 使用手機app查詢 Raspberry IP Address
- 查詢Raspberry的 IP Address 
- 透過手機AppNet Analyzer`查詢Raspberry IP Address
- **PC 透過SSH連線至Raspberry**  
- **Mac 透過SSH連線至Raspberry**
- **設定raspberry環境**
- **建立新的使用者帳號**
- **使用遠端桌面(Microsoft Remote Desktop)**
- **使用VSCode連線至Raspberry**

## [命令列](./目錄/命令列)
- **學習命令列** 
- 使用apt-get安裝和移除軟體
- **安裝vim文字編輯器**

## [建立github連線](./目錄/ssh_keys)
￼

## [安裝python軟體工具和建立虛擬環境](./目錄/安裝軟體工具)
- 使用miniforge建立python的虛擬環境

## [樹莓派內安裝程式編輯器](./目錄/樹莓派內安裝程式編輯器)
- 安裝pycharm comunity editor for respberry4 2GB 以上
- 安裝vscode(piOS已經內建,在xwindows->add/Remove Software/Programming/)


## [安裝RPI-Monitor了解效能](./目錄/安裝RPI-Monitor)

## [安排週期性執行功能](./目錄/cron)

## [python程式週期性執行](./目錄/schedule)

## [MQTT Server￼](./目錄/mqtt)

## [radis server](./目錄/redis)

## [postgreSQL server](./目錄/postgreSQL)

## [Docker官網安裝方法](https://docs.docker.com/engine/install/debian/)
- 注意完成後要將user pi 加入至 docker group
  
  `sudo usermod -aG docker pi`


## [雲端服務](./目錄/雲端服務)
- Firebase
- Blynk
- ifttt
- thingSpeak

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

1 建立 .desktop File

mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/clock.desktop

2 clock.desktop的內容為

[Desktop Entry]
Type=Application
Name=Clock
Exec=/usr/bin/python3 /home/pi/clock.py
```



	

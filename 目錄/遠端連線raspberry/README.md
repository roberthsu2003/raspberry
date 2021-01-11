## 遠端連線raspberry

- [從序列埠連線至Raspberry(必需要有TTL線)](https://www.raspberrypi.com.tw/tag/usb-to-ttl/)  
- [查詢Raspberry的 ip Address](#find_ip_address)  
- [PC 透過SSH連線至Raspberry](#sshToRaspberryOnPC)  
- [Mac 透過SSH連線至Raspberry](#sshToRaspberryOnMac) 
- [設定raspberry環境](#set_up_raspberry)
- [使用遠端桌面(Microsoft Remote Desktop)](#Microsoft_Remote_Desktop) 

<a name="find_ip_address"></a>
## 查詢Raspberry的 ip Address
1. 將raspberry連接電源線,螢幕,keyboard,mouse,並開啟手機熱點連線
2. 將raspberry連線至手機熱點

![](./images/pic10.png)

3. 開啟terminal,並查詢ip address

	`$ ifconfig`
	
	![](./images/pic12.png)
<a name="sshToRaspberryOnPC"></a>
## PC 透過SSH連線到Raspberry
1. 下載並開啟[putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
2. 開啟putty,並用ssh連線到raspberry

![](./images/putty-linux.png)


<a name="sshToRaspberryOnMac"></a>
## Mac 透過SSH連線至Raspberry

```
#開啟terminal
% ssh 帳號@raspberry_ip_address
```


<a name="set_up_raspberry"></a>
## 設定raspberry環境
1. 開啟raspberry環境設定

	$ sudo raspi-config

![](./images/pic4.png)

2.選擇 Interfacing Options
	- VNC關閉，其餘開啟

![](./images/pic5.png)

3.選擇 Localisation Options -> 選擇Change Locale -> 選擇zh-TW.UTF8

![](./images/pic6.png)

4.選擇 Localisation Options -> 選擇Timezone -> 選擇Asia 

![](./images/pic7.png) 

5.選擇 Localisation Options -> 選擇Change Wi-fi Country -> 選擇TW

![](./images/pic8.png)

6.選擇 Localisation Options -> 選擇Keyboard Layout
	- Model:105-key PC(intl.)
	- Layout:English(UK)
	- Variant:English(UK) 

<a name="Microsoft_Remote_Desktop"></a>
### 使用遠端桌面(Microsoft Remote Desktop)
1. 關閉 vnc Server
2. 透過ssh安裝xrdp

	`sudo apt-get update`
	`sudo apt-get install xrdp -y`

3.使用遠端桌面連線raspberry

![](./images/pic9.png)

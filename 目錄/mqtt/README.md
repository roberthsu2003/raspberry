## MQTT 通訊協定
MQTT (Message Queuing Telemetry Transport) 是輕量和同時有發佈和訂閱功能的網路通訊協定,適合機器和機器傳送訊息的協定.它被設計來連線遠端裝置(arduin,pico....)有傳送少量資料的需求. 或是頻寬有限制(iot)的環境.

### Key Features of MQTT:

1. **輕量和高效率**:
	- MQTT 最大限度地減少網路頻寬和設備資源需求，同時確保可靠性和一定程度的交付保證。
2. **發佈/訂閱模式**:
	- 裝置(使用者端)可以發送帶有主題的訊息或訂閱主題以便接收訊息.使用中央代理可以協調訊息的交換.
3. **接收和發送的品質**:
	- MQTT支援三種￼QoS等級以確保訊息的傳送:
		- QoS 0: 最多ㄧ次 - 最有效率的傳送,不保證一定可以接收.
		- QoS 1: 最少一次 - 有可能會傳送多次.
		- QoS 2: 保證一次 - 確保一定會傳達訊息一次.(接收到一次)

### 應用方式:

- **IoT (Internet of Things)**:
- MQTT廣泛應用於IoT的應用程式，主要原因是它傳送的標頭非常小和有效率，適合多種裝置和sensor之間互相傳遞訊息￼.
	
- **即時資料的監控￼**:
	- 需要即時更新的應用程式，例如股票即時系統或環境監控系統，使用MQTT會有最低的延遲。￼

### MQTT 如何工作￼:
1. **使用者端**
￼￼- 任何裝置￼(sensor, 手機，應用程式)￼傳送訂閱主題資料給MQTT ￼broker￼和從MQTT ￼broker￼接收訂閱資料

2. **Broker(中介者)**:
	- 伺服器從裝置端接收訂閱主題￼資料和傳送他們至適當的訂閱者端裝置￼

### 工作流程範例:
1. 一個溫度感測器發佈訂閱此`home/livingroom/temperature`主題資料￼.
2. 中介伺服器接收這些訊息並且傳遞至所有有訂閱此`home/livingroom/temperature`主題的裝置端￼
3. 一個應用程式訂閱`home/livingroom/temperature`主題並接收訂閱的溫度資料資料，即時顯示溫度資料給使用者￼

MQTT支援多種平台和資源庫，使他容易整合到各種應用程式。這個通訊協定非常小巧和有效率，讓他運用在IoT的工作情境￼。


### MQTT￼安裝(Mosquitto)

1. **更新系統:**

```bash
sudo apt update
sudo apt upgrade
```

2. **Install Mosquitto:**
使用下列命令，￼安裝Mosquitto和Mosquitto clients
   
```bash
sudo apt install mosquitto mosquitto-clients
```

3. **開機時自動啟動Mosquitto￼:**
   
```bash
sudo systemctl enable mosquitto
```

4. **立即啟動 Mosquitto Service:**

```bash
sudo systemctl start mosquitto
```

5. **檢查Mosquitto Service狀態:**
   驗證現在Mosquitto service是否在執行￼:
```bash
sudo systemctl status mosquitto
```

6. **修改Mosquitto配置設定:**
    使用編輯器修改`/etc/mosquitto/mosquitto.conf`的設定.
    [修改說明]￼(/usr/share/doc/mosquitto/examples/mosquitto.conf.example)
    ￼
```bash
#原本的設定
pid_file /run/mosquitto/mosquitto.pid

persistence true
persistence_location /var/lib/mosquitto/

log_dest file /var/log/mosquitto/mosquitto.log

include_dir /etc/mosquitto/conf.d

#新增的設定
#監聽1883port
#允許匿名發佈
￼listener 1883 
allow_anonymous true
```

￼
### 使用command line操作測試
￼建立兩個終端機，一個終端機當作訂閱另一個終端機當作發佈。
￼
- 訂閱主題終端機如下：

```bash
mosquitto_sub -d -h localhost -t test/topic
```

- 發佈訂閱主題如下：

```bash
mosquitto_pub -d -h localhost -t test/topic -m "Hello, Mosquitto!"
```

￼將在訂閱主題的終端機看到以下幾個字：
```
Hello,Mosquitto!
```

### 在Windows￼上，可以安裝mqtt explore
### 使用python操作￼￼￼￼
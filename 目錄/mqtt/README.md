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

1. **Client**:
	- Any device (sensor, smartphone, application) that connects to the MQTT broker to publish or subscribe to topics.
2. **Broker**:
	- The server that receives messages from clients and routes them to appropriate subscribed clients.

### Example Workflow:

1. A temperature sensor publishes data to the topic `home/livingroom/temperature`.
2. The broker receives the message and forwards it to all clients subscribed to `home/livingroom/temperature`.
3. A smartphone app subscribed to this topic receives the temperature updates and displays them to the user.

MQTT is supported by many platforms and libraries, making it easy to integrate into various applications. The protocol's simplicity and efficiency have made it a de facto standard in the IoT industry.


### MQTT￼安裝(Mosquitto)
### 使用command line操作
### 使用python操作￼￼￼￼
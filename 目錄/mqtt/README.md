## MQTT 通訊協定
MQTT (Message Queuing Telemetry Transport) 是輕量和同時有發佈和訂閱功能的網路通訊協定,適合機器和機器傳送訊息的協定.它被設計來連線遠端裝置(arduin,pico....)有傳送少量資料的需求. 或是頻寬有限制(iot)的環境.

### Key Features of MQTT:

1. **輕量和高效率**:
	- MQTT 最大限度地減少網路頻寬和設備資源需求，同時確保可靠性和一定程度的交付保證。
2. **Publish/Subscribe Model**:
	- Devices (clients) can publish messages to topics or subscribe to topics to receive messages. A central broker mediates all message exchanges.
3. **Quality of Service Levels**:
	- MQTT supports three QoS levels to ensure message delivery:
		- QoS 0: At most once – The message is delivered according to the best efforts of the operating environment.
		- QoS 1: At least once – The message is assured to arrive but may be delivered more than once.
		- QoS 2: Exactly once – The message is assured to arrive exactly once.
4. **Small Transport Overhead**:
	- The protocol header is only 2 bytes (in the simplest case), making it suitable for low-bandwidth networks.
5. **Retained Messages**:
	- The broker can retain the last message sent on a topic, which can be delivered to clients when they subscribe to that topic.
6. **Last Will and Testament (LWT)**:
	- Allows clients to specify a message that the broker will send if it detects that the client has disconnected unexpectedly.

### Typical Use Cases:

- **IoT (Internet of Things)**:
	- MQTT is widely used in IoT applications due to its efficiency and low overhead, enabling communication between a vast number of devices and sensors.
- **Mobile Applications**:
	- Mobile apps that need to push updates or receive notifications use MQTT due to its ability to maintain connection and minimize data usage.
- **Real-Time Data Monitoring**:
	- Applications requiring real-time updates, such as stock tickers or environmental monitoring systems, use MQTT for its low latency.

### How MQTT Works:

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
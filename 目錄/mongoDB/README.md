## raspberry 透過Docker安裝MongoDB
- 使用非官方版,依照說明書,下載檔案,載入image
- https://github.com/themattman/mongodb-raspberrypi-docker

**建立container**
```
docker run -itd -p 27071:27071 mongodb-raspberrypi4-unofficial-r7.0.4
```
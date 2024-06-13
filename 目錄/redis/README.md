# 在 Raspberry Pi 上安裝 Redis Stack

本文將指導您如何在 Raspberry Pi 上安裝 Redis Stack。

## 前置準備

在開始之前，請確保您的系統已更新並且安裝了必要的工具。

1. 更新系統：
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

2. 安裝必要的工具：
```bash
sudo apt-get install -y build-essential tcl
```

## 安裝 Redis

```bash
sudo apt install redis-server -y
```

## 設定Redis

```
sudo nano /etc/redis/redis.conf
```

## 增加一行

```
maxmemory 100mb maxmemory-policy allkeys-lru
```

## 啟動redis service 和 自動開啟

```bash
sudo systemctl  enable  redis-server
sudo systemctl start redis-server
```

## 測試

```
redis-cli ping
```

## 重新啟動redis

```
redis-server
```



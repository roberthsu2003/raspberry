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

## 增加(可設可不設),最大使用記憶體的數量

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

## 從外部電腦使用redis insight連至redis server

### 1. 修改設定,讓所有外部電腦可以連入

#### 1-1. 修改redis.conf
```
sudo nano /etc/redis/redis.conf
```

#### 1-2. 修改一行設定

```
bind 0.0.0.0
```

#### 1-3. 重新啟動

```
sudo service redis-server restart
```

### 2. 修改設定,不需使用帳號密碼
#### 2-1. 修改redis.conf
```
sudo nano /etc/redis/redis.conf
```

#### 2-2. 修改一行設定

```
protected-mode no
```

#### 2-3. 重新啟動

```
sudo service redis-server restart
```


## 手動啟用redis-server
```
redis-server
```



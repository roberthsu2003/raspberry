# 在 Raspberry Pi 上安裝 Redis Stack

本文將指導您如何在 Raspberry Pi 上安裝 Redis Stack。

## 前置準備

在開始之前，請確保您的系統已更新並且安裝了必要的工具。

1. 更新系統：
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

2. 安裝必要的工具：
    ```bash
    sudo apt-get install -y build-essential tcl
    ```

## 安裝 Redis

1. 下載 Redis 最新版本：
    ```bash
    wget http://download.redis.io/redis-stable.tar.gz
    ```

2. 解壓縮檔案：
    ```bash
    tar xvzf redis-stable.tar.gz
    ```

3. 進入目錄並編譯安裝：
    ```bash
    cd redis-stable
    make
    sudo make install
    ```

4. 執行 Redis 測試：
    ```bash
    make test
    ```

5. 安裝 Redis 服務：
    ```bash
    sudo cp src/redis-server /usr/local/bin/
    sudo cp src/redis-cli /usr/local/bin/
    ```

## 配置 Redis

1. 創建配置檔案和資料夾：
    ```bash
    sudo mkdir /etc/redis
    sudo cp redis.conf /etc/redis
    ```

2. 編輯 Redis 配置檔案：
    ```bash
    sudo nano /etc/redis/redis.conf
    ```

    修改以下內容：
    ```plaintext
    supervised systemd
    dir /var/lib/redis
    ```

## 設定 Redis 服務

1. 創建 Redis 服務檔案：
    ```bash
    sudo nano /etc/systemd/system/redis.service
    ```

2. 複製以下內容到檔案中：
    ```plaintext
    [Unit]
    Description=Redis In-Memory Data Store
    After=network.target

    [Service]
    User=redis
    Group=redis
    ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf
    ExecStop=/usr/local/bin/redis-cli shutdown
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```

3. 設置資料夾權限：
    ```bash
    sudo mkdir /var/lib/redis
    sudo chown redis:redis /var/lib/redis
    sudo chmod 770 /var/lib/redis
    ```

4. 啟動並啟用 Redis 服務：
    ```bash
    sudo systemctl start redis
    sudo systemctl enable redis
    ```

## 驗證 Redis 安裝

1. 驗證 Redis 是否正常運行：
    ```bash
    sudo systemctl status redis
    ```

2. 使用 Redis CLI 測試：
    ```bash
    redis-cli
    ```

    輸入以下命令：
    ```plaintext
    ping
    ```

    如果返回 `PONG`，表示 Redis 安裝成功。

恭喜您！您已成功在 Raspberry Pi 上安裝並配置了 Redis Stack。

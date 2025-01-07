## 解決 the Perl Locale Warning
### 1. 檢查目前系統的Locale

```bash
local -a
```

### 2. 編輯/etc/locale.gen增加en_US.UTF8, en_GB.UTF8的設定

```
en_US.UTF-8 UTF-8
en_GB.UTF-8 UTF-8
zh_TW.UTF-8 UTF-8
```

然後執行以下指令安裝

```
sudo locale-gen
```

### 3. 在~/.bashrc內設定Locale的環境變數


- **可以只設定最高等級的LC_ALL**

```
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```



### 4. 執行更新

```bash
sudo apt-get update && \
sudo apt-get install -y locales && \
sudo locale-gen en_US.UTF-8 && \
sudo update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
```
### 5.重新開機

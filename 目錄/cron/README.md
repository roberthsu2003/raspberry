## 安排週期性工作 - `cron`
#### `cron` 只可以使用在linux環境,windows的使用都必需安裝WSL(window subsystem linux),
工具型軟體cron是一款類Unix的作業系統下的基於時間的任務管理系統。使用者們可以通過cron在固定時間、日期、間隔下，執行定期任務（可以是命令和指令碼）。cron常用於運維和管理，但也可用於其他地方，如：定期下載檔案和郵件。cron該詞來源於希臘語chronos（χρόνος），原意是時間。

### 1.0 工作目錄:
 - #### `/etc/cron.d`:
	- 包含的檔案是屬於系統等級的
	- 檔案格式需要加入user field -> `* * * * * user command`
	- 經常籍由安裝套件時加入工作,或系統管理員加入 
- /var/spool/cron/
	- 使用者的管理等級
	- 檔案格式沒有user fileld -> `* * * * * command`
	- 使用者使用crontab命令管理

### 2.0 指令:crontab
#### 2.1 語法:

```python
* * * * * command_to_execute
- - - - -
| | | | |
| | | | +----- Day of the week (0 - 7) (Sunday=0 or 7)
| | | +------- Month (1 - 12)
| | +--------- Day of the month (1 - 31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
```
#### 2.2 基本語法:
##### 2.2.1 顯示目前的crontab

```bash
crontab -l
```

##### 2.2.2 編輯crontab

```bash
crontab -e
```

##### 2.2.3 移除crontab

```bash
crontab -r
```

#### 2.3 crontab 範例程式

##### 2.3.1 每天早上3:00執行

```bash
0 3 * * * /path/to/script.sh
```


##### 2.3.2 每15分鐘執行

```bash
*/15 * * * * /path/to/script.sh
```


##### 2.3.1 每月1日早上10:30分執行 

```bash
30 10 1 * * /path/to/script.sh
```

##### 每天星期一下午5:00執行

```bash
0 17 * * 1 /path/to/script.sh
```

#### 2.4 特殊字串

- `@reboot` -> 電腦重新啟動時執行
- `@year` or `@annually` -> 每年執行一次
- `@monthly` -> 每月
- `@weekly` -> 每星期
- `@daily` -> 每天
- `@hourly` -> 每小時

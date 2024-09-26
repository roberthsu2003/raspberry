## 解決 the Perl Locale Warning
### 1. 檢查目前系統的Locale

```bash
local -a
```

### 2.編輯/etc/locale.gen增加en_US.UTF8, en_GB.UTF8的設定

```
en_US.UTF-8 UTF-8
en_GB.UTF-8 UTF-8
zh_TW.UTF-8 UTF-8
```

然後執行以下指令安裝

```
sudo locale-gen
```

### 3.在~/.bashrc內設定Locale的環境變數

```
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 4.重新開機

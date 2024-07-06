## python schedule
### 1.0 安裝套件

```bash
pip install schedule

```

### 2.0 [官網說明書](https://schedule.readthedocs.io/en/stable/)

### 3.0 [範例]

#### 3.1 每5秒執行一次

```python
import schedule
import time as tm

def job():
	print("I am teacher RobertHsu")

schedule.every(5).seconds.do(job)


while True:
	schedule.run_pending()
	tm.sleep(1)

```



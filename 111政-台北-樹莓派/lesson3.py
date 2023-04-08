import private
import requests

url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttKey}?value1=31c&value2=51'

r = requests.get(url)
if r.status_code == 200:
    print("發送成功")
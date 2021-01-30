import requests
import time
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
while True:
    paras = {'value1':'50',
             'value2':'60'   
            }
    response = requests.get("https://maker.ifttt.com/trigger/over30/with/key/eDqcZfqY_i_BHCZVXCwb6aq7GLPKpdV4q1ePja35Mjq",
                params = paras,
                headers = header
               )
    print(response.status_code)
    time.sleep(60)
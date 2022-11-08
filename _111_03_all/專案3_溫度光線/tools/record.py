import os
from datetime import datetime

directory = os.path.abspath("./record")
if not os.path.isdir(directory):
    #建立目錄
    os.makedirs(directory)

def recordData(distance,lightValue):
    current = datetime.now()
    current_date = current.date()
    filename = current_date.strftime("%Y-%m-%d.csv")    
    currentFiles = os.listdir(directory)
    if filename not in currentFiles:
        #建立檔案
        file = open(f"{directory}/{filename}",'w',encoding='utf-8')
        file.close()
    
    

    
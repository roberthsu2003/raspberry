import os
import csv
from datetime import datetime

directory = os.path.abspath("./record")
if not os.path.isdir(directory):
    #建立目錄
    os.makedirs(directory)

filename_abs = None

def recordData(distance,lightValue):
    global filename_abs
    current = datetime.now()
    current_date = current.date()
    filename = current_date.strftime("%Y-%m-%d.csv")    
    currentFiles = os.listdir(directory)
    filename_abs = f"{directory}/{filename}"
    if filename not in currentFiles:
        #建立檔案
        file = open(filename_abs,'w',encoding='utf-8',newline='')
        header_writer = csv.writer(file)
        header_writer.writerow(["日期","距離","光線"])
        file.close()
    #加入資料
    with open(filename_abs,"a",newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([current.strftime("%Y-%m-%d %H:%M:%S"),distance,lightValue])

def getData():
    with open(filename_abs,"r",newline='') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    return data

    
    

    
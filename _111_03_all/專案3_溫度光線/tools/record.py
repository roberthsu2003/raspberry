import os
import csv
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


full_path_csvFile =  None
db = None

def recordData(distance,lightValue,absolute_path): 
    global full_path_csvFile
    global db  
    current = datetime.now()
    current_date = current.date()
    filename = current_date.strftime("%Y-%m-%d.csv")
    relative_path = "record/"
    full_path_record = os.path.join(absolute_path,relative_path)

    if not os.path.isdir(full_path_record):
        #建立目錄
        os.makedirs(full_path_record)
       
    currentFiles = os.listdir(full_path_record)
    full_path_csvFile = os.path.join(full_path_record,filename)
    print(full_path_csvFile)    
    if filename not in currentFiles:
        #建立檔案
        file = open(full_path_csvFile,'w',encoding='utf-8',newline='')
        header_writer = csv.writer(file)
        header_writer.writerow(["日期","距離","光線"])
        file.close()
    #加入資料
    with open(full_path_csvFile,"a",newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([current.strftime("%Y-%m-%d %H:%M:%S"),distance,lightValue])

    #將資料加入至firestore
    #print("要加入的資料")
    #print('日期',current.strftime("%Y-%m-%d %H:%M:%S"))
    #print('距離',distance)
    #print("亮度",lightValue)
    relative_path_key = "private/raspberry1-58efc-firebase-adminsdk-tzk5o-6836a56c1e.json"
    full_path_key = os.path.join(absolute_path,relative_path_key)
    print("key:",full_path_key)
    if db is None:
        cred = credentials.Certificate(full_path_key)
        app = firebase_admin.initialize_app(cred)
        db = firestore.client()

def getData():
    with open(full_path_csvFile,"r",newline='') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    return data

    
    

    
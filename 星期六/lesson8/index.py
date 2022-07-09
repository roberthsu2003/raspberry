import tkinter as tk
import requests
from tkinter import LEFT, ttk 

blynk_token = "dG_jaJZqwM5YZsh8x7zPFeyI3VwBDa7h"
 


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #-----------建立tkinter----------------------        
        self.title("python視窗和Blynk整合")
        mainFrame  = tk.Frame(self, relief="groove", borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame,text="python視窗和Blynk整合",font=("Arial",15),fg="#555555").pack(padx=10)
        titleFrame.pack(pady=30)
        mainFrame.pack(pady=30,padx=30,ipadx=30,ipady=30) 

        #------------建立bottomFrame和temperatureFrame------------------------
        self._tem_job = None
        def tem_something(value):
            self._tem_job = None
            print(f"temperature={value}")
            update_url = f'https://blynk.cloud/external/api/update?token={blynk_token}&v0={value}'
            response = requests.get(update_url)
            if response.status_code == 200:
                print("溫度更新成功")


        def tem_update_value(scale_value):
            #scale_value是它的值
            if self._tem_job:
                self.after_cancel(self._tem_job)
            self._tem_job = self.after(500,lambda:tem_something(scale_value))

        self.temperatureText = tk.StringVar()
        bottomFrame = tk.Frame(mainFrame)
        temperatureFrame = tk.LabelFrame(bottomFrame,text="溫度")
        tk.Entry(temperatureFrame, width = 16, textvariable=self.temperatureText,state = tk.DISABLED).grid(row=0,column=0,sticky=tk.W,padx=5,pady=20);
        self.temperatureText.set("123.456");
         

        temperatureFrame.pack(side=tk.LEFT)

        #--------------建立HumidityFrame--------------------
        self._hum_job = None
        def hum_something(value):
            self._hum_job = None
            print(f"humidity={value}")
            update_url = f'https://blynk.cloud/external/api/update?token={blynk_token}&v1={value}'
            response = requests.get(update_url)
            if response.status_code == 200:
                print("溼度更新成功")

        def hum_update_value(scale_value):
            #scale_value是它的值
            if self._hum_job:
                self.after_cancel(self._hum_job)
            self._hum_job = self.after(500,lambda:hum_something(scale_value))
            
        self.lightnessText = tk.StringVar()
        humidityFrame = tk.LabelFrame(bottomFrame,text="光線")         
        tk.Entry(humidityFrame, width = 16, textvariable=self.lightnessText, state = tk.DISABLED).grid(row=0,column=0,sticky=tk.W,padx=5,pady=20);
        self.lightnessText.set("456.789");
        humidityFrame.pack(side=tk.RIGHT)


        bottomFrame.pack()
        
def closeWindow():
    print("close window")
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.resizable(width=0,height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()


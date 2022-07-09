import tkinter as tk
import requests
from tkinter import LEFT, ttk 
from gpiozero import MCP3008

blynk_token = "xxxxxxxxxxxxxxx"

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #----------gpiozero mcp3008-----------------
        #gpiozero
        self.lightness = MCP3008(channel=7);
        self.temperature = MCP3008(channel=6);

        #-----------建立tkinter----------------------        
        self.title("python視窗和Blynk整合")
        mainFrame  = tk.Frame(self, relief="groove", borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame,text="python視窗和Blynk整合",font=("Arial",15),fg="#555555").pack(padx=10)
        titleFrame.pack(pady=30)
        mainFrame.pack(pady=30,padx=30,ipadx=30,ipady=30) 

        #------------建立bottomFrame和temperatureFrame------------------------   
        self.temperatureText = tk.StringVar()
        bottomFrame = tk.Frame(mainFrame)
        temperatureFrame = tk.LabelFrame(bottomFrame,text="溫度")
        tk.Entry(temperatureFrame, width = 16, textvariable=self.temperatureText,state = tk.DISABLED).grid(row=0,column=0,sticky=tk.W,padx=5,pady=20);
        self.temperatureText.set("123.456");
         

        temperatureFrame.pack(side=tk.LEFT)
        #--------------建立HumidityFrame--------------------        
        self.lightnessText = tk.StringVar()
        humidityFrame = tk.LabelFrame(bottomFrame,text="光線")         
        tk.Entry(humidityFrame, width = 16, textvariable=self.lightnessText, state = tk.DISABLED).grid(row=0,column=0,sticky=tk.W,padx=5,pady=20);
        self.lightnessText.set("456.789");
        humidityFrame.pack(side=tk.RIGHT)
        bottomFrame.pack()  
        self.update_temperature_light()

    def update_temperature_light(self):
        lightnessValue = self.lightness.value * 1000;
        temperatureValue = self.temperature.value * 3.3 * 100;
        self.temperatureText.set("{:.2f}".format(temperatureValue));
        self.lightnessText.set("{:.2f}".format(lightnessValue));

        update_tem_url = f'https://blynk.cloud/external/api/update?token={blynk_token}&v0={temperatureValue}'
        response = requests.get(update_tem_url)
        if response.status_code == 200:
            print("溫度更新成功")
        
        update_light_url = f'https://blynk.cloud/external/api/update?token={blynk_token}&v1={lightnessValue}'
        response = requests.get(update_light_url)
        if response.status_code == 200:
            print("光線更新成功")

        self.after(500,self.update_temperature_light);
        
        
def closeWindow():
    print("close window")
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.resizable(width=0,height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()


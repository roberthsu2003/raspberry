import tkinter as tk
import tkinter.font as font
import requests

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        cfont = font.Font(family='Helvetica',size=35)
        btn = tk.Button(self,text="Press Me",command=self.buttonClick,font=cfont)
        btn.pack(expand=tk.YES,fill=tk.BOTH,padx=20,pady=20)
    
    def buttonClick(self):
        lineUrl = "https://maker.ifttt.com/trigger/tkinter_press/with/key/xxxxxx"
        sendInfo = { "value1" : "10", "value2" : "20", "value3" : "30" }
        headers =  {'content-type': 'application/json'}
        response = requests.get(lineUrl, params=sendInfo,headers=headers)

        


if __name__ == "__main__":
    window = Window()
    window.title("連線iftttt")
    window.geometry("400x200+300+300")
    window.resizable(width=False,height=False)
    window.configure(background="#333333")
    window.mainloop()
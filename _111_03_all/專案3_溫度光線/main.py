import tkinter as tk
from datetime import datetime
from tools import data


class Window(tk.Tk):
    def __init__(self):
        super().__init__()   
        self.label = tk.Label(self,text="",font=("arial",30))
        self.label.pack(padx=50,pady=30)
        self.change_time()
        self.window_time()
        

        
    def change_time(self):
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.label.config(text=now_str)
        self.after_id = self.label.after(1000,self.change_time)

    def window_time(self):
        data.getDistance()
        data.getLightValue()
        self.window_id = self.after(1000 * 3,self.window_time)

    def delete_delay(self):
        self.label.after_cancel(self.after_id)
        self.after_cancel(self.window_id)
        self.destroy()
        
        
        


def main():
    window =  Window()
    window.title("數位時鐘")
    window.protocol("WM_DELETE_WINDOW",window.delete_delay)
    window.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tools import data,record


class CustomView(ttk.Treeview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.heading('#1',text="日期")
        self.heading('#2',text="距離")
        self.heading('#3',text="光線")

    def addData(self,data):
        #清除第一筆資料
        data.pop(0)
        #反向
        data.reverse()
        #清除所有資料
        for i in self.get_children():
            self.delete(i)
        #新增所有資料
        for item in  data:
            self.insert('',tk.END,values=item)
        
        
class Window(tk.Tk):
    def __init__(self):
        super().__init__()   
        self.label = tk.Label(self,text="",font=("arial",30))
        self.label.pack(padx=50,pady=30)
        self.customView = CustomView(self,columns=('#1','#2','#3'),show='headings')
        self.customView.pack(padx=20,pady=(0,20))
        self.change_time()
        self.window_time()
        
    def change_time(self):
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.label.config(text=now_str)
        self.after_id = self.label.after(1000,self.change_time)

    def window_time(self):
        distance = data.getDistance()
        print(distance)
        if distance < 100.0: 
            print(f"距離:{distance:.2f}公分")
        else:
            print(f"距離:大於100公分")
            distance = 100   
               
        lightValue = data.getLightValue()
        print(f"光線:{lightValue:.1f}")
        #記錄資料
        record.recordData(distance=distance,lightValue=lightValue)

        #取得資料
        all_data = record.getData()
        self.customView.addData(all_data)        
        self.window_id = self.after(1000 * 30,self.window_time)

    def delete_delay(self):
        self.label.after_cancel(self.after_id)
        self.after_cancel(self.window_id)
        self.destroy()
        
        
def main():
    window =  Window()
    window.title("光線和距離監測器")
    window.protocol("WM_DELETE_WINDOW",window.delete_delay)
    window.mainloop()

if __name__ == "__main__":
    main()
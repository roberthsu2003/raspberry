import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('這是我的第一個視窗')
        self.resizable(False, False)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Title.TLabel',foreground='red',background='yellow',font=('Arial',20))
        s.configure('Led.TButton',foreground='red',background='yellow',font=('Arial',20),borderwidth=5,padding=(10,20))
        print(s.layout('TButton'))
        title_label = ttk.Label(self,text="LED控制器",style='Title.TLabel')        
        title_label.pack(pady=25,padx=100)

        led_btn = ttk.Button(self,text="LED 開",style='Led.TButton',command=self.user_click)
             
        led_btn.pack(pady=(10,50))

    def user_click(self):
        print('user click')

if __name__ == "__main__":
    window = Window()   
    window.mainloop()
   
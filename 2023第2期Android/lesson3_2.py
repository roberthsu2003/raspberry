import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('這是我的第一個視窗')
        self.resizable(False, False)
        s = ttk.Style()
        print(s.theme_names())
        print(s.theme_use())
        s.theme_use('clam')
        title_label = ttk.Label(self,text="LED控制器",font=('Helvetica', '16'))
        title_label.pack(pady=25,padx=100)

        led_btn = ttk.Button(self,text="LED 開")
        led_btn.pack(pady=(10,50))

if __name__ == "__main__":
    window = Window()   
    window.mainloop()
   
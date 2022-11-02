import tkinter as tk
from datetime import datetime

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        tk.Label(self,text=now_str,font=("Arial",30)).pack(padx=50,pady=30)


def main():
    window =  Window()
    window.title("數位時鐘")
    window.mainloop()

if __name__ == "__main__":
    main()
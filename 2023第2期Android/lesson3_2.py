import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('這是我的第一個視窗')
        self.geometry('380x400')
        self.resizable(False, False)

if __name__ == "__main__":
    window = Window()   
    window.mainloop()
   
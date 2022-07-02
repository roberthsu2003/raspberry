import tkinter as tk

class Window(tk.Tk):
    pass

def closeWindow():
    print("close window")
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.resizable(width=0, height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()
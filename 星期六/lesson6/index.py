import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        mainFrame = tk.Frame(self, relief="groove", borderwidth=2)
        titleFrame = tk.Frame(mainFrame)
        tk.Label(titleFrame,text="python視窗和Firebase及時資料庫_RGBLED",font=("Arial",20),fg="#555555").pack(padx=10)
        titleFrame.pack(pady=30)
        mainFrame.pack(padx=30, pady=30, ipadx=30, ipady=30)

def closeWindow():
    print("close window")
    window.destroy()

if __name__ == "__main__":
    window = Window()
    window.title("python視窗和Firebase及時資料庫")
    window.resizable(width=0, height=0)
    window.protocol("WM_DELETE_WINDOW",closeWindow)
    window.mainloop()
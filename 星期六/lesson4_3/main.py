import tkinter as tk
import tkinter.font as font

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        cfont = font.Font(family='arial',size=35)
        btn = tk.Button(self,text="Press Me",command=self.buttonClick,font=cfont)
        btn.pack()
    
    def buttonClick(self):
        print("button click")
        


if __name__ == "__main__":
    window = Window()
    window.title("連線iftttt")
    window.geometry("400x200+300+300")
    window.resizable(width=False,height=False)
    window.configure(background="#333333")
    window.mainloop()
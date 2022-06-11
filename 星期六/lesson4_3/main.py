import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        btn = tk.Button(self,text="請按我",command=self.buttonClick)
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
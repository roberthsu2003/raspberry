import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas1 = tk.Canvas(self,width=400,height=250)
        canvas1.create_rectangle(30, 10, 120, 80, outline="#000", fill="#fb0")
        canvas1.create_rectangle(150, 10, 240, 80, outline="#000", fill="#f50")
        canvas1.create_rectangle(270, 10, 370, 80, outline="#000", fill="#05f")
        canvas1.pack()
        

def main():
    window = Window()
    window.title("Canvas")
    window.geometry("400x100+300+200")
    window.mainloop()
    

if __name__ == "__main__":
    main()
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas1 = tk.Canvas(self,width=400,height=250,background="#7D532C")
        canvas1.create_line(15, 30, 200, 30,fill="#FFBA84")
        canvas1.create_line(300,35,300,200, dash=(4,2),fill="#FFBA84")
        canvas1.create_line(55, 85, 155,85,105,180,55, 85,fill="#FFBA84")
        canvas1.pack()
        

def main():
    window = Window()
    window.title("Canvas")
    window.geometry("400x250+300+200")
    window.mainloop()
    

if __name__ == "__main__":
    main()
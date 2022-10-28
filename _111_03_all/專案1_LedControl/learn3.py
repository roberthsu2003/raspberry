import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas1 = tk.Canvas(self,width=400,height=300)
        canvas1.create_oval(10, 10, 80, 80, outline="#000", fill="#1f1", width=5)

        canvas1.create_oval(110, 10, 210, 80, outline="#000", fill="#1f1", width=5)

        canvas1.create_arc(30, 200, 90, 260, start=0, extent=270, outline="#000", width=5, fill="#1f1")
        

        points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
        canvas1.create_polygon(points, outline="#000", fill="#1f1", width=5)

        canvas1.pack()
        

def main():
    window = Window()
    window.title("Canvas")
    window.geometry("400x300+300+200")
    window.mainloop()
    

if __name__ == "__main__":
    main()
import tkinter as tk

class Window(tk.Tk):
    def __init_(self):
        super().__init__()
        pass
        

def main():
    window = Window()
    window.title("Canvas")
    window.geometry("400x250+300+200")

if __name__ == "__main__":
    main()
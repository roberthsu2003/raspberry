import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        

def main():
    window =  Window()
    window.title("數位時鐘")
    window.mainloop()

if __name__ == "__main__":
    main()
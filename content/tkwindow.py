from tkinter import *



class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Kitty")
        
        label = Label(self, text="Hello World!")
        label.pack(fill=BOTH, expand=True, padx=100, pady=50)
    
if __name__ == "__main__":
    window = Window()
    window.mainloop()
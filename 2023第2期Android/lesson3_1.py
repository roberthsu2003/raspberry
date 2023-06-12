import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        label = tk.Label(self, text="Hello! 這是我的第一個視窗軟體!")
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("按鈕")
        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

    def say_hello(self):
        print("Hello! Robert")


def main():
    window = Window()
    window.mainloop()
    
if __name__ == "__main__":
    main()
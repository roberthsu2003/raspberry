import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立title
        self.title("LED Controller")
        #建立按鈕
        btn = tk.Button(self,text="開關",padx=50,pady=30,font=('arial',18),command=self.userClick)
        btn.pack(padx=50,pady=30)
    
    def userClick(self):
        print("user click")


def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()
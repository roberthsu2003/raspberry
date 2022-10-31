import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()    
        red = tk.Canvas(self,width=70,height=70,relief='ridge')
        red.create_rectangle(10,10,60,60,fill="red")
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)

        green = tk.Canvas(self,width=70,height=70)
        green.create_rectangle(10,10,60,60,fill="green")
        green.grid(row=0, column=1)

        blue = tk.Canvas(self,width=70,height=70)
        blue.create_rectangle(10,10,60,60,fill="blue")
        blue.grid(row=0, column=2)

    def mouse_click(self,event):
        print(event.__dict__)
        event.widget.config(borderwidth=5,)
        event.widget.update()

def main():
    window = Window()
    window.title("RGBLED 顏色控制")
    window.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk

class ColorCanvas(tk.Canvas):
    def __init__(self,parent,rec_color,**kwargs):
        super().__init__(parent,**kwargs)
        self.rec_color = rec_color
        space = 10
        rec_width = int(self['width'])  - 2 * space 
        rec_height = int(self['height']) - 2 * space   
        self.create_rectangle(space, space, int(self['width']) - space, int(self['height']) - space,fill=self.rec_color)

class Window(tk.Tk):
    def __init__(self):
        super().__init__()    
        red = ColorCanvas(self,"red",width=70,height=70)
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
        #event.widget.delete()
        event.widget.create_rectangle(10,10,60,60,fill='white')
        event.widget.create_rectangle(20,20,50,50,fill='red')
        #event.widget.update()

def main():
    window = Window()
    window.title("RGBLED 顏色控制")
    window.mainloop()

if __name__ == "__main__":
    main()
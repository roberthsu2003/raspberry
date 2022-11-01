import tkinter as tk

class ColorCanvas(tk.Canvas):
    def __init__(self,parent,rec_color,**kwargs):
        width = kwargs['width']
        height = kwargs['height']
        super().__init__(parent,**kwargs)
        self.rec_color = rec_color
        self.__state = False
        space = width / 7
        rec_width = width  - 2 * space 
        rec_height = height - 2 * space   
        self.create_rectangle(space, space, width - space, height - space,fill=self.rec_color)

    
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self,s):
        self.__state  = s


class Window(tk.Tk):
    def __init__(self):
        super().__init__()    
        red = ColorCanvas(self,"red",width=100,height=100)
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)
        red.state = True
        print(f"red狀態:{red.state}")
        green = ColorCanvas(self,"green",width=100,height=100)        
        green.grid(row=0, column=1)
        blue = ColorCanvas(self,"blue",width=100,height=100)        
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
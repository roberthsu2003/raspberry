import tkinter as tk

class ColorCanvas(tk.Canvas):
    #建立Class的propertuy
    #建立一個Class內建的常數
    ON =  True
    OFF = False
    def __init__(self,parent,rec_color,**kwargs):
        self.width = kwargs['width']
        self.height = kwargs['height']
        super().__init__(parent,**kwargs)
        self.rec_color = rec_color
        self.__state = ColorCanvas.OFF
        self.space = self.width / 7
        rec_width = self.width  - 2 * self.space 
        rec_height = self.height - 2 * self.space   
        self.create_rectangle(self.space, self.space, self.width - self.space, self.height - self.space,fill=self.rec_color)

    
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self,s):
        self.__state  = s
        self.delete()
        self.create_rectangle(self.space, self.space, self.width - self.space, self.height - self.space,fill=self.rec_color)        
        if self.__state == True:
            #多加小圓點
            print("多加小圓點")
            

       


class Window(tk.Tk):
    def __init__(self):
        super().__init__()           
        red = ColorCanvas(self,"red",width=100,height=100)
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)
        red.state = ColorCanvas.ON
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
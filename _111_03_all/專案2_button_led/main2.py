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
            rec_width = self.width  - 2 * self.space 
            rec_height = self.height - 2 * self.space            
            cir_width = rec_width / 5
            cir_height = rec_height / 5
            cir_start_x = self.space + cir_width / 2
            cir_end_x = cir_start_x + cir_width
            cir_start_y = self.space + rec_height * 5 / 7
            cir_end_y  =  cir_start_y + cir_height
            self.create_oval(cir_start_x,cir_start_y,cir_end_x,cir_end_y,fill='white',outline='white')

       


class Window(tk.Tk):
    selected_convas = None
    @classmethod
    def get_select_convas(cls):
        return cls.selected_convas

    @classmethod
    def set_select_convas(cls,convas):
        if cls.selected_convas is not None:
            cls.selected_convas.state = ColorCanvas.OFF   
        cls.selected_convas = convas
        cls.selected_convas.state = ColorCanvas.ON


    def __init__(self):
        super().__init__()           
        red = ColorCanvas(self,"red",width=100,height=100)
        red.bind('<ButtonRelease-1>',self.mouse_click)
        red.grid(row=0, column=0)               
        green = ColorCanvas(self,"green",width=100,height=100)
        green.bind('<ButtonRelease-1>',self.mouse_click)        
        green.grid(row=0, column=1)        
        blue = ColorCanvas(self,"blue",width=100,height=100)
        blue.bind('<ButtonRelease-1>',self.mouse_click)        
        blue.grid(row=0, column=2)
        Window.set_select_convas(red)
        select_canvas = Window.get_select_convas()
        print(select_canvas.rec_color)
        

    def mouse_click(self,event):
        Window.set_select_convas(event.widget)

def main():
    window = Window()
    window.title("RGBLED 顏色控制")
    window.mainloop()

if __name__ == "__main__":
    main()
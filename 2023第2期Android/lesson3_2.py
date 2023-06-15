import tkinter as tk
from tkinter import ttk
from gpiozero import LED
#import pprint

class Window(tk.Tk):    
    def __init__(self,redLed):
        '''
        @parmater redLed,是gpiozeor.LED的實體
        '''
        super().__init__()
        self.redLed = redLed
        self.state = False
        self.title('這是我的第一個視窗')
        self.resizable(False, False)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Title.TLabel',font=('Arial',20))
        s.configure('LEDClose.TButton',                    
                    font=('Arial',20),
                    borderwidth=5,
                    padding=(10,20),
                    )
        s.configure('LEDOpen.TButton',
                    background='yellow',                    
                    font=('Arial',20),
                    borderwidth=5,
                    padding=(10,20),
                    )
        #pprint.pprint(s.layout('TButton'))
        #pprint.pprint(s.element_options('Button.focus'))
        title_label = ttk.Label(self,text="LED控制器",style='Title.TLabel')        
        title_label.pack(pady=25,padx=100)

        self.led_btn = ttk.Button(self,text="LED 開",style='LEDClose.TButton',command=self.user_click)             
        self.led_btn.pack(pady=(10,50))

    def user_click(self):
        self.state = not self.state
        if self.state:
            self.led_btn.configure(text='LED 關')
            self.led_btn.configure(style='LEDOpen.TButton')
            self.redLed.on()
        else:
            self.led_btn.configure(text='LED 開')
            self.led_btn.configure(style='LEDClose.TButton')
            self.redLed.off()

if __name__ == "__main__":
    led = LED(23)
    led.off()
    window = Window(led)   
    window.mainloop()
   
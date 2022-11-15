import tkinter as tk
from PIL import Image,ImageTk
import RPi.GPIO as GPIO

BLYNK_AUTH_TOKEN = "_W4TI-9ca37qXQyAhFiX4jMhvO989lvj"

class LightButton(tk.Button):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        #建立圖片
        ##建立close的圖片
        close_image = Image.open('light_close.png')
        self.close_photo = ImageTk.PhotoImage(close_image)
        ##建立open的圖片
        open_image = Image.open('light_open.png')
        self.open_photo = ImageTk.PhotoImage(open_image)
        self.config(borderwidth=0)
        self.config(state="disabled")
        

    def open(self):
        self.config(image=self.open_photo)
        

    def close(self):
        self.config(image=self.close_photo);
        

class Window(tk.Tk):
    def __init__(self):
        super().__init__()        

        #建立title
        self.title("LED Controller")

        #建立按鈕

        self.btn = LightButton(self,padx=50,pady=30)
        self.btn.pack(padx=50,pady=30)
        self.repeat_run()
        
        
        '''
        currentState = led.get()['led']
        if currentState:
           self.btn.open()
           GPIO.output(25,GPIO.HIGH)
        else:
           self.btn.close()
           GPIO.output(25,GPIO.LOW)
        '''

    def delete_delay(self):
        GPIO.cleanup()
        self.after_cancel(self.window_id)
        self.destroy()

   

    def repeat_run(self):
        print("run")
        self.window_id = self.after(1000,self.repeat_run)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25,GPIO.OUT)
    window = Window()
    window.protocol("WM_DELETE_WINDOW",window.delete_delay)
    window.mainloop()

if __name__ == "__main__":
    main()
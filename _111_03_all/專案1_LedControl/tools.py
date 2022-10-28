#自訂專案的module
import tkinter as tk
from PIL import Image,ImageTk

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
        self.config(font=('arial',18))
        self.config(compound=tk.LEFT)

    def open(self):
        self.config(image=self.open_photo)
        self.config(text="關")

    def close(self):
        self.config(image=self.close_photo);
        self.config(text="開")  
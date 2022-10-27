import tkinter as tk
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("private/raspberry1-58efc-firebase-adminsdk-tzk5o-2743aa1e4a.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://raspberry1-58efc-default-rtdb.firebaseio.com/'
})

led = db.reference('ledControl')

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立title
        self.title("LED Controller")

        #建立按鈕

        ##建立圖片
        close_image = Image.open('light_close.png')
        self.close_photo = ImageTk.PhotoImage(close_image)

        open_image = Image.open('light_open.png')
        self.open_photo = ImageTk.PhotoImage(open_image)

        self.btn = tk.Button(self,image=self.close_photo,padx=50,pady=30,font=('arial',18),command=self.userClick)
        self.btn.pack(padx=50,pady=30)
        currentState = led.get()['led']
        if currentState:
           self.btn.config(image=self.close_photo)
        else:
           self.btn.config(image=self.open_photo)
    
    def userClick(self):
        currentState = led.get()['led']
        led.update({'led':not currentState})
        if currentState:
           self.btn.config(image=self.open_photo)
        else:
           self.btn.config(image=self.close_photo)


def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()
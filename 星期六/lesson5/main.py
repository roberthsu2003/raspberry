import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk
import tk_tools

cred = credentials.Certificate('firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-e21c25a365.json')

firebase_admin.initialize_app(cred,{
    'databaseURL':'https://raspberryfirebase.firebaseio.com/'
})

ref = db.reference('raspberry2022/led')
print(ref.get())

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.led_state = False
        self.led = tk_tools.Led(self, size=50)       
        self.led.pack()
        self.switch_light()

    def switch_light(self):
        if self.led_state == False:
            self.led.to_grey()
        else:
            self.led.to_green()


if __name__ == "__main__":
    window = Window()
    window.title("LED控制")
    window.geometry("300x300")
    window.mainloop()

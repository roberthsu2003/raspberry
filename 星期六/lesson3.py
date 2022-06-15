import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin.exceptions import FirebaseError

import tkinter as tk

cred = credentials.Certificate("firebase_key/raspberryfirebase-firebase-adminsdk-y4f0x-e21c25a365.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
})


root = tk.Tk()
root.title('Radiobutton')
ref = db.reference('raspberrypi/Radiobutton')
var = tk.IntVar()
def colorChanged(event):
    if (type(event.data) is dict):
        print(event.data['color'])
        var.set(event.data['color'])
    else:
        print(event.data)
        var.set(event.data)

try:
    ref.listen(colorChanged)
except FirebaseError as e:
    print(e)

def getEvent(_):
    ref.set({
        'color':var.get()
    })
    


fruit=[('紅燈', 1), ('綠燈', 2), ('藍燈', 3)]
red=tk.Radiobutton(root, text='紅燈', value=1, variable=var,command=lambda:getEvent(red)).pack(anchor=tk.W)
green=tk.Radiobutton(root, text='綠燈', value=2, variable=var,command=lambda:getEvent(green)).pack(anchor=tk.W)
blue=tk.Radiobutton(root, text='藍燈', value=3, variable=var,command=lambda:getEvent(blue)).pack(anchor=tk.W)




root.mainloop()
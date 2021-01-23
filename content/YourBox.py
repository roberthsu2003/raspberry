from tkinter import *

class Linebox():
    def __init__(self,w):
        #設定視窗基本功能
        w.title('溫度和光線的感應')
        w.option_add("*font",("verdana",18,"bold"))
        w.option_add("*background", "#068587")
        w.option_add("*foreground", "#ffffff")

        #設定介面
        mainFrame = Frame(w,borderwidth=2,relief=GROOVE,padx=100,pady=10)
        Label(mainFrame, text="室內溫度:").pack()
        mainFrame.pack(padx=10, pady=10)
        

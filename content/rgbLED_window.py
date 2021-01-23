from tkinter import *

class RGBLED():
    def __init__(self,w):
        w.title('溫度和光線的感應')
        

if __name__ == "__main__":
    window = Tk()
    rgbLed = RGBLED(window)
    window.mainloop()
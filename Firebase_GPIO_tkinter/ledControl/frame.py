from tkinter import *

if __name__ == '__main__':
    app = Tk();
    app.title("LEDControl");
    #app.geometry("500x600");
    for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
        f = Frame(app,borderwidth=2, relief=relief, padx=10, pady=10)
        Label(f, text=relief,width=10).pack(side=LEFT)
        f.pack(side=LEFT, padx=5, pady=10)
        
    app.mainloop();
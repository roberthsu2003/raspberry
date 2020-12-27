from tkinter import *



class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Allan")
        
        label = Label(self, text="LCD Controller")
        label.pack(fill=BOTH, expand=True, padx=100, pady=50)
        
        hello_button = Button(self,text="Say Hello")
        hello_button.pack(side=LEFT, padx=(20,0), pady=(0, 20))
        
        goodbye_button = Button(self,text="Say Goodbye")
        goodbye_button.pack(side=RIGHT, padx=(0, 20), pady=(0, 20))
    
if __name__ == "__main__":
    window = Window()
    window.mainloop()
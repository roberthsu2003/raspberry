import tkinter as tk
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        image  = Image.open("light_open.png")
        self.lightImage = ImageTk.PhotoImage(image)
        print(image.size)
        canvas = tk.Canvas(self,width=image.size[0]+20,height=image.size[1]+40)
        canvas.create_image(10,10,anchor=tk.NW,image=self.lightImage)
        canvas.delete("all")
        image1  = Image.open("light_close.png")
        self.lightImage1 = ImageTk.PhotoImage(image1)
        canvas.create_image(10,10,anchor=tk.NW,image=self.lightImage1)
        

        #畫文字        
        canvas.create_text(20,95,anchor=tk.NW,text="燈開",font=("sans_arial",16))
        canvas.pack()


        
        

        
        

def main():
    window = Window()
    window.title("Canvas")
    window.geometry("400x300+300+200")
    window.mainloop()
    

if __name__ == "__main__":
    main()
import tkinter as tk 

def main():
    window = tk.Tk()
    window.title("first window")
    #window.geometry("800x300")
    btn = tk.Button(window,text="press me",padx=30,pady=20,font=('arial',20))
    btn.pack(padx=100,pady=100)
    
    window.mainloop()

if __name__ == "__main__":
    main()
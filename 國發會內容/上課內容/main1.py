import tkinter as tk 

def user_click():
    print("使用者按下")

def main():
    window = tk.Tk()
    window.title("first window")
    #window.geometry("800x300")
    btn = tk.Button(window,text="請按我",padx=30,pady=20,font=('arial',20),command=user_click)
    btn.pack(padx=100,pady=100)

    window.mainloop()

if __name__ == "__main__":
    main()
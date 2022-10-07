import tkinter as tk 
import RPi.GPIO as GPIO

def user_click():
    print("使用者按下")

def main():
    #GPIO 初始化
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)


    #視窗
    window = tk.Tk()
    window.title("first window")
    #window.geometry("800x300")
    btn = tk.Button(window,text="請按我",padx=30,pady=20,font=('arial',20),command=user_click)
    btn.pack(padx=100,pady=100)

    window.mainloop()

if __name__ == "__main__":
    main()
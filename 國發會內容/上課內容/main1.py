import tkinter as tk 
import RPi.GPIO as GPIO


def on_close():
    GPIO.output(25, GPIO.LOW)
    GPIO.cleanup()
    window.destroy()

def user_click():
    global ledState
    if ledState == True:
        GPIO.output(25, GPIO.LOW)
        ledState = False
        btn.config(text="開燈")
    else:
        GPIO.output(25, GPIO.HIGH)
        ledState = True
        btn.config(text="關燈")


def main():
    #GPIO 初始化
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)


    #視窗
    global btn
    global window
    window = tk.Tk()
    window.title("LED Control")
    window.protocol("WM_DELETE_WINDOW",on_close)
    #window.geometry("800x300")
    btn = tk.Button(window,text="開燈",padx=30,pady=20,font=('arial',20),command=user_click)
    btn.pack(padx=100,pady=100)

    window.mainloop()

if __name__ == "__main__":
    ledState = False
    btn = None
    window = None
    main()
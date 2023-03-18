import tkinter as tk
import RPi.GPIO as GPIO

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("按鈕")
        open_button = tk.Button(self, text="開啟電燈", command=self.open, padx=30,pady=30)
        open_button.pack(side=tk.LEFT, padx=20, pady=20)

        close_button = tk.Button(self, text="關閉電燈", command=self.close, padx=30,pady=30)
        close_button.pack(side=tk.LEFT, padx=20, pady=20)

    def open(self):
        print("開燈")
        GPIO.output(25, GPIO.HIGH)

    def close(self):
        print("關燈")
        GPIO.output(25, GPIO.LOW)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25,GPIO.OUT)
    window = Window()
    window.mainloop()
    
if __name__ == "__main__":
    main()
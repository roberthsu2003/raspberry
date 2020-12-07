from tkinter import *
class App:
        def __init__(self,master):
            master.geometry("800x800");
            fm1 = Frame(master);
            fm1Border = Frame(fm1,borderwidth=2,relief=GROOVE);
            self.__garageLayout(fm1Border);
            fm1Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm1.pack(side=TOP,expand=YES,fill=BOTH);
        
            fm2 = Frame(master);
            fm2Border = Frame(fm2,borderwidth=2,relief=GROOVE);
            self.__livingRoomLayout(fm2Border);
            fm2Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm2.pack(side=TOP,expand=YES,fill=BOTH);
            
            fm3 = Frame(master);
            fm3Border = Frame(fm3,borderwidth=2,relief=GROOVE);
            self.__bathRoomLayout(fm3Border);
            fm3Border.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            fm3.pack(side=TOP,expand=YES,fill=BOTH);
        
        def __garageLayout(self,frame):
            fm1Title = Label(frame,text="停車庫").pack(side=TOP,pady=10,padx=10,anchor=W);
            #parking
            parkingFrame=Frame(frame,background="#345678");
            parkingBorder = Frame(parkingFrame,borderwidth=2,relief=GROOVE,background="#345678");
            parkingTitle = Label(parkingFrame,text="停車狀態",background="#345678",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
            self.parkingMessageString = StringVar();
            parkingMessage = Label(parkingBorder,textvariable=self.parkingMessageString,background="#345678",foreground="white").pack(expand=YES);
            self.parkingMessageString.set("presented");
            parkingBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            parkingFrame.pack(side=LEFT,expand=YES,fill=BOTH);
            #gate
            gateFrame=Frame(frame,background="#876543");
            gateBorder = Frame(gateFrame,borderwidth=2,relief=GROOVE,background="#876543");
            gateTitle = Label(gateFrame,text="柵欄狀態",background="#876543",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
            self.gateTextString = StringVar();
            gateButton = Button(gateBorder,textvariable=self.gateTextString,command=self.changeGate).pack(expand=YES,fill=BOTH,padx=20,pady=20);
            self.gateTextString.set("Gate Open");
            gateBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            gateFrame.pack(side=LEFT,expand=YES,fill=BOTH);

        def changeGate(self):
            if self.gateTextString.get() == "Gate Open":
                    self.gateTextString.set("Gate Close");
            else:
                    self.gateTextString.set("Gate Open");
            

        def __livingRoomLayout(self,frame):
            fm2Title = Label(frame,text="一樓客廳").pack(side=TOP,pady=10,padx=10,anchor=W);
            #Door
            doorFrame=Frame(frame,background="#345678");
            doorBorder = Frame(doorFrame,borderwidth=2,relief=GROOVE,background="#345678");
            doorTitle = Label(doorFrame,text="Door狀態",background="#345678",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
            
            doorBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            doorFrame.pack(side=LEFT,expand=YES,fill=BOTH);
            #RGBLED
            rgbFrame=Frame(frame,background="#876543");
            rgbBorder = Frame(rgbFrame,borderwidth=2,relief=GROOVE,background="#876543");
            rgbTitle = Label(rgbFrame,text="RGB狀態",background="#876543",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
           
            rgbBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            rgbFrame.pack(side=LEFT,expand=YES,fill=BOTH);

        def __bathRoomLayout(self,frame):
            fm3Title = Label(frame,text="二摟臥室").pack(side=TOP,pady=10,padx=10,anchor=W);
            #LED
            ledFrame=Frame(frame,background="#345678");
            ledBorder = Frame(ledFrame,borderwidth=2,relief=GROOVE,background="#345678");
            ledTitle = Label(ledFrame,text="LED狀態",background="#345678",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
            
            ledBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            ledFrame.pack(side=LEFT,expand=YES,fill=BOTH);
            #lightness
            lightnessFrame=Frame(frame,background="#876543");
            lightnessBorder = Frame(lightnessFrame,borderwidth=2,relief=GROOVE,background="#876543");
            lightnessTitle = Label(lightnessFrame,text="Lightness狀態",background="#876543",foreground="white").place(relx=0.02,rely=0.00,anchor=NW)
           
            lightnessBorder.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=10);
            lightnessFrame.pack(side=LEFT,expand=YES,fill=BOTH);
    
            
root = Tk();
root.option_add("*font",("verdana",18));
root.title("Home");
display = App(root)
root.mainloop();

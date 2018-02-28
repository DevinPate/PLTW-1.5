import Tkinter
red_intvar = 0
green_intvar = 0
blue_intvar = 0
b1 = "up"
xold, yold = None, None
global xa
xa=0
mode = 2
colors=[]
colors.append("Red")
colors.append("Blue")
colors.append("Green")
colors.append("Orange")
colors.append("Yellow")
colors.append("Black")
colors.append("Gray")
colors.append("Magenta")
colors.append("#4B0082")
colors.append("Cyan")
colors.append("#593001")
colors.append("White")
def main():
    root = Tkinter.Tk()
    drawing_area = Tkinter.Canvas(root, width=1280, height=720)
    drawing_area.grid(row=1, column=3,rowspan=3)
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)

    def Blacks():
        global xa
        xa=6
    def Reds():
        global xa
        xa = 1

    def Blues():
        global xa
        xa = 2

    def Greennn():
        global xa
        xa = 3

    def Oranges():
        global xa
        xa = 4

    def Yellows():
        global xa
        xa = 5

    def Grayy():
        global xa
        xa = 7

    def Magicenta():
        global xa
        xa = 8

    def Pureple():
        global xa
        xa = 9

    def Ceean():
        global xa
        xa = 10

    def Broon():
        global xa
        xa = 11
    def Wheete():
        global xa
        xa = 12
    def bubbble():
        global mode
        mode = 1
    def pennn():
        global mode
        mode = 2
    def clear():
        drawing_area.delete("all")
    def rectpenn():
        global mode
        mode = 3
    root = Tkinter.Tk()
    frame = Tkinter.Frame(root)
    frame.pack()
    Redd = Tkinter.Button(frame,
                          #text="Red",
                          text="     ",
                          bg="Red",
                          command=Reds)
    Redd.grid(row=1, column=1, rowspan=1, sticky=Tkinter.W)
    Bluee = Tkinter.Button(frame,
                           #text="Blue",
                           text="     ",
                            bg="Blue",
                           command=Blues)
    Bluee.grid(row=1, column=2, rowspan=1, sticky=Tkinter.W)
    Greenn = Tkinter.Button(frame,
                            bg="Green", #text="Green",
                             text="     ",
                            command=Greennn)

    Greenn.grid(row=2, column=1, rowspan=1, sticky=Tkinter.W)
    Grayy = Tkinter.Button(frame,
                           bg="Gray",
                           text="     ",

                           command=Grayy)

    Grayy.grid(row=4, column=1, rowspan=1, sticky=Tkinter.W)
    Magicenta = Tkinter.Button(frame,
                           bg="Magenta",
                           text="     ",

                           command=Magicenta)

    Magicenta.grid(row=4, column=2, rowspan=1, sticky=Tkinter.W)
    Broon = Tkinter.Button(frame,
                           bg="#593001",
                           text="     ",

                           command=Broon)

    Broon.grid(row=6, column=1, rowspan=1, sticky=Tkinter.W)
    Ceean = Tkinter.Button(frame,
                           bg="Cyan",
                           text="     ",

                           command=Ceean)

    Ceean.grid(row=5, column=2, rowspan=1, sticky=Tkinter.W)
    button = Tkinter.Button(frame,
                            #text="Orange",
                            text="     ",
                            bg="Orange",
                            command=Oranges)
    button.grid(row=2, column=2, rowspan=1, sticky=Tkinter.W)
    Wheete = Tkinter.Button(frame,
                            #text="Orange",
                            text="     ",
                            bg="White",
                            command=Wheete)
    Wheete.grid(row=6, column=2, rowspan=1, sticky=Tkinter.W)

    slogan = Tkinter.Button(frame,
                            #text="Yellow",
                            text="     ",
                            bg="Yellow",
                            command=Yellows)
    slogan.grid(row=3, column=1, rowspan=1, sticky=Tkinter.W)
    Pureple = Tkinter.Button(frame,
                            text="     ",
                            bg="#4B0082",
                            command=Pureple)
    Pureple.grid(row=5, column=1, rowspan=1, sticky=Tkinter.W)
    Blackk = Tkinter.Button(frame,
                            #text="Black",
                            text="     ",
                            bg="Black",fg="white",
                            command=Blacks)
    Blackk.grid(row=3, column=2, rowspan=1, sticky=Tkinter.W)
    bubble = Tkinter.Button(frame,
                            text="Bubble pen",
                            command=bubbble)
    bubble.grid(row=7, column=1, rowspan=1, sticky=Tkinter.W)
    penn = Tkinter.Button(frame,
                         text="Pen",
                         command=pennn)
    penn.grid(row=7, column=2,rowspan=1, sticky=Tkinter.W)
    rectpen = Tkinter.Button(frame,
                             text="Rect pen",
                             command=rectpenn)
    rectpen.grid(row=8,column=1,rowspan=1,sticky=Tkinter.W)
    quitt = Tkinter.Button(frame,
                           text="   Quit   ", bg="Red",fg="Black",
                           command=quit)
    quitt.grid(row=9,column=1, columnspan=2, sticky=Tkinter.W)
    clearr = Tkinter.Button(frame,
                            text="  Clear   ",
                            command=clear)
    clearr.grid(row=10, column=1,columnspan=2, sticky=Tkinter.W)

    root.mainloop()
def b1down(event):
    global b1
    b1 = "down"

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None and mode is 1:
            event.widget.create_oval(xold,yold,event.x,event.y,fill=colors[xa-1])

        if xold is not None and yold is not None and mode is 2:
            event.widget.create_line(xold,yold,event.x,event.y,fill=colors[xa-1],smooth=True)
        if xold is not None and yold is not None and mode is 3:
            event.widget.create_rectangle(xold, yold, event.x, event.y, fill=colors[xa - 1],outline=colors[xa - 1])

        xold = event.x
        yold = event.y
if __name__ == "__main__":
    main()



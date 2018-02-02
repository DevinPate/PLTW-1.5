#####
# bouncing_ball.py
#
# Creates a Scale and a Canvas. Animates a circle based on the Scale
# (c) 2013 PLTW
# version 11/1/2013
####


import Tkinter #often people import Tkinter as *
shapes = []



#####
# Create root window
####
root = Tkinter.Tk()

#####
# Create Model
######
speed_intvar = Tkinter.IntVar()
speed_intvar.set(3) # Initialize y coordinate
# radius and x-coordinate of circle
r = 10
x = 150
y = 150
freeze=0

direction = 0.5 # radians of angle in standard position, ccw from positive x axis
def nothing():
        print("What did you expect?" or "Why?")
######
# Create Controller
#######
# Instantiate and place slider
button = Tkinter.Button(root,text="Nothing",fg="blue", command=nothing)
button.grid(row=2, column=0)
speed_slider = Tkinter.Scale(root, from_=600, to=0, variable=speed_intvar,
                              label='Speed')
speed_slider.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\nspeed.')
text.grid(row=0, column =0)

######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r,
                                 outline='#000000', fill='#00FFFF')
import math
def animate():
    global speed_intvar
    # Get the slider data and create x- and y-components of velocity
    velocity_x = speed_intvar.get() * math.cos(direction) # adj = hyp*cos()
    velocity_y = speed_intvar.get() * math.sin(direction) # opp = hyp*sin()
    # Change the canvas item's coordinates
    canvas.move(circle_item, velocity_x, velocity_y)
    # Get the new coordinates and act accordingly if ball is at an edge
    x1, y1, x2, y2 = canvas.coords(circle_item)
    global direction
    # If crossing left or right of canvas
    if x2>canvas.winfo_width() or x1<0:
        direction = math.pi - direction # Reverse the x-component of velocity
    # If crossing top or bottom of canvas
    if y2>canvas.winfo_height() or y1<0:
        direction = -1 * direction # Reverse the y-component of velocity

    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion
    canvas.after(1, animate)
# Call function directly to start the recursion
animate()

#######
# Event Loop
#######
root.mainloop()
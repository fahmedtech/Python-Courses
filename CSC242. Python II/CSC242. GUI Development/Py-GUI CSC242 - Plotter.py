'''
Python CSC242
GUI Development

'''
#Plotter
#Run Module for Program to execute (F5)

from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

#Event Handlers
def up():
    'move pen up 10 pixels | y is modified'
    global y, canvas                  
    canvas.create_line(x, y, x, y-10)
    y -= 10

def down():
    'move pen down 10 pixels | y is modified'
    global y, canvas                  
    canvas.create_line(x, y, x, y+10)
    y += 10

def left():
    'move pen left 10 pixels | x is modified'
    global x, canvas                  
    canvas.create_line(x, y, x-10, y)
    x -= 10

def right():
    'move pen right 10 pixels | x is modified'
    global x, canvas                  
    canvas.create_line(x, y, x+10, y)
    x += 10

#GUI
root = Tk()

# canvas with border of size 100 x 150
canvas = Canvas(root, height=100, width=150, relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

# frame to hold the 4 buttons
box = Frame(root)
box.pack(side=RIGHT)

#4 button widgets have Frame widget box as their master
button1 = Button(box, text='up', command=up)
button1.grid(row=0, column=0, columnspan=2)

button2 = Button(box, text='left',command=left)
button2.grid(row=1, column=0)

button3 = Button(box, text='right', command=right)
button3.grid(row=1, column=1)

button4 = Button(box, text='down', command=down)
button4.grid(row=2, column=0, columnspan=2)

# pen position, initially in the middle
x, y = 50, 75 

root.mainloop()

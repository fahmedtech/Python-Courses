#Class: Draw()
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> from tkinter import *
>>> root = Tk()
>>> Draw(root)
<__main__.Draw object at 0x000000000345CE48>
'''

from tkinter import Canvas, Frame, BOTH

class Draw(Frame):
    'a basic drawing application'

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        #mouse coordinates | instance variables
        self.oldX, self.oldY = 0, 0

        #creating canvas | bind mouse events to handlers
        self.canvas = Canvas(self, height=250, width=250)

        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)

    def begin(self, event):
        'handles left button click by recording mouse position'
        self.oldX, self.oldY = event.x, event.y

    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
           connecting the previous mouse position to the new one'''
        newX, newY = event.x, event.y

        self.canvas.create_line(self.oldX, self.oldY, newX, newY)

        self.oldX, self.oldY = newX, newY

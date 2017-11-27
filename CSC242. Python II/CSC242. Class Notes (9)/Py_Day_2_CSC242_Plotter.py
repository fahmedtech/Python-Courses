#Class Plotter()
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> root = Tk()
>>> Plotter(root)
<__main__.Plotter object .47688112>
'''

from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

class Plotter(Frame):
    'a simple pen drawing app'
    
    def __init__(self, parent=None):
        'arrange canvas and 4 button widgets controling the pen'
        Frame.__init__(self, parent)
        self.pack()

        self.x = 75                # x-coordinate of pen
        self.y = 50                # y-coordinate of pen

        self.canvas = Canvas(self, height=100, width=150,
                             relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        buttons = Frame(self)
        buttons.pack(side=RIGHT)

        # create up button
        b = Button(buttons, text='up', command=self.up)
        b.grid(row=0, column=0, columnspan=2)
        
        # create left button
        b = Button(buttons, text='left', command=self.left)
        b.grid(row=1, column=0)
        
        # create right button
        b = Button(buttons, text='right', command=self.right)
        b.grid(row=1, column=1)
        
        # create down button
        b = Button(buttons, text='down', command=self.down)
        b.grid(row=2, column=0, columnspan=2)

    #event handling Methods
        
    def up(self):
        'move pen up 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x, self.y-10)
        self.y -= 10

    def down(self):
        'move pen down 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x, self.y+10)
        self.y += 10

    def left(self):
        'move pen left 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x-10, self.y)
        self.x -= 10

    def right(self):
        'move pen right 10 pixels'
        self.canvas.create_line(self.x, self.y, self.x+10, self.y)
        self.x += 10

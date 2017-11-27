'''
Python CSC242
HW5 Solutions
'''

from tkinter import *
from tkinter.messagebox import showinfo
from random import randrange


#Problem 1 & 2 - Plotter()
'''
>>> Plotter().mainloop()
Then Press '<TAB>' to start using Arrow Keys for Pen

Alternative Way:
>>> root = Tk()
>>> Plotter(root).pack()
>>> root.mainloop()
'''

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
        self.canvas.bind('<Up>', self.up)
        self.canvas.bind('<Down>', self.down)
        self.canvas.bind('<Left>', self.left)
        self.canvas.bind('<Right>', self.right)

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

        Button(buttons, text='clear', command=self.clear).grid(row=3, column=0)
        Button(buttons, text='delete', command=self.delete).grid(row=3, column=1)
        
        self.moves = []
        self.positions = []

    def clear(self):
        self.canvas.delete(ALL)
        self.moves = []
        self.positions = []
        self.x = 75                # x-coordinate of pen
        self.y = 50                # y-coordinate of pen

    def delete(self):
        self.canvas.delete(self.moves.pop())
        self.x, self.y = self.positions.pop()

    #moving plotter pen - EVENT HANDLERS
    def up(self, event=None):
        'move pen up 10 pixels'
        self.moves.append(self.canvas.create_line(self.x, self.y, self.x, self.y-10))
        self.positions.append((self.x, self.y))
        self.y -= 10
        

    def down(self, event=None):
        'move pen down 10 pixels'
        self.moves.append(self.canvas.create_line(self.x, self.y, self.x, self.y+10))
        self.positions.append((self.x, self.y))
        self.y += 10

    def left(self, event=None):
        'move pen left 10 pixels'
        self.moves.append(self.canvas.create_line(self.x, self.y, self.x-10, self.y))
        self.positions.append((self.x, self.y))
        self.x -= 10

    def right(self, event=None):
        'move pen right 10 pixels'
        self.moves.append(self.canvas.create_line(self.x, self.y, self.x+10, self.y))
        self.positions.append((self.x, self.y))
        self.x += 10

#Problem 3: BMI()
'''
>>> BMI().mainloop()

Alternative Way:
>>> root = Tk()
>>> BMI(root).pack()
>>> root.mainloop()
'''

class BMI(Frame):
    def __init__(self, parent=None):
        
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Enter your weight:").grid(row=0, column=0)
        Label(self, text="Enter your height:").grid(row=1, column=0)
        self.wEnt = Entry(self,width=36)
        self.wEnt.grid(row=0, column=1)
        self.hEnt = Entry(self,width=36)
        self.hEnt.grid(row=1, column=1)
        Button(self, text="Compute BMI", command=self.compute).grid(row=2, column=0, columnspan=21)

    def compute(self):
        weight = int(self.wEnt.get())
        height = int(self.hEnt.get())
        bmi = weight*703/height**2
        showinfo(message='Your BMI is {}'.format(bmi))
        self.wEnt.delete(0, END)
        self.hEnt.delete(0, END)

#Problem 4: GUI Craps()
'''
>>> Craps().mainloop()

Alternative Way:
>>> root=Tk()
>>> Craps(root).pack()
>>> root.mainloop()
'''

class Craps(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.pack()
        
        Label(self, text="Your Roll:").pack()
        self.ent = Entry(self,width=36)
        self.ent.pack()
        
        frame = Frame(self)
        frame.pack()
        Button(frame, text="New Game", command=self.newGame).pack(side='left')
        Button(frame, text="Roll For Point", command=self.forPoint).pack(side='left')

    def newGame(self):    
        self.initial = randrange(1,7) + randrange(1,7)
        self.ent.delete(0,END)
        
        if self.initial in [7,11]:
            self.ent.insert(END, "Throw total: {}... you won!".format(self.initial))
        elif self.initial in [2,3,12]:
            self.ent.insert(END, "Throw total: {}... you lost.".format(self.initial))
        else:
            self.ent.insert(END, "Throw total: {}... Throw for point.".format(self.initial))

    def forPoint(self):
        tmp = randrange(1,7) + randrange(1,7)
        self.ent.delete(0,END)
        
        if tmp == self.initial:
            self.ent.insert(END, "Throw total: {}... you won!".format(tmp))
        elif tmp == 7:
            self.ent.insert(END, "Throw total: {}... you lost.".format(tmp))
        else:
            self.ent.insert(END, "Throw total: {}... Throw for point.".format(tmp))
   

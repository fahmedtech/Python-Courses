#Class: MegaGUI() - Requires Both Draw() and Plotter Classes 
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> root = Tk()
>>> MegaGUI(root).pack()
>>> root.mainloop()
'''

from tkinter import Frame, Tk
from Py_Day_2_CSC242_Draw import Draw
from Py_Day_2_CSC242_Plotter import Plotter

class MegaGUI(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)

        Draw(self).pack()
        Plotter(self).pack()

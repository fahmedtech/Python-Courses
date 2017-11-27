'''
Python CSC242
Day 2 - 7/1/2016
'''

'''
**Concept: __str__ vs __repr__

object.__repr__(self): called by the repr() built-in function and by string
conversions (reverse quotes) to compute the "official" string representation
of an object.

object.__str__(self): called by the str() build-in function and by the print
statement to compute the "informal" string representation of an object.

Implement __repr__ for every class you implement. There should be no excuse.
Implement __str__ for classes which you think readability is more important
of non-ambiguity.

>>> x = 1
>>> repr(x)
'1'
>>> str(x)
'1'

>>> y = 'a string'
>>> repr(y)
"'a string'"
>>> str(y)
'a string'

**Concept Practice.
In order to check the Libraries and its Functions follow these steps in shell!

Import the Library
>>> import tkinter
Now in Shell type the library name and . and press TAB to see its functions
>>> tkinter.messagebox. (Here you can now press TAB)
'''

#Class 1: Rep()
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = Rep()
>>> obj
Official String Representation
>>> print(obj)
Informal String Representation
'''

class Rep:

    def __repr__(self):
        return "Official String Representation"

    def __str__(self):
        return "Informal String Representation"

#Program 2: Using tkinter GUI Libraries
#Run Module for Program to execute (F5)

from tkinter import *
from random import randrange
from tkinter.messagebox import showinfo

def guessGame():
    global _entry

    inp_num = int(_entry.get())
    _entry.delete(0, END)

    _secretVal = randrange(1, 4)

    if(inp_num == _secretVal):
        showinfo(message =
                 "You Guessed It! \nSecret Value is {}.".format(_secretVal))
    else:
        showinfo(message =
                 "Bad Luck :( \nSecret Value is {}.".format(_secretVal))

root = Tk()

label = Label(root, text="Guess Number from 1-3: ")
button = Button(root, text="Submit", command=guessGame)

_entry = Entry(root)
label.pack(side=TOP)
_entry.pack(side=TOP)
button.pack(side=BOTTOM)   

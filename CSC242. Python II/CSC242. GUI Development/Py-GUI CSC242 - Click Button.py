'''
Python CSC242
GUI Development

'''
#Click Button to display PC Time
#Run Module for Program to execute (F5)

from tkinter import Tk, Button
# alternate version:
# from tkinter.messagebox import showinfo

from time import strftime, localtime

def clicked():
    'prints day and time info'
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    print(time)
    # alternate version:
    # showinfo(message = time)

#GUI
    
root = Tk()

# create button labeled 'Click it' and event handler clicked()
button = Button(root,
                text='Click it',   # text on top of button
                command=clicked)   # button click event handler

button.pack()
root.mainloop()

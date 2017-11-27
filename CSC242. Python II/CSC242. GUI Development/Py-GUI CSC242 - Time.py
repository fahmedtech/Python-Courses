'''
Python CSC242
GUI Development

>>>
Local Time
Day:  02 Jul 2016
Time: 16:34:41 PM

Greenwich time
Day:  02 Jul 2016
Time: 21:34:43 PM
'''
#Check Local and Greenwich Time
#Run Module for Program to execute (F5)

from tkinter import Tk, Button, LEFT, RIGHT
from time import strftime, localtime, gmtime

def localTime():
    'print local PC day and time'

    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    print('Local Time\n' + time)

def greenwichTime():
    'prints Greenwich day and time info'
    
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                    gmtime())
    print('Greenwich time\n' + time)

#GUI
root = Tk()

button1 = Button(root, text='Local Time',
                 command=localTime)
button2 = Button(root, text='Greenwich Time',
                 command=greenwichTime)

button1.pack(side = LEFT)
button2.pack(side = RIGHT)
root.mainloop()

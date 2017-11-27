'''
Python CSC242
HW6 Solutions
'''

from tkinter import *
from calendar import monthrange
from tkinter.simpledialog import askstring

#Problem 1: Calendar() - GUI
'''
>>> year = 2017
>>> month = 7
>>> _weekday, _numDays = monthrange(year, month)
>>> _weekday
5
>>> _numDays
31

>>> Calendar(2016, 7).mainloop()
'''

class Calendar(Frame):

    #constructor
    def __init__(self, year, month, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.year, self.month = year, month

        self.calDict = {}
        
        Calendar.make_widgets(self)

    def make_widgets(self):
        arrDays = ['MON','TUE','WED','THU','FRI','SAT','SUN']

        _weekday, _numDays = monthrange(self.year, self.month)

        #initializing Days Label on Grid
        for i in range(len(arrDays)):
            Label(self, text = arrDays[i]).grid(row = 0, column = i)

        #initializing Dates Button on Grid 
        _week = 1
        for i in range(1, _numDays +1):

            def cmd(x = i):
                self.click(x)

            Button(self, text=str(i), command=cmd).grid(row = _week,
                                                        column = _weekday)
            _weekday += 1

            if(_weekday > 6):
                _week += 1
                _weekday = 0

    #When Date Button <Clicked> enter information.
    def click(self, i):
        if(i not in self.calDict):
            self.calDict[i] = askstring('example', 'Enter Text')

        else:
            self.calDict[i] = askstring('example', 'Enter Text',
                                        initialvalue = self.calDict[i])

#Problem 2: BMI() - GUI
'''
>>> MyApp(2016, 7).mainloop()
'''
            
from Py_HW_5_CSC242 import BMI
from calc import Calc

class MyApp(Frame):

    def __init__(self, year, month, master=None):
        Frame.__init__(self, master)
        self.pack()

        Calc(self).pack(side=RIGHT)
        BMI(self).pack(side=LEFT)

#Problem 3: silly() - RECURSIVE
'''
>>> silly(0)
>>> silly(1)
*!
>>> silly(3)
***!!!
>>> silly(10)
**********!!!!!!!!!!
'''

def silly(int_num):

    if(int_num > 0):
        print('*', end='')
        silly(int_num -1)
        print('!', end='')

#Problem 4: numOnes(<integer>) - RECURSIVE
'''
>>> numOnes(0)
0
>>> numOnes(1)
1
>>> numOnes(3)
2
>>> numOnes(15)
4
'''

def numOnes(int_num):
    'return number of 1s in the binary representation of int_num'

    if(int_num == 0):
        return 0

    tempVal = numOnes(int_num // 2)

    if(int_num % 2):
        return 1 + tempVal
    else:
        return tempVal

#Problem 5: design(<integer>) - RECURSIVE

def design(int_num):

    if(int_num > 0):
        design(int_num -1)
        print(int_num * '*')
        design(int_num -1)

##### TESTING ALL METHODS #####

if __name__ == '__main__':

    print("--- silly() ---") 
    silly(0); print()
    silly(1); print()
    silly(3); print()
    silly(10); print()

    print("\n--- numOnes(<int>) ---") 
    print(numOnes(0))
    print(numOnes(1))
    print(numOnes(3))
    print(numOnes(15))

    print("\n--- design(<int>) ---") 
    design(0)
    design(1)
    design(2)
    design(4)

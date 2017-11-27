'''
Python CSC242
Day 7 - 7/8/2016
'''

#Program 1: Return most frequent occurring item in non-empty list
#Run Module for Program to execute (F5)
#Type Frequent(<list>) - Name of Method in Shell to execute.
'''
>>> Frequent([1,6,9,8,1,1,2,5])
1
>>> Frequent(['david','pedro','gabriel','david','pedro','david'])
'david'
'''

def Frequent(lst):
    lst.sort()

    _currLen = 1            #length of current sequence
    _longLen = 1            #length of longest sequence
    _mostFreq = lst[0]      #item with longest sequence

    for i in range(1, len(lst)):

        if(lst[i] == lst[i -1]):
            _currLen += 1

        else:
            #update longest sequence if necessary
            #condition: if sequence ended is longest so far, store its length & item
            if(_currLen > _longLen):

                _longLen = _currLen
                _mostFreq = lst[i -1]

            _currLen = 1
    return _mostFreq

#Program 2: Print digits in new line (Recursive)
#Run Module for Program to execute (F5)
#Type Reverse(<integer>) - Name of Method in Shell to execute.
'''
>>> Reverse(895001)
1
0
0
5
9
8
'''

def Reverse(int_num):

    if(int_num < 10):
        print(int_num)

    else:
        print(int_num % 10)
        Reverse(int_num // 10)

#Program 3: Factorial (New Recursive)
#Run Module for Program to execute (F5)
#Type Factorial(<integer>) - Name of Method in Shell to execute.
'''
>>> Factorial(5)
120
>>> Factorial(3)
6
'''

def Factorial(int_num):

    if(int_num in [0, 1]):
        return 1
    else:
        return Factorial(int_num -1) * int_num

#Program 4: Drawing Pattern 
#Run Module for Program to execute (F5)
#Type Pattern(<integer>) - Name of Method in Shell to execute.
'''
>>> Pattern(3)
*
**      printing Pattern(2) or (3 -1) 
*
-----
***     print(int_num * '*')
-----
*
**      printing Pattern(2) or (3 -1)
*
'''

def Pattern(int_num):

    if(int_num > 0):
        Pattern(int_num -1)
        print(int_num * '*')
        Pattern(int_num -1)

#Program 5: Drawing Snowflake Curve using Koch() 3 Times
#Run Module for Program to execute (F5)
#Type DrawSnowflake(<integer>) - Name of Method in Shell to execute.
'''
>>> Koch(1)
'FLFRFLF'
>>> DrawSnowflake(5)
'''

from turtle import *

def Koch(int_num):
    if(int_num == 0):
        return 'F'

    tempVal = Koch(int_num -1)
    return tempVal + 'L' + tempVal + 'R' + tempVal + 'L' + tempVal


def DrawSnowflake(int_num):
    _screen = Screen()
    _turtle = Turtle()
    _directions = Koch(int_num)

    for i in range(3):
        for item in _directions:
            if(item == 'F'):
                _turtle.fd(300 / 3 ** int_num)
            if(item == 'L'):
                _turtle.lt(60)
            if(item == 'R'):
                _turtle.rt(120)

        _turtle.rt(120)
    #_screen.bye()
    

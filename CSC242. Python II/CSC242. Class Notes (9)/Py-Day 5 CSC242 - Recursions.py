'''
Python CSC242
Day 5 - 7/4/2016

More RECURSIONS
'''

#Program 1: Printing Patterns with Integers
#Run Module for Program to execute (F5)
#Type Pattern(<integer>) - Name of Method in Shell to execute.
'''
>>> Pattern(3)
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 
'''

def Pattern(int_num):

    if(int_num == 0):
        print(0, end =' ')

    else:
        Pattern(int_num -1)
        print(int_num, end=' ')
        Pattern(int_num -1)

#Program 2: Drawing Koch Curve
#Run Module for Program to execute (F5)
#Type Koch(<integer>) - Name of Method in Shell to execute.
#Type DrawKoch(<integer>) - Name of Method in Shell to execute.
'''
>>> Koch(2)
'FLFRFLFLFLFRFLFRFLFRFLFLFLFRFLF'
'''

def Koch(int_num):

    if(int_num == 0):
        return 'F'

    tempVal = Koch(int_num -1)

    return tempVal + 'L' + tempVal + 'R' + tempVal + 'L' + tempVal

'''
>>> DrawKoch(2)
'''
from turtle import Screen, Turtle

def DrawKoch(int_num):

    s = Screen()
    t = Turtle()
    direction = Koch(int_num)

    for item in direction:
        if(item == 'F'):
            t.forward(300 / 3 ** int_num)
        if(item == 'L'):
            t.lt(60) #rotate left 60 degrees
        if(item == 'R'):
            t.rt(120) #rotate right 60 degrees

    s.bye()

#Program 3: Scanning Definition of Virus in Files|Folders
#Run Module for Program to execute (F5)
#Type scan(<string>, <dictionary>) - Name of Method in Shell to execute.
'''
>>> sigDict = {'Creeper':'ye8009g2h1azzx33', 'Code RED':'99dh1cz963bsscs3',
               'Blaster':'fdp1102k1ks6hgbc'}

>>> scan("Py_Day 5 CSC242_Recursions_Test", sigDict)
Py_Day 5 CSC242_Recursions_Test\test\fileA.txt, found virus Creeper
Py_Day 5 CSC242_Recursions_Test\test\folder1\fileB.txt, found virus Creeper
Py_Day 5 CSC242_Recursions_Test\test\folder1\fileC.txt, found virus Code RED
Py_Day 5 CSC242_Recursions_Test\test\folder1\folder11\fileD.txt, found virus Code RED
Py_Day 5 CSC242_Recursions_Test\test\folder2\fileD.txt, found virus Blaster
Py_Day 5 CSC242_Recursions_Test\test\folder2\fileE.txt, found virus Blaster
'''

import os
def scan(pathname, signatures):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''

    for item in os.listdir(pathname):       # for every file or folder 
                                            # in folder pathname 
        # create pathname for item called next
        # next = pathname + '/' + item	    # Mac only
        # next = pathname + '\' + item	    # Windows only
        next = os.path.join(pathname, item) # any OS

        try: # blindly recurse on next
            scan(next, signatures)
        except: # base case: exception means that item is a file
            # for every virus signature
            for virus in signatures:

                # check if file next has the virus signature
                if open(next).read().find(signatures[virus]) >= 0:
                    print('{}, found virus {}'.format(next,virus))

#Program 4: Covert power() to Recursive
#Run Module for Program to execute (F5)
#Type RPower(<integer>, <integer>) - Name of Method in Shell to execute.
'''
def power(a, n):
    'returns a to the nth power'
    res = 1
    for i in range(n):
        res *= a
    return res

>>> RPower(2, 3)
8
>>> RPower(2, 2)
4
>>> RPower(3, 2)
9
>>> RPower(3, 3)
27
'''

def RPower(int_num, int_pow):

    if(int_pow == 0):
        return 1

    #Recursive Step
    tempVal = RPower(int_num, int_pow // 2)

    if(int_pow % 2 == 0):
        return tempVal * tempVal    # a**n = a**(n//2) * a**a(n//2)
    else:
        return int_num * tempVal * tempVal
        # a**n = a**(n//2) * a**a(n//2) * a

#Other Recursive Version
def RPowerV2(int_num, int_pow):
    'returns a to the nth power'
    _counter = 1     # counts number of multiplications

    if(int_pow == 0):
        return 1
    
    tempVal = RPowerV2(int_num, int_pow // 2)

    if(int_pow % 2 == 0):
        _counter += 1
        return tempVal * tempVal     # 1 multiplication

    # n%2==1
    else: 
        _counter += 2
        return int_num * tempVal * tempVal    # 2 multiplications

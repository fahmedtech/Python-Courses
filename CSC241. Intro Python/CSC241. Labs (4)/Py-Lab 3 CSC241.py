'''
Python CSC241
Lab 3 - 6/24/2016
'''

#Lab 5

#Program 1:
'''
Create a function Monogram that makes this work:

>>> help(Monogram)
Help on function monogram in module __main__:

Monogram(str_longname)
    given a longname -  a string with a names (e.g. first/middle/last)
    separated by spaces, returns its monogram, a string consisting of
    the first letters of each sub-name, each capitalized

>>> Monogram('cher')
'C'
>>> Monogram('George Washington')
'GW'
>>> Monogram('george herbert walker bush')
'GHWB'
'''
#Run Module for Program to execute (F5)
#Type Monogram(<string>) - Name of Method in Shell to execute.

def Monogram(str_longname):
    '''given a longname -  a string with a names (e.g. first/middle/last)
    separated by spaces, returns its monogram, a string consisting of
    the first letters of each sub-name, each capitalized'''

    nameList = str_longname.split()
    retVal = ''

    for item in nameList:
        retVal += item[0].upper()
    return retVal

#Program 2:
'''
Write a function RetEmpPay() that takes as a parameter two numbers,
the first of which represents an employee's hourly pay rate and
the second of which represents the number of hours the employee worked.
The function computes and returns the employee's pay for the pay period.
Any hours beyond 40 and less than 60 should be paid overtime at 1.5 times
the regular hourly rate.  Any hours greater than 60 should be paid at 2 times
the houry rate.

>>> RetEmpPay(10,35)
350
>>> RetEmpPay(10,45)
475.0
>>> RetEmpPay(10,61)
620
'''
#Run Module for Program to execute (F5)
#Type RetEmpPay(<float>, <integer>) - Name of Method in Shell to execute.

def RetEmpPay(hourly_rate, hours_worked):

    regPay = hourly_rate * hours_worked

    if(hours_worked <= 40):
        return regPay
    elif(hours_worked > 40 and hours_worked < 60):
        return (40 * 10 + (hours_worked - 40) * (hourly_rate * 1.5))
    elif(hours_worked > 60):
        return (60 * 10 + (hours_worked - 60) * (hourly_rate * 2))

#Program 3:
'''
Implement a function RetAverageLenWord() that takes one parameter which is a string
representing the name of a text file.  The function should return the average
length of a word in the file.  You may assume that the file contains no
punctuation.  If the file is empty, the function should return 0.

>>> RetAverageLenWord('Py-Lab 3 CSC241 - empty.txt')
0.0
>>> RetAverageLenWord('Py-Lab 3 CSC241 - ex1.txt')
4.35
>>> RetAverageLenWord('Py-Lab 3 CSC241 - ex2.txt')
4.52
'''
#Run Module for Program to execute (F5)
#Type RetAverageLenWord(<string>) - Name of Method in Shell to execute.

def RetAverageLenWord(filename):
    _totalLength = 0
    
    ifile = open(filename, 'r')
    content = ifile.read()
    ifile.close()

    wordList = content.split()
    _totalWords = len(wordList)
    
    for item in wordList:
        _totalLength += len(item)

    try:
        return round(_totalLength / _totalWords, 2)
    except ZeroDivisionError:
        return 0.0

#Lab 6

#Program 4:
'''
Write a function MultiplesOf() that takes a list lst of numbers
and a positive integer (> 0) n as parameters and prints the indices of
the numbers in lst that are multiples of n, one per line.
If lst is empty, n is zero or negative, or there are no items in lst that
are multiples of n, the function should not print anything.  

>>> MultiplesOf(3, [3,1,6,2,7,9,10,20,5])
0 2 5
>>> MultiplesOf(5, [3,1,6,2,7,9,10,20,5])
6 7 8
>>> MultiplesOf(13, [3,1,6,2,7,9,10,20,5])
>>> MultiplesOf(-5, [3,1,6,2,7,9,10,20,5])
>>> MultiplesOf(0, [3,1,6,2,7,9,10,20,5])
>>> MultiplesOf(2, [])
>>> MultiplesOf(13, [3,1,6,2,7,9,10,13,20,5])
7 
'''
#Run Module for Program to execute (F5)
#Type MultiplesOf(<integer>, <list>) - Name of Method in Shell to execute.

def MultiplesOf(int_num, int_list):

    for i in range(len(int_list)):

        if(int_num <= 0):
            return
        if(int_list[i] % int_num == 0):
            print(i, end=' ')

#Program 5:
'''
Write a function RetDoubles() that takes as a list of integers
as a parameter and prints the values in the list, one per line,
that are exactly twice the previous value in the list.
If the list is empty or there are no values that are double the value of
their predecessor, then the function does not print anything.
The list provided as a parameter should not be changed.
Note that the first item in the list will never be printed since it does not
have a predecessor in the list.

>>> RetDoubles( [4,8,-12,-24,48,3,6,12,24,0])
8 -24 6 12 24
>>> RetDoubles(([1,2,3,4,5]))
2
>>> RetDoubles([9])
>>> RetDoubles([])
'''
#Run Module for Program to execute (F5)
#Type RetDoubles(<list>) - Name of Method in Shell to execute.

def RetDoubles(int_list):

    for i in range(len(int_list) -1): #not printing the predecessor
        
        if(int_list[i] * 2 == int_list[i+1]):
            print(int_list[i+1], end=' ')

#Program 6:
'''
Write a function OddSpots() that takes as a list of integers
returns a list of the indices of all odd numbers on that list.

>>> OddSpots([0,5,7,1,2,5,44,12])
[1, 2, 3, 5]
>>> OddSpots([2,4,8,12])
[]
>>> OddSpots([])
[]
'''
#Run Module for Program to execute (F5)
#Type OddSpots(<list>) - Name of Method in Shell to execute.

def OddSpots(int_list):
    oddList = []

    for i in range(len(int_list)):
        if(int_list[i] % 2 == 1):
            oddList.append(i)
    return oddList

#Lab 7

#Program 7:
'''
Implement a function inBoth() that takes as parameters two lists
and returns True if there is an item that is common to both lists
and False otherwise.  You are NOT ALLOWED to use find,in or count,
you MUST use ==.  The list can contain numbers, strings, or a mix of both.
If the lists contain strings, the capitalization of the string matters
when considering whether items match.

>>> inBoth([3,2,5,4,7], [9,0,1,3])
True
>>> inBoth(['cat','dog'], ['chicken','horse','mouse'])
False
>>> inBoth(['cat','dog',4,'fish'], ['CAT',2,'gerbil'])
False
>>> inBoth(['cat','dog',4,'fish'], ['CAT',2,'gerbil',4])
True
'''
#Run Module for Program to execute (F5)
#Type inBoth(<list>, <list>) - Name of Method in Shell to execute.

def inBoth(list1, list2):

    for i in range(len(list1)):
        for item2 in list2:
            if(list1[i] == item2):
                    return True
    return False

#Program 8
'''
Write a function Collatz() that takes a positive integer x as input
and prints the Collatz sequence starting at  x.
A Collatz sequence is obtained by repeatedly applying the following rule:
if x is even, then the next term is x/2, if x is odd then the next term is 3x+1.
Your function should stop printing when 1 is reached.
(It is not known whether there is a number x whose Collatz sequence does not
end at 1).

>>> Collatz(5)
5
16
8
4
2
1
>>> Collatz(4)
4
2
1
>>> Collatz(3)
3
10
5
16
8
4
2
1
'''

def Collatz(int_num):

    while(int_num > 1):
        print(int_num)

        if(int_num % 2 == 0):
            int_num = int(int_num / 2)
        else:
            int_num = (3 * int_num) + 1
    print(1)

#Program 9
'''
Write a function RetPosPixels() that takes as a parameter a two-dimensional list
of non-negative integer entries (representing the values of pixels of an image),
and returns the number of entries that are positive, that is strictly greater
than 0 (i.e. the number of pixels that are not dark).  Your function should
work on two-dimensional lists of any size.

>>> RetPosPixels([[123,56,255], [34,0,0], [23,123,0], [3,0,0]])
7
>>> RetPosPixels([[0,156,0,0], [34,0,0,0], [23,123,0,34]])
5
'''
#Run Module for Program to execute (F5)
#Type RetPosPixels(<lists>) - Name of Method in Shell to execute.

def RetPosPixels(bigList):
    posPixelsTotal = 0

    for lists in bigList:
        for item in lists:
            if(item > 0):
                posPixelsTotal += 1
                
    return posPixelsTotal
                

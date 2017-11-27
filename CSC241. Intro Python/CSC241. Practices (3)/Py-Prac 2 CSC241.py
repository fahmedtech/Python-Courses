'''
Python CSC241
Practice 2

Contains Collections of Program
Run Module to execute (F5)
Type Method() - Name in Shell to execute.
'''

#Program 1: Return Line that contains Word
'''
>>> myGrep('Py-Prac 1 CSC241 - ex.txt', 'will')
this,,,, punctuation will not b seen !! ## 
this line will come as 'lion' is the key word
this line #10 will showup for the lion !
'''

def myGrep(str_filename, str_word):

    ifile = open(str_filename, 'r')

    for line in ifile:
        if(str_word in line):
            print(line, end='')


    ifile.close()

#Program 2:
'''
>>> openLog('Py-Prac 1 CSC241 - ex.txt', 'r')
<_io.TextIOWrapper name='Py-Prac 1 CSC241 - ex.txt' mode='r' encoding='cp1252'>

IN SHELL
>>> infile = openLog('Py-Prac 1 CSC241 - ex.txt', 'r')
>>> logfile = open('Py-Prac 1 CSC241 - ex.txt')
>>> for log in logfile:
print(log, end = '')
'''
import time

def openLog(str_filename, char_mode):

    currentTime = time.localtime()
    FormatTime = time.strftime('%A %b%d%y %I:%M %p', currentTime)

    ifile = open(str_filename, char_mode)

    str_log = 'File {} opened.\n'

    ofile = open('Py-Prac 2 CSC241 - ex.txt', 'a')
    ofile.write(str_log.format(FormatTime, str_filename))
    ofile.close()

    return ifile

#Program 3:
'''
>>> myBMI(120, 72)
Underweight
>>> myBMI(150, 71)
Normal
>>> myBMI(180, 71)
Overweight
'''

def myBMI(lbs_weight, inch_height):
    bmi = lbs_weight * 703 / inch_height ** 2

    if(bmi < 18.5):
        print("Underweight")
    elif(bmi < 25):
        print("Normal")
    else:
        print("Overweight")

#Program 4: Math.Pow Version
'''
>>> powers(2, 2)
2 4 
>>> powers(2, 3)
2 4 8 
>>> powers(3, 3)
3 9 27
'''

def powers(num, toPower):

    for i in range(1, toPower +1):
        print(num ** i, end = " ")

#Program 5:
'''
>>> isListSorted([1,2,3,5,9,10])
True
>>> isListSorted([1,2,3,5,9,2,10])
False
'''

def isListSorted(list_name):

    for i in range(0, len(list_name) -1):   #not including last item
        if(list_name[i] > list_name[i+1]):
            return False
        
    return True

#Program 6: Arithmetic Sequence
'''
checking difference between successive items is equal to the
difference between the first two numbers.

>>> arithSeq([8,6,2,3])
False
>>> arithSeq([3,5,7,9])
True
>>> arithSeq([2,4,6,8])
True
'''

def arithSeq(int_list):
    if(len(int_list) < 2):
        return True

    diff = int_list[1] - int_list[0]

    for i in range(1, len(int_list) -1):    #not including 1st and last item
        if(int_list[i+1] - int_list[i] != diff):
            return False
        
    return True

#Program 7: Factorial
'''
>>> factorial(3)
2
3
6
'''

def factorial(int_num):
    _value = 1

    for i in range(2, int_num +1):
        print(i)

        _value *= i

    return _value

#Program 8:
'''
>>> acronym('the lion king')
'TLK'
'''

def acronym(str_word):
    retVal = ''
    
    charList = str_word.split()

    for item in charList:
        retVal += item[0].upper()

    return retVal

#Program 9:
'''
>>> divisors(5)
[1, 5]
>>> divisors(15)
[1, 3, 5, 15]
>>> divisors(12)
[1, 2, 3, 4, 6, 12]
'''

def divisors(int_num):
    retList = []

    for i in range(1, int_num +1):
        if(int_num % i == 0):
            retList.append(i)

    return retList

#Program 10: Nested Loops
'''
>>> nested(5)
0 
1 1 
2 2 2 
3 3 3 3 
4 4 4 4 4 
'''

def nested(int_num):

    for i in range(int_num):
        for j in range(i +1):
            print(i, end=' ')
        print()

#Program 11:
'''
>>> ListMulti([2,3], [1,2,3,4,5])
[2, 4, 6, 8, 10, 3, 6, 9, 12, 15]
'''

def ListMulti(list1, list2):
    retList = []

    for item1 in list1:
        for item2 in list2:
            retList.append(item1 * item2)
            
    return retList

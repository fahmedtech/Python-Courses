'''
Python CSC241
Lab 2 - 6/23/2016
'''

#Lab 3

#Program 1:
'''
Define a function Print3Chars which accepts a single argument, a list of 
strings, and that prints to the screen, one per line, the first three characters of each 
string. If the string has fewer than three characters, it prints as many characters as 
the string has. You are allowed to index into a string, i.e. s[2], but you are NOT 
ALLOWED to use slice notation s[1:5] if you know it.
           SUGGESTIONS:
           #retVal = item[0] + item[1] + item[2]
           #print(retVal)

>>> Print3Chars(['hello','goodbye','no','later'])
hel
goo
no
lat
'''
#Run Module for Program to execute (F5)
#Type Print3Chars(<list>) - Name of Method in Shell to execute.

def Print3Chars(str_list):

    for item in str_list:
        if(item != ' '):
            print(item[:3])

def Print3CharsV2(str_list):
    retVal = ""

    for item in str_list:
        if(len(item) < 3):
            print(item)
        else:
            for i in range(3):
                retVal += item[i]
            retVal += '\n'
    print(retVal)

#Program 2:
'''
Implement the function AvgList() that takes no parameters and inputs from the 
user a list of numbers. The function returns the average of the numbers in the 
list. If the list entered by the user is empty, the average returned should be 0.0. 
You may assume that the list provided by the user contains only numbers, either 
floating point or integer or both.

>>> AvgList()
Please input the List of numbers: [3,7,22]
10.666666666666666
Please input the List of numbers: [-12.3,77.2,99]
54.63333333333333
Please input the List of numbers: []
0.0
'''
#Run Module for Program to execute (F5)
#Type AvgList() - Name of Method in Shell to execute.

def AvgList():
    n_List = eval(input("Please input the List of numbers: "))

    if(len(n_List) > 0):
        return (sum(n_List) / len(n_List))
    else:
        return 0.0

#Program 3:
'''
Write a function magnitude that accepts a list of numbers and returns the 
magnitude of the list. The magnitude of the list is the largest absolute value found
among numbers in the list. (Hint: it is the absolute value of either the largest or 
the smallest number in the list. Use the functions abs,max,min.) If the list is 
empty, then the function should return 0.

>>> MagnitudeList([])
0.0
>>> MagnitudeList([-3,-44,11,-22])
44
>>> MagnitudeList([3,4,11,22])
22
'''
#Run Module for Program to execute (F5)
#Type MagnitudeList(<list>) - Name of Method in Shell to execute.

def MagnitudeList(num_List):

    if(len(num_List) == 0):
        return 0.0

    else:
        abs_Max = abs(max(num_List))
        abs_Min = abs(min(num_List))

        if(abs_Max > abs_Min):
               return abs_Max
        else:
            return abs_Min

#Program 4:
'''
Implement a function PrintDivisors which accepts a positive integer n and 
prints all the divisors of that number. A divisor is a number between 1 and n that 
divides the number with no remainder. You will need range and %.

>>> PrintDivisors(12)
1 2 3 4 6 12 
>>> PrintDivisors(17)
1 17 
'''
#Run Module for Program to execute (F5)
#Type PrintDivisors(<integer>) - Name of Method in Shell to execute.

def PrintDivisors(int_num):

    for i in range(1, int_num + 1):
        if(int_num % i == 0):
            print(i , end=' ')

#Lab 4

#Program 5:
'''
Define and implement a function CensoredCopy() that takes two file names and a string as parameters
and copies the contents of the first file into the second where each occurrence of the third parameter
has been replaced with ‘xxxx’.  You are guaranteed that the first file exists,
but the second file may not already exist.  The information below shows how you would
call the function CensoredCopy() and what it would display for example files which
can be found in the zip file with the template for the fourth lab:

>>> CensoredCopy('Py-Lab 2 CSC241 - test1.txt', 'Py-Lab 2 CSC241 - out1.txt', 'test')
>>> open('Py-Lab 2 CSC241 - out1.txt').read()
"This is a xxxx\n\nThis is only a xxxx\n\nWhy must we have xxxxs\n\nI don't know the answer\n"

>>> CensoredCopy('Py-Lab 2 CSC241 - test2.txt', 'Py-Lab 2 CSC241 - out2.txt', 'test')
>>> open('Py-Lab 2 CSC241 - out2.txt').read()
'This is a TesT!\nThis is only a TEST.\nHow about a longer line that is also a question?\nThis lab is going well.\n'
'''
#Run Module for Program to execute (F5)
#Type CensoredCopy(<string>, <string>, <string>) - Name of Method in Shell to execute.

def CensoredCopy(inp_file, out_file, str_word):

    ifile = open(inp_file, 'r')
    lines = ifile.readlines() #list of each lines
    ifile.close()

    ofile = open(out_file, 'w')

    for item in lines:
        if(str_word not in item):
            ofile.write(item)
        else:
            ofile.write(item.replace(str_word, 'xxxx') + '\n')
            
    ofile.close()
    
#Program 6:
'''
Define and implement a function WordCount() that takes a file name as a parameter
and returns the number of words in the file.  Words are non-space characters separated
by spaces in the file.  The information below shows you how you would call the
function WordCount() and what it would display for the example files found
in the zip file with the template for the fourth lab:

>>> WordCount('Py-Lab 2 CSC241 - test1.txt')
19
>>> WordCount('Py-Lab 2 CSC241 - test2.txt')
24
'''
#Run Module for Program to execute (F5)
#Type WordCount(<string>) - Name of Method in Shell to execute.

def WordCount(file_name):

    ifile = open(file_name, 'r')
    content = ifile.read() #whole text as string
    ifile.close()

    words_count = len(content.split())

    return words_count

#Program 7:
'''
Write a function Palindrome() that accepts a string and returns True
if the string is a palindrome, using the same characters forwards and backwards.
This function should NOT be case sensitive and should ignore
white space and the punctuation characters (;.,?!).

>>> Palindrome('doggone')
False
>>> Palindrome("Otto!")
True
>>> Palindrome("Eva, Can I stab bats in a cave?")
True
'''
#Run Module for Program to execute (F5)
#Type Palindrome(<string>) - Name of Method in Shell to execute.

from string import ascii_lowercase

def Palindrome(str_word):

    retVal = ""
    caseWord = str_word.lower()

    for char in caseWord:
        if(char in ascii_lowercase):
            retVal += char

    return retVal == retVal[::-1]

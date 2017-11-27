'''
Python CSC241
Practice 1

Contains Collections of Program
Run Module to execute (F5)
Type Method() - Name in Shell to execute.
'''

#Program 1:
'''
>>> LeapYear(2014)
Nope
>>> LeapYear(2016)
Leap
'''

def LeapYear(int_year):

    if(int_year % 4 == 0):
        print("Leap")
    else:
        print("Nope")

#Program 2:
'''
>>> fishyLogin()
Enter User Name: faizan
Fishy member Logged In!
>>> fishyLogin()
Enter User Name: "faizan"
You are not a Fishy!
'''
        
def fishyLogin():
    members = ['faizan','david','gabriel','ilia','pedro']

    inp_name = input("Enter User Name: ")
    
    if(inp_name in members):
        print("Fishy member Logged In!")
    else:
        print("You are not a Fishy!")

#Program 3:
'''
>>> ItemLen4()
Enter Word List: ['four','hello','three','okay']
four
okay
>>> ItemLen4()
Enter Word List: []
'''

def ItemLen4():
    inp_list = eval(input("Enter Word List: "))

    for item in inp_list:
        if(len(item) == 4):
            print(item)

#Program 5
'''
>>> average(5,6)
5.5
>>> average(3,3)
3.0
'''

def average(int_x, int_y):
    return (int_x + int_y) / 2

#Program 6
'''
>>> circle_perimeter(5.4)
33.929200658769766
'''

import math

def circle_perimeter(int_x):
    return 2 * (math.pi) * int_x

#Program 7
'''
>>> negInList([])
>>> negInList([-2,2,3,4,6,8,-3])
-2 -3 
'''

def negInList(num_list):

    for item in num_list:
        if(item < 0):
            print(item, end=" ")

#Program 8
'''
>>> squareOrCube(2)
Type S for Square or C for Cube: s
4.0
>>> squareOrCube(2)
Type S for Square or C for Cube: c
8.0
'''
import math

def squareOrCube(int_num):

    inp_cmd = input('Type S for Square or C for Cube: ')

    if(inp_cmd.upper() == 'S'):
        return math.pow(int_num, 2)
    else:
        return math.pow(int_num, 3)

#Program 9
'''
>>> printEvens(15)
2 4 6 8 10 12 14 
>>> printEvens(12)
2 4 6 8 10 12
'''

def printEvens(int_num):

    for i in range(2, int_num +1):
        if(i % 2 == 0):
            print(i, end=" ")

#Program 10
'''
>>> studentsList = []
>>> studentsList.append(['demoiness','jim','sophomore', 3.45])
>>> studentsList.append(['pierre','sophie','sophomore', 4.0])
>>> studentsList.append(['columbus','maria','senior', 2.5])

>>> classRoster(studentsList)
Last     First     Class   Average Grade
demoiness jim       sophomore       3.45
pierre    sophie    sophomore       4.00
columbus  maria     senior          2.50
'''

def classRoster(obj_list):
    print('Last     First     Class   Average Grade')

    for item in obj_list:
        print('{:10}{:10}{:10}{:10.2f}'.format(item[0],item[1],
                                               item[2],item[3]))
    
#Program 11: Count Total Number of Words in file.
'''
>>> numWords('Py-Prac 1 CSC241 - ex.txt')
41
'''

def numWords(str_filename):

    ifile = open(str_filename, 'r')
    content = ifile.read()
    ifile.close()

    wordList = content.split()
    return len(wordList)

#Program 12: Count Appearance of Word in File
'''
>>> wordCount('Py-Prac 1 CSC241 - ex.txt', 'will')
'3' will Found in File
>>> wordCount('Py-Prac 1 CSC241 - ex.txt', 'five')
'1' five Found in File
'''

def wordCount(str_filename, str_word):

    ifile = open(str_filename, 'r')
    content = ifile.read()
    ifile.close()

    if(content.count(str_word) == 0):
        print("Word Not Found!")
    else:
        print("'{}' {} Found in File".format(content.count(str_word),
                                             str_word))

#Program 13: Return Words without Punctuations
'''
>>> noPunctuations('Py-Prac 1 CSC241 - ex.txt')
['there', 'are', 'five', 'words', 'totally', 'we', 'we', 'are', 'for',
'problem', '4', '8', 'this', 'punctuation', 'will', 'not', 'b', 'seen',
'for', 'problem', '4', '9', 'this', 'line', 'will', 'come', 'as', "'lion'",
'is', 'the', 'key', 'word', 'this', 'line', '10', 'will', 'showup', 'for',
'the', 'lion']
'''

def noPunctuations(str_filename):

    ifile = open(str_filename, 'r')
    content = ifile.read()
    ifile.close()

    puncTranslate = str.maketrans('!,.:;?#', 7 * ' ')

    content = content.translate(puncTranslate)

    return content.split()

#Program 14: Return Number of Lines from File
'''
>>> lineNum('Py-Prac 1 CSC241 - ex.txt')
11
'''

def lineNum(str_filename):

    ifile = open(str_filename, 'r')
    lineList = ifile.readlines()
    ifile.close()

    return len(lineList)

'''
Python CSC241
Lab 4 - 6/25/2016
'''

#Lab 8

#Program 1:
'''
Write function ReverseDict() that takes as input a dictionary
and returns another (new) dictionary that is the “reverse” of the original,
that is, the pairs are the same but with the keys and values switched.
Remember that dictionaries are not ordered so you don’t expect the reversed
dictionary to have the same order:

>>> phoneDict = {'eric':'123-4567','sue':'999-9999','sally':'3333'}
>>> phoneDict['sue']
'999-9999'
>>> ReverseDict(phoneDict)
{'3333': 'sally', '999-9999': 'sue', '123-4567': 'eric'}
>>> ReverseDict(phoneDict)['3333']
'sally'
'''
#Run Module for Program to execute (F5)
#Type ReverseDict(<dictionary>) - Name of Method in Shell to execute.

def ReverseDict(dict_name):
    retDict = {}

    for item in dict_name:
        key = dict_name[item]
        retDict[key] = item
        
    return retDict

#Program 2:
'''
Write function HasDuplicates() that accepts a list as an argument
and returns True if any element in the list appears more than once,
and False otherwise:

>>> HasDuplicates([1,2,3,5])
False
>>> HasDuplicates([5,1,2,3,5])
True
'''
#Run Module for Program to execute (F5)
#Type HasDuplicates(<list>) - Name of Method in Shell to execute.

def HasDuplicates(list_name):

    if(len(set(list_name)) == len(list_name)):
        return False
    else:
        return True

#Program 3:
'''
Write a function FindMinRow() that takes a two-dimensional list of numbers
as a parameter.  It returns the index of the minimum row in the list.
The minimum row is the row with the smallest sum of elements.  If the list
has multiple rows that achieve the minimum value, the first such row should
be returned.  If the list is empty the function should return -1.

>>> FindMinRow([])
-1
>>> FindMinRow([ [3.99,-12.5,8.61], [0], [-3,-5,-7] ])
2
>>> FindMinRow([ [1,2,3], [-100], [10,-30.5,8] ])
1
>>> FindMinRow([ [10,20], [100,200], [8,7,6,5], [13], [8,9,10] ])
3
'''
#Run Module for Program to execute (F5)
#Type FindMinRow(<list>) - Name of Method in Shell to execute.

def FindMinRow(lists):
    if(len(lists) == 0):
        return -1

    index = 0
    initialSum = sum(lists[0])

    for i in range(1, len(lists)):
        if(sum(lists[i]) < initialSum):

           initialSum = sum(lists[i])
           index = i
           
    return index

#Lab 9

#Program 4:
'''
Write a function Letter2Number() that takes a string representing
a letter grade as a parameter and returns the grade point associated
with that grade.  The grade letter will be one of A, B, C, D, or F
(upper- or lowercase).  It may include a plus or minus after the letter.
An A corresponds to a grade point of 4, a B to 3, a C to 2, a D to 1,
and an F to 0.  A plus increases the base grade point by 0.3
and a minus decreases it by 0.3.  There is no such thing as an A+ or an F-.
If the user provides a string as an argument that doesn't correspond to a
valid grade, the function returns the string 'unknown grade'.
You MUST use a dictionary for this problem.  Any solution that does not
involve a dictionary will not earn full credit.
The following shows the letter2number() function as used on several different
arguments:

>>> Letter2Number('A')
4
>>> Letter2Number('c+')
2.3
>>> Letter2Number('f')
0
>>> Letter2Number('E')
'Unknown Grade'
'''
#Run Module for Program to execute (F5)
#Type Letter2Number(<string>) - Name of Method in Shell to execute.

def Letter2Number(str_grade):

    grades_dict = {'A':4,'A-':3.7,'B':3,'B+':3.3,'B-':2.7,'C':2,'C+':2.3,
                   'C-':1.7,'D+':1.3,'D-':0.7,'D':1,'F':0}
    upcaseGrade = str_grade.upper()

    while True:
        if(upcaseGrade not in grades_dict):
            return 'Unknown Grade'
        else:
            return grades_dict[upcaseGrade]

#Program 5:
'''
Write function InputNames() that takes no input and repeatedly asks the user to
enter the first name of a student in class.   When the user enters the empty
string, the function print the number of students with each name that are in
the class.   For full credit the names are not case sensitive,
i.e. ‘FRANK’ and ‘fRAnk’ are all considered the same as ‘Frank’.
And, the list of students MUST be printed in alphabetical order
(hint: use list()).

>>> InputNames()
Enter the Name: Faizan
Enter the Name: faizan
Enter the Name: FaIzAn
Enter the Name: sheraz
Enter the Name: sHERAZ
Enter the Name: Fraz
Enter the Name: 
There are 3 named Faizan
There are 2 named Sheraz
There are 1 named Fraz
'''
#Run Module for Program to execute (F5)
#Type InputNames() - Name of Method in Shell to execute.

def InputNames():
    _namesList = []
    _setList = []
    temp = True

    while temp:
        inp_name = input("Enter the Name: ").capitalize()

        if(inp_name != ''):
            _namesList.append(inp_name)

        else:
            temp = False    #Terminate Program

    _namesList.sort()
    for item in _namesList:
        _setList.append('There are '+ str(_namesList.count(item))
                        + ' named ' + item)

    output = set(_setList)
    
    for item in output:
        print(item)

# -- This Version uses a Dictionary (BETTER VERSION)
def InputNamesV2():
    _namesDict = {}
    temp = True

    while temp:
        inp_name = input("Enter the Name: ").capitalize()

        if(inp_name != ''):
            if(inp_name not in _namesDict):
                _namesDict[inp_name] = 1
            else:
                _namesDict[inp_name] += 1

        else:
            temp = False

    for keyItem in sorted(_namesDict):
        print('There are', _namesDict[keyItem], 'named', keyItem)

#Program 6:
'''
Two words are anagrams if they are the same after rearranging the letters.
Write a function isAnagram() that accepts two strings and returns True if
they are anagrams and False if not.   You may assume that the given arguments
consist of only lower case letters.

>>> isAnagram('otto', 'toto')
True
>>> isAnagram('to', 'otto')
False
>>> isAnagram('dormitory', 'dirtyroom')
True
'''
#Run Module for Program to execute (F5)
#Type isAnagram(<string>, <string>) - Name of Method in Shell to execute.

def isAnagram(str_word1, str_word2):

    charsList1 = list(str_word1)
    charsList1.sort()
    
    charsList2 = list(str_word2)
    charsList2.sort()

    return charsList1 == charsList2

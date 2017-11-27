'''
Python CSC241
HW 3 - 6/27/2016
'''

#HW 5

#Program 1:
'''
Write a function VowelIndices() that takes a string as a parameter and prints,
one per line, the indices of all the vowels in the string.  A vowel is one of
a, e, i, o, or u.  Capitalization should not matter in reporting the indices,
meaning that upper- and lowercase vowels should have their indices printed.
If there are no vowels in the string, nothing should be printed.

>>> VowelIndices("Hello WORLD")
1
4
7
>>> VowelIndices("Amber Settle")
0
3
7
11
>>> VowelIndices("")
>>> VowelIndices("TestIng, TESTING!")
1
4
10
13
>>> VowelIndices("BCD")
'''
#Run Module for Program to execute (F5)
#Type VowelIndices(<string>) - Name of Method in Shell to execute.

def VowelIndices(str_word):
    _vowels = "aeiou"
    str_word = str_word.lower()

    for i in range(len(str_word)):
        if(str_word[i] in _vowels):
            print(i)

#Program 2:
'''
Write a function printNthItem() that takes a list lst and a positive (>= 0) integer
n as parameters.  It prints every nth item in lst, one per line,
beginning with the first item in the list.  For example, if n is 2,
the function will print every other item in the list, beginning with the first
item.  The function must work regardless of the type of items that are in the
list.  If the parameter n is zero or negative the function should not print
anything.  The function should not modify the list provided as a parameter.

>>> printNthItem([1,2,3,4,5,6], 2)
1
3
5
>>> printNthItem([1,2,3,4,5,6], 3)
1
4
>>> printNthItem([1,2,3,4,5,6], 4)
1
5
>>> printNthItem([], 3)
>>> printNthItem(['dog','cat','ferret','hamster'], 2)
dog
ferret
>>> printNthItem(['dog','cat','ferret','hamster'], 5)
dog
>>> printNthItem(['dog','cat','ferret','hamster'], -5)
'''
#Run Module for Program to execute (F5)
#Type printNthItem(<list>, <integer>) - Name of Method in Shell to execute.

def printNthItem(obj_list, int_num):

    for i in range(0, len(obj_list), int_num):
        print(obj_list[i])

#This Version contains additional ways of writing this Program
def printNthItemV2(obj_list, int_num):

    #Prints the List
    for item in obj_list:
        print(obj_list[::int_num])
        break

    #Another Method
    for i in range(len(obj_list)):
        if(i % int_num == 0):
            print(obj_list[i])
            
#Program 3:
'''
Write a function findSubStrs() that takes a list of strings as a parameter.
It prints every string in the list that is a substring of the one that
precedes it (comes immediately before it in the list), one per line.
If the list is empty or contains only one string, the function doesn't print
anything.  Note that this means that the function will never print the
first item in the list since it has no predecessor in the list.  

>>> findSubStrs(['hope','hop','hopefully','test','testing'])
hop
>>> findSubStrs(['hopefully','hope','hop','testing','test'])
hope
hop
test
>>> findSubStrs(['one','once','only'])
>>> findSubStrs(['one'])
>>> findSubStrs([])
>>> findSubStrs(['blues','blue','blu','b'])
blue
blu
b

Index Comparison Table (findSubStrs(['hope','hop','hopefully','test','testing']))

Index str_list[i]  |  Index str_list[i-1]
=========================================
0   'hope'            -1    'testing'
1   'hop'              0    'hope'
2   'hopefully'        1    'hop'
3   'test'             2    'hopefully'
4   'testing'          3    'test'
'''
#Run Module for Program to execute (F5)
#Type findSubStrs(<list>) - Name of Method in Shell to execute. 

def findSubStrs(str_list):

    if(len(str_list) > 1):
        
        for i in range(len(str_list)):
            if(str_list[i] in str_list[i-1]):
                print(str_list[i])

#Program 4:
'''
Write a function RetStrListOfLen() that takes a list lst of strings and a
non-negative (>= 0) integer n as a parameter and returns a new list
containing all of the strings in lst that have length n.  If n is negative
or lst is empty the function should return an empty list.  The original list
should not be modified.

>>> RetStrListOfLen(['dog','letter','stop','door','cat','bus','floor'], 3)
['dog', 'cat', 'bus']
>>> RetStrListOfLen(['dog','letter','stop','door','cat','bus','floor'], 4)
['stop', 'door']
>>> RetStrListOfLen(['dog','letter','stop','door','cat','bus','floor'], 5)
['floor']
>>> RetStrListOfLen(['dog','letter','stop','door','cat','bus','floor'], 2)
[]
>>> RetStrListOfLen([], 5)
[]
>>> RetStrListOfLen(['one','two','three'], -3)
[]
'''
#Run Module for Program to execute (F5)
#Type RetStrListOfLen(<list>, <integer>) - Name of Method in Shell to execute.

def RetStrListOfLen(str_list, int_num):
    newList = []

    for item in str_list:
        if(len(item) == int_num):
            newList.append(item)

    return newList

#Program 5:
'''
Write a function findDigits() that takes a string as a parameter
and returns a list containing all of the digits that appear in the string.
The digits in the list that is accumulated should be in numeric form rather
than strings.  If the string does not contain any digits or an
empty string is provided as a parameter, the empty list should be returned.
If a digit appears in the string multiple times, it will appear in the list
the same number of times.

>>> findDigits("1 2 3 ... we have begun counting!")
[1, 2, 3]
>>> findDigits("Testing 1. Testing 12. Testing again!")
[1, 1, 2]
>>> findDigits("1 2 3 o'clock, 5 6 7 o'clock, 8 9 10 o'clock")
[1, 2, 3, 5, 6, 7, 8, 9, 1, 0]
>>> findDigits("This is a test without digits.")
[]
>>> findDigits("")
[]
'''
#Run Module for Program to execute (F5)
#Type findDigits(<string>) - Name of Method in Shell to execute.

def findDigits(str_word):
    numList = []

    for char in str_word:
        if(char.isdigit()):
            numList.append(int(char))
            
    return numList

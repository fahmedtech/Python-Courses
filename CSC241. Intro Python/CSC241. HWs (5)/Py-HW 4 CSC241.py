'''
Python CSC241
HW 4 - 6/27/2016
'''

#HW 6

#Program 1:
'''
A polynomial of degree n with coefficients a0, a1, a2, a3, ..., an is
the function: p(x) = a0 + a1x + a2x**2 + a3x**3 + ... + anx**n.
This function can be evaluated at different values of x.
For examples, if p(x) = 1 + 2x + x**2, then p(2) = 1 + 2 * 2 + 2**2 = 9.
If p(x) = 1 + x**2 + x**4 then p(2) = 21 and p(3) = 91.
Write a function poly() that takes as a parameter a list of coefficients a0, a1,
a2, a3, ... an of a polynomial p(x) and a value x.
It returns p(x) which is the value of the polynomial when evaluated at x.

**ALL LOOPS COMPARISON
http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops


----- ENUMERATE ------
for index, item in enumerate(items):
    print(index, item)
    

**Unidiomatic control flow

What you are asking for is the Pythonic equivalent of the following,
which is the algorithm most programmers of lower-level languages would use:

----- REGULAR FOR LOOP -----
index = 0            # Python's indexing starts at zero
for item in items:   # Python's for loops are a "for each" loop 
    print(index, item)
    index += 1

>>> count = 0
>>> for item in [1,2,3,4,5]:
	print(count, end=" ")
	count += 1
0  1  2  3  4

>>> for item in [1,2,3,4,5]:
	print(item)
	count += 1	
1  2  3  4  5
    
Or in languages that do not have a for-each loop:

----- WHILE LOOP -----
index = 0
while index < len(items):
    print(index, items[index])
    index += 1
    
or sometimes more commonly (but unidiomatically) found in Python:

for index in range(len(items)):
    print(index, items[index])

Use the Enumerate Function:
Python's enumerate function reduces the visual clutter by hiding the accounting
for the indexes, and encapsulating the iterable into another iterable
(an enumerate object) that yields a two-item tuple of the index and
the item that the original iterable would provide. That looks like this:

for index, item in enumerate(items, start=0):   # default is zero
    print(index, item)

=============
>>> polynomialDegree([1,2,1], 2)
9
>>> polynomialDegree([1,0,1,0,1], 2)
21
>>> polynomialDegree([1,0,1,0,1], 3)
91
'''
#Run Module for Program to execute (F5)
#Type polynomialDegree(<list>, <integer>) - Name of Method in Shell to execute.

def polynomialDegree(int_list, int_val):
    _totalList = []
    _finalSum = 0
    _indexPower = 0
    
    for _itemCoe in int_list:
        _totalList.append( (int_val ** _indexPower) * _itemCoe)
        _indexPower += 1

    for item in _totalList:
        _finalSum += item

    return _finalSum

#This Version uses Enumerate - Better!

def polynomialDegreeV2(int_list, int_val):
    _totalList = []

    for _indexPower, _itemCoe in enumerate(int_list):
        _totalList.append( (int_val ** _indexPower) * _itemCoe)

    return sum(_totalList)

#Program 2:
'''
The mathematical constant π (pi) is an irrational number with value
approximately 3.1415928...  The precise value of π is equal to the following
infinite sum: π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
We can get a good approximation of π by computing the sum of the first few
terms.  Write a function approxPi() that takes as a parameter a floating point
value error and approximates the constant π within error by computing the
above sum, term by term, until the absolute value of the difference between
the current sum and the previous sum (with one fewer terms) is no greater
than error.  Once the function finds that the difference is less than error,
it should return the new sum.  Please note that this function should not use
any functions or constants from the math module.
You are supposed to use the described algorithm to approximate π, not
use the built-in value in Python.

>>> approxPi(0.5)
3.3396825396825403
>>> approxPi(0.05)
3.1659792728432157
>>> approxPi(0.005)
3.144086415298761
>>> approxPi(0.0000005)
3.1415929035895926

'running Detailed Program on Error values > 0.05 can take very long!'
Use CTRL + Z to Terminate.
>>> approxPiDetailed(0.5)
4 -3
_newVal:  2.666666666666667
_prevVal:  2.666666666666667 

2.666666666666667 5
_newVal:  3.466666666666667
_prevVal:  3.466666666666667 

3.466666666666667 -7
_newVal:  2.8952380952380956
_prevVal:  2.8952380952380956 

2.8952380952380956 9
_newVal:  3.3396825396825403
FINAL _prevVal:  3.3396825396825403 

3.3396825396825403
'''
#Run Module for Program to execute (F5)
#Type approxPi(<float>) - Name of Method in Shell to execute.

def approxPi(float_error):
    _initialVal = 1
    _prevVal = 4

    while True:
        denominator = (2 * _initialVal) + 1

        if(_initialVal % 2 == 1):
            denominator =  -denominator

        newVal = _prevVal + 4.0/denominator

        if(abs(newVal - _prevVal) < float_error):
            _prevVal = newVal
            break

        #else condition
        _prevVal = newVal
        _initialVal += 1
        
    return _prevVal

#This version explains in detail how this Algorithm works!
def approxPiDetailed(float_error):
    _initialVal = 1
    _prevVal = 4

    while True:
        denominator = (2 * _initialVal) + 1

        if(_initialVal % 2 == 1):
            denominator =  -denominator  #changing every other sign (+/-)

        print(_prevVal, denominator)
        newVal = _prevVal + 4.0/denominator
        print("_newVal: " , newVal) 

        if(abs(newVal - _prevVal) < float_error):
            _prevVal = newVal
            print("FINAL _prevVal: " , _prevVal, "\n")
            break

        #else condition
        _prevVal = newVal
        print("_prevVal: ", _prevVal, "\n")
        _initialVal += 1
        
    return _prevVal


#Program 3:
'''
At the end of textbooks there is usually an index that lists the pages
where certain words appear. In this problem you will create an index for a text,
but instead of using page numbers you will use the line numbers. To do this,
implement a function indexLine() that takes as a parameter the name of a text
file (as a string) and a list of words. For every word in the list,
your function will print the lines in the text file where the word occurs and
print the corresponding line numbers (where the numbering starts at 1).
The numbers can either be printed individually or in a list as shown below.
Punctuation (including commas, periods, exclamation marks, question marks,
colons, semicolons, apostrophes, and quotes) and capitalization should be
ignored when considering words in the file. You should open and close the text
file only once. Finally, you need to make sure that if the file the user
specifies cannot be opened that the function recovers gracefully.
It should indicate to the user that the file could not be found and immediately
return rather than raising an exception.

**REFRESHER - counts number of occurences in file

    ifile = open(str_filename, 'r')
    content = ifile.read()
    ifile.close()

    wordList = content.split()

    for item in str_list:
        if(item in wordList):
            print(item, " ", wordList.count(item))

>>> indexLineV2('Py-HW 4 CSC241 - raven.txt', ['raven','mortal','dying','ghost','ghastly','evil','demon'])
raven      [44, 53, 55, 64, 78, 97, 104, 111, 118, 120]
ghost      [9]
ghastly    [82]
demon      [122]
evil       [99, 106]
dying      [9]
mortal     [30]
>>> indexLineV2('none.txt', ['does','not','matter'])
File 'none.txt' is not in current Directory!

>>> indexLine('Py-HW 4 CSC241 - raven.txt', ['raven','mortal','dying','ghost','ghastly','evil','demon'])
{'mortal': [30], 'dying': [9], 'demon': [122], 'raven': [44, 53, 55, 64, 78, 97, 104, 111, 118, 120], 'ghastly': [82], 'evil': [99, 106], 'ghost': [9]}
>>> indexLine('none.txt', ['does','not','matter'])
File 'none.txt' is not in current Directory!
'''
#Run Module for Program to execute (F5)
#Type indexLine(<string>, <list>) - Name of Method in Shell to execute.

import string

def indexLine(str_filename, str_list):

    try:
        wordDict = {}

        for item in str_list:
            wordDict[item] = list()

        with open(str_filename, 'r') as ifile:
             for lineNum, line in enumerate(ifile, 1):

                 transPunct = line.maketrans(string.punctuation,
                                            len(string.punctuation) * " ")
                 line = line.translate(transPunct)

                 for item in str_list:
                     if(item in line.split()):
                         wordDict[item].append(lineNum)
        return wordDict

    except FileNotFoundError:
        print("File '{}' is not in current Directory!".format(str_filename))


#This version meets the Criteria of the Question much better!
import string

def indexLineV2(str_filename, str_list):

    try:
        lineNum = 0
        wordsDict = {}

        #add items from str_list to dict[items] as 'key' and  List as 'value'
        for item in str_list:
            wordsDict[item] = list()

        with open(str_filename, 'r') as ifile:

            for lineItems in ifile:
                lineNum += 1

                #removing Punctuations
                transPunct = lineItems.maketrans(string.punctuation,
                                                 len(string.punctuation) * " ")
                lineItems = lineItems.translate(transPunct)
                
                for item in str_list:                    
                    if(item in lineItems.split()):
                        wordsDict[item].append(lineNum)

            for keys in wordsDict:
                print("{:10} {}".format(keys, wordsDict[keys]))


    except FileNotFoundError:
        print("File '{}' is not in current Directory!".format(str_filename))
               
#Program 4:
'''
In any group of people there are many pairs of friends.  Assume that two people
who share a friend are friends themselves.  (Yes, this is an unrealistic
assumption in real life, but let's make it nevertheless).  In other words,
if people A and B are friends and B is friends with C, then A and C must also be
friends.  Using this rule we can partition any group of people into friendship
circles as long as we know something about the friendships in the group.

Write a function Networks() that takes two parameters.  The first parameter
is the number of people in the group and the second parameter is a list of tuple
objects that define friends.  Assume that people are identified by numbers 0
through n-1.  For example, tuple (0, 2) says that person 0 is friends
with person 2.  The function should print the partition of people into
friendship circles.

>>> Networks(5, [(0,1),(1,2),(3,4)])
Social Network 0 is {0, 1, 2}
Social Network 1 is {3, 4}
>>> Networks(10, [(0,1),(1,2),(3,4),(5,4),(7,8)])
Social Network 0 is {0, 1, 2}
Social Network 1 is {3, 4, 5}
Social Network 2 is {9}
Social Network 3 is {6}
Social Network 4 is {8, 7}
>>> Networks(6, [(0,1),(2,3),(3,5),(5,1)])
Social Network 0 is {0, 1, 2, 3, 5}
Social Network 1 is {4}
'''
#Run Module for Program to execute (F5)
#Type Networks(<integer>, <list> <tuple>) - Name of Method in Shell to execute.

def Networks(int_num, list_tup):
    groupList = []

    for i in range(int_num):
        groupList.append( {i} )

    for tupItems in list_tup:
        union = groupList[tupItems[0]] | groupList[tupItems[1]]

        for tup in union:
            groupList[tup] = union

    sets = set()
    for items in groupList:
        sets.add(tuple(items))

    for i, item in enumerate(sets):
        print("Social Network", i, "is", set(item))


def NetworksDetailed(int_num, list_tup):
    groupList = []

    for i in range(int_num):
        groupList.append( {i} ) #appending dictionary values
    print("groupList:", groupList, "\n")

    #tupItems tells the index as well
    for tupItems in list_tup:
        #assigning tuple values to dictionary - set values 'indices' ([0],[1])
        print("List Index:", groupList[tupItems[0]], groupList[tupItems[1]])
        union = groupList[tupItems[0]] | groupList[tupItems[1]] 
        print("tupItems:", tupItems, end=" ")
        print("union af:", union)

        #adding to dictionary list
        for tup in union:
            groupList[tup] = union
            print("tup", tup, end=" ")
            print("groupList[tup]", groupList[tup])
        print("groupList", groupList, "\n")

        sets = set()
        for items in groupList:
            sets.add(tuple(items))
            print("groupList to tuples:", tuple(items))
        print("sets", sets, "\n")

        index = 0
        for item in sets:
            print("Social Netork", index, "is", item)
            index += 1

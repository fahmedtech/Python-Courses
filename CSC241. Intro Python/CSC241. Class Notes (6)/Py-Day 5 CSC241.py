'''
Python CSC241
Day 5 - 6/20/2016
'''

'''
**Concept: Importing Random

random.randrange(start, stop) - int
random.uniform(start, stop) - float
random.choice(sequence) - returns random item
random.sample(sequence, k) - returns k items
random.shuffle(sequence) - shuffles

>>> random.random()        # Random float x, 0.0 <= x < 1.0
0.37444887175646646
>>> random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
1.1800146073117523
>>> random.randint(1, 10)  # Integer from 1 to 10, endpoints included
7
>>> random.randrange(0, 101, 2)  # Even integer from 0 to 100
26
>>> random.choice('abcdefghij')  # Choose a random element
'c'

>>> items = [1, 2, 3, 4, 5, 6, 7]
>>> random.shuffle(items)
>>> items
[7, 3, 2, 5, 6, 4, 1]

>>> random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
[4, 1, 5]

SHELL PRACTICE (RANDOM)
>>> import random
>>> random.randrange(1,6)
3
>>> random.randrange(1,7)
6
>>> [random.randrange(1,7) for i in range (100)]
[3, 3, 6, 6, 3, 5, 5, 4, 5, 6, 3, 1, 6, 6, 2, 2, 2, 5, 5, 6, 1, 5, 3, 6, 6, 3, 3, 2, 1, 4, 1, 6, 2, 4, 1, 3, 5, 4, 5, 1, 2, 2, 1, 4, 1, 5, 5, 1, 5, 6, 2, 6, 5, 2, 4, 1, 4, 5, 4, 6, 6, 1, 5, 4, 1, 1, 6, 4, 1, 3, 1, 3, 4, 5, 6, 6, 3, 4, 5, 3, 1, 1, 4, 2, 2, 6, 6, 4, 1, 4, 4, 2, 4, 5, 6, 3, 2, 4, 4, 1]
>>> random.uniform(0,1)
0.6177630359885248
>>> random.uniform(0,1)
0.9761416066932117

>>> height = random.uniform(100,200)
>>> height
151.9925745297827

>>> fruit = ['orange','pear','apple']
>>> random.choice(fruit)
'apple'

>>> random.sample(fruit,2)
['pear', 'orange']
>>> random.sample(fruit,2)
['pear', 'apple']


>>> random.randrange(0,2)
1
>>> random.randrange('h','t') - doesnt work
>>> random.choice(['h','t'])
't'

>>> fruit
['orange', 'pear', 'apple']
>>> random.shuffle(fruit)
>>> fruit
['pear', 'orange', 'apple']


**Concept Importing Math

>>> import math
>>> math.pi
3.141592653589793
>>> 'pi' in vars(math)
True
>>> vars(math)['pi']
3.141592653589793

>>> from math import pi
>>> pi
3.141592653589793
>>> from math import *
>>> cos
<built-in function cos>
>>> e
2.718281828459045
'''

#Program 1: Random 2 Dice Rolls | If 'Double' Roll Again | Return total Rolls
#Run Module for Program to execute (F5)
#Type DiceTotal() - Name of Method in Shell to execute.

'''
>>> DiceTotalV2()
5 5
2 4
16
>>> DiceTotal()
4 4
2 5
15
'''

import random

def DiceTotal():
    _total = 0

    dice1 = random.randrange(1,7) #7 not included
    dice2 = random.randrange(1,7)
    print(dice1, dice2)

    _total += dice1 + dice2

    #keep rolling if double
    while(dice1 == dice2):
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        print(dice1, dice2)

        _total += dice1 + dice2
        
    return _total

#Version 2. DiceTotalV2() - Using Infinite Loop Method.

import random

def DiceTotalV2():
    _total = 0

    #keep rolling if double
    while True:
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        print(dice1, dice2)

        _total += dice1 + dice2

        if(dice1 != dice2):
            return _total

'''
**Concept: Namespace
a dictionary where variables and their values are stored as pairs
when you define a variable, an entry in the current namspace is made
- variable:value

x = 99 # add 'x':99 to namespace

when you access a variable, its value is looked up in the namespace:
print (x)

lookup is in the following order
1) local function namespace
2) global/module namespace
3) builtins namespace
'''

x = 99

def f():
    x = 22
    print(vars())
    print(x)

def g():
    print(vars())
    print(x)

#f() - 'x' will be 22 found locally
#g() - 'x' will be 99 found in module

'''
***OVERVIEW***

method:   l.append('apple')
function: l=len(mylist)

numbers
    bool < int < float
    operators: +,-,*,/,**,%,//
    comparisons: <,>,<=,>=,==,!=
    functions: abs()

string
    containment: in, not in
    +, *(int)
    [][start:stop:step]
    methods - split,upper,lower,capitalize,format,count
    functions: len()
    immutable

list - indexed sequence of items
    in, not in
    [],[::]
    indexed by range
    mutable (editable)
    methods: append,pop,sort,count,remove,find,reverse
    functions: len,min,max,range

dictionary
    {key: val1, key1,val2...}
    d[key] = val
    indexed by keys
    not ordered
    mutable, keys are immutable
    in, not in - works in keys

tuple
    (,,,,)
    like a list but immutable(cant edit,only construct)
    doesnt have append,sort method

set
    {,,,,}
    like a list but,
    no duplicates, not ordered,indexed
    &,|
    ex. {1,3,4} & {1,2}

files
    open,read,write,readlines,close

math
    import math
    math.pi
    math.e
    math.sqrt, math.cos

random
    import random
    randrange, uniform
    choice,shuffle,sample

control structures/logic
    if,elif,else
    for, while
    loop mods: return,break,pass,continue

loop patterns
    iterate over sequence
        for i in lst
        for i in range()
        for char in string
        for key in dict
    indexed
        use when you need location
        for i in range(len(lst))
    nested loop
        2d list
        for row in table:
            for item in row:
    accumulator
        init,accumulate,return/
    for loops that execute at least one time
    loop and a half
    infinite loop

functions
    return vs print
    local vs global variables

'''

#Program 2: Create a Stack of Cups given an Integer
#Run Module for Program to execute (F5)
#Type GetStackHeight(<integer>) - Name of Method in Shell to execute.

'''
>>> GetStackHeight(5)
X
XX
2
>>> GetStackHeight(6)
X
XX
XXX
3
'''

def GetStackHeight(int_cups):
    _length = 1 #for next row to build
    _height = 0

    while(int_cups >= _length):
        print(_length * 'X')

        int_cups -= _length
        _height += 1
        _length += 1
        
    return _height

#Program 3: Return Set of Index Matching items from two Lists 
#Run Module for Program to execute (F5)
#Type RetFindMatch(<list>, <list>) - Name of Method in Shell to execute.

'''
>>> RetIndexFindMatch([1,2,3,4],[2,4,6,8])
(1, 0)
>>> RetIndexFindMatch(['david','gabriel','faizan'],['pedro','faizan','ilia'])
(2, 1)
'''

def RetIndexFindMatch(list1, list2):

    for i in range(len(list1)):
        for j in range(len(list2)):

            if(list1[i] == list2[j]):
                return (i, j)
    return -1,-1

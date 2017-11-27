'''
Python CSC242
Day 6 - 7/5/2016

RECURSIONS!
'''

#Program 1: Fibonacci (non-Recursive vs Recursive) - Returns nth Fib #
#Run Module for Program to execute (F5)
#Type Fib(<integer>) or RFib(<integer>) - Name of Method in Shell to execute.
'''
>>> Fib(6)
13
>>> Fib(10)
89
>>> RFib(6)
13
>>> RFib(10)
89
'''

def Fib(int_num):

    _prev = 1
    _curr = 1
    _index = 1

    while(_index < int_num):
        _prev, _curr = _curr, _prev + _curr
        _index += 1

    return _curr

def RFib(int_num):

    if(int_num < 2):
        return 1

    return RFib(int_num -1) + RFib(int_num -2)

#Program 2: Timing - Shows which Fibonacci Program is faster. 
#Run Module for Program to execute (F5)
#Type Timing(<Function>, <integer>) - Name of Method in Shell to execute.
'''
>>> Fib(30)
1346269
>>> RFib(30)
1346269

>>> Timing(Fib, 30)
0.0
>>> Timing(RFib, 30)
0.5460009574890137
'''

import time

def Timing(func, int_num):
    'runs func on input returned by buildInput()'

    _funcInp = buildInput(int_num)

    _start = time.time()
    func(_funcInp)
    _end = time.time()

    return _end - _start

def buildInput(int_num):
    'returns input for Fibonacci programs'
    return int_num

def TimingAnalysis(func, _start, _stop, _incr, _runs):
    '''prints average run-times of function func on inputs of
       size start, start+inc, start+2*inc, ..., up to stop'''

    for i in range(_start, _stop, _incr):
        totalTime = 0.0

        for j in range(_runs):
            totalTime += Timing(func, i)

        retVal = 'Run-time of {}({}) is {:.7f} seconds.'
        print(retVal.format(func.__name__, i, totalTime/_runs))

'''
Further Implementations for buildInput()

import random

# buildInput for comparing Linear and Binary search
def buildInput(n):
    'returns a random sample of n numbers in range [0, 2n)'
    lst = random.sample(range(2*n), n)
    lst.sort()
    return lst

# buildInput for Practice Problems 10.7, 10.8
def buildInput(n):
    'returns a list of n random integers in range [0, n**2)'
    res = []
    for i in range(n):
        res.append(random.choice(range(n**2)))
    return res
'''

#Program 3: Searches an object target - given the range of start & end index in list
#Run Module for Program to execute - (F5)
#Type RSearch(<list>, <object>, <int>, <int>) - Name of Method in Shell to execute.
'''
>>> lst = [2,3,4,9,18,39,40,55,69,71,75,77,85,90,95,96,97]
>>> RSearch(lst, 75, 0, 16)
10

>>> lst = ['faizan','pedro','gabriel','ilia','david']
>>> RSearch(lst, 'faizan', 0, 4)
0
'''

def RSearch(list_name, obj_target, ind_i, ind_j):
    '''attempts to find target in sorted sublist list_name[ind_i:ind_j];
       index of target is returned if found, -1 otherwise'''

    #base case: empty List 
    if(ind_i == ind_j):
        return -1

    _median = (ind_i + ind_j) // 2

    if(list_name[_median] == obj_target):
        return _median

    #Search Left of _median
    if(obj_target < list_name[_median]):
        return RSearch(list_name, obj_target, ind_i, _median)

    #Search Right of _median
    else:
        return RSearch(list_name, obj_target, _median +1, ind_j)

#Implementation
#Method: Choose an item in list at random and run RSearch()
'''
>>> lst = ['faizan','pedro','gabriel','ilia','david']
>>> binary(lst)
2
'''
import random

def binary(list_name):

    _target = random.choice(list_name)
    return RSearch(list_name, _target, 0, len(list_name))
    

    
#Program 4: Choose item in list at random and run index() - Not Recursive
#Run Module for Program to execute (F5).
#Type linear(<list>) - Name of Method in Shell to execute.
'''
>>> lst = ['faizan','pedro','gabriel','ilia','david']
>>> linear(lst)
3
'''

def linear(lst):
    _target = random.choice(lst)
    return lst.index(_target)

#Program 5: Checking Duplicates in List Programs (Non-Recursive)
#Run Module for Program to execute (F5)
#Type Dup(<list>) - Name of Method in Shell to execute.
'''
>>> lst = ['faizan','pedro','gabriel','ilia','david']
>>> lst2 = ['faizan','pedro','faizan','faizan','david']

>>> Dup(lst)
False
>>> Dup(lst2)
True

>>> DupV2(lst)
False
>>> DupV2(lst2)
True

#different implementation - read Code!
>>> DupV3(lst)
True
>>> DupV3(lst2)
False

>>> DupV4(lst)
False
>>> DupV4(lst2)
True
'''

def Dup(obj_list):

    for item in obj_list:
        if(obj_list.count(item) > 1):
            return True
    return False


def DupV2(obj_list):

    obj_list.sort()

    for index in range(1, len(obj_list)):
        if(obj_list[index] == obj_list[index -1]):
            return True
    return False

def DupV3(obj_list):
    _set = set()

    for item in obj_list:
        if(item in _set):
            return False
        else:
            _set.add(item)
    return True

def DupV4(obj_list):
    return len(obj_list) != len(set(obj_list))

'''
#testing TimeAnalysis() for Dup Programs - Please Uncomment Code to work
def buildInput(int_num):
    res = []

    for i in range(int_num):
        res.append(random.choice(range(int_num ** 2)))
    return res


>>> TimingAnalysis(Dup, 0, 2500, 500, 1)
Run-time of Dup(0) is 0.0000000 seconds.
Run-time of Dup(500) is 0.0156000 seconds.
Run-time of Dup(1000) is 0.0000000 seconds.
Run-time of Dup(1500) is 0.0311999 seconds.
Run-time of Dup(2000) is 0.0936003 seconds.

>>> TimingAnalysis(DupV2, 0, 2500, 500, 1)
Run-time of DupV2(0) is 0.0000000 seconds.
Run-time of DupV2(500) is 0.0000000 seconds.
Run-time of DupV2(1000) is 0.0000000 seconds.
Run-time of DupV2(1500) is 0.0000000 seconds.
Run-time of DupV2(2000) is 0.0156000 seconds.

>>> TimingAnalysis(DupV3, 0, 2500, 500, 1)
Run-time of DupV3(0) is 0.0000000 seconds.
Run-time of DupV3(500) is 0.0000000 seconds.
Run-time of DupV3(1000) is 0.0000000 seconds.
Run-time of DupV3(1500) is 0.0000000 seconds.
Run-time of DupV3(2000) is 0.0000000 seconds.

>>> TimingAnalysis(DupV4, 0, 2500, 500, 1)
Run-time of DupV4(0) is 0.0000000 seconds.
Run-time of DupV4(500) is 0.0000000 seconds.
Run-time of DupV4(1000) is 0.0000000 seconds.
Run-time of DupV4(1500) is 0.0000000 seconds.
Run-time of DupV4(2000) is 0.0000000 seconds.
'''

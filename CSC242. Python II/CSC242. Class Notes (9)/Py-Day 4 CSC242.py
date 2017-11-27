'''
Python CSC242
Day 4 - 7/4/2016


If you want to use tkinter without calling root=Tk() in Shell
inside __init__ method type self.pack()
and then type
<Name of Class>().mainloop()
'''

#CONCEPT: Understanding Recursions

#Program 1: Countdown (Recursive)
#Run Module for Program to execute (F5)
#Type Countdown(<integer>) - Name of Method in Shell to execute.
'''
def infiniteCountdown(int_num):
    print(int_num, end=' ')
    infiniteCountdown(int_num -1)

>>> Countdown(10)
10 9 8 7 6 5 4 3 2 1 0 Done!
'''

def Countdown(int_num):

    if(int_num >= 0):
        print(int_num, end=' ')
        Countdown(int_num -1)

    else:
        print("Done!")

#Program 2: Print each integer in its own line (Recursive)
#Run Module for Program to execute (F5)
#Type PrintInteger(<integer>) - Name of Method in Shell to execute.
'''
>>> PrintInteger(504)
5
0
4
>>> PrintInteger(52)
5
2
>>> PrintInteger(5)
5
'''

def PrintInteger(int_num):

    if(int_num < 10):
        print(int_num)

    else:
        PrintInteger(int_num // 10)
        print(int_num % 10)

        # last digit, can be movable before 'PrintInteger(n//10)'
        # in order to reverse the print

#Program 3: Print X number of Cheers (Recursive)
#Run Module for Program to execute (F5)
#Type Cheers(<integer>) - Name of Method in Shell to execute.
'''
>>> Cheers(5)
Hip! Hip! Hip! Hip! Hip! Hooray!
'''

def Cheers(int_num):

    if(int_num == 0):
        print('Hooray!')

    else:
        print('Hip!', end=' ')
        Cheers(int_num -1)

#Program 4: Factorial (Recursive)
#Run Module for Program to execute (F5)
#Type Factorial(<integer>) - Name of Method in Shell to execute.
'''
>>> Factorial(5)
5!
4!
3!
2!
1!
120
>>> Factorial(3)
3!
2!
1!
6
'''

def Factorial(int_num):

    if(int_num == 0):
        return 1

    else:
        print(str(int_num) + '!')
        return int_num * Factorial(int_num -1)

#Program 5: List Sum (Recursive)
#Run Module for Program to execute (F5)
#Type ListSum(<list>) - Name of Method in Shell to execute.
'''
>>> ListSum([])
0
>>> ListSum([1,2,3])
6
>>> ListSum([25,30])
55
'''

def ListSum(num_list):

    if(len(num_list) == 0):
        return 0

    lastItem = num_list.pop()
    return lastItem + ListSum(num_list)

#Program 6: Fibonacci (non-Recursive vs Recursive)
#Run Module for Program to execute (F5)
#Type Fib(<integer>) or RFib(<integer>) - Name of Method in Shell to execute.
'''
This Program Gives you the Fibonacci Number at Nth Sequence.

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
    _prev, _curr = 1, 1

    for i in range(2, int_num +1):
        _curr, _prev = _prev + _curr, _curr
        #print(_curr, _prev)

    return _curr

#Recursive Version

def RFib(int_num):

    if(int_num in [0,1]):
        return 1
    
    return RFib(int_num -1) + RFib(int_num -2)        
    
    

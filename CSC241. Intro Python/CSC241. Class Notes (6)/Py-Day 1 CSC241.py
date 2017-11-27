'''
Python CSC241
Day 1 - 6/15/2016 
-----

Keyboard Shortcuts
 - ALT-P, ALT-N (Previous/Next command)
 - CTRL-N (Create new file)


**Some Examples of Math Operations on Python Command Line
>>> 3+4
7
>>> 3.0*4.5
13.5
>>> 7/2
3.5
>>> 7//2
3
>>> 7%2
1
>>> 132//60
2
>>> 132%60
12
>>> 2**4
16

**Using Variables or Legal Identifiers on Command Line

>>> f = 212
>>> c = (f-32)*5/9
>>> c
100.0
>>> f=32
>>> c = (f-32)*5/9
>>> c
0.0

>>> vars() - shows all defined Variable names

**Boolean operators are math operations(!) produce either True or False

    >,<,>=,<=
    ==
    !=
    and,or
    not
    !
    
>>> 2<3
True
>>> 4<4
False
>>> 2=3
SyntaxError: can't assign to literal
>>> 2==3
False
>>> 2!=3
True
>>> 3*.3==.9
False

>>> 2<3 and 4.1<3
False
>>> 2<3 or 4.1<3
True
>>> not( 7<6)
True

**A String is a sequence of characters delimited using either and
can be delimited in 3 ways

>>> 'apple'
'apple'
>>> "pear"
'pear'
>>> '''  ''' <-- Multiline Comment

You can concat and remove characters from String
>>> 'apple'+'pear'
'applepear'
>>> 'a'*4
'aaaa'

**You can also print in Command Line
print('hello','bye',3,2.1,True)
'''

#Program 1: Double the inputted Number
#Run Module for Program to execute (F5)

'''
functions used
    print()
        prints zero or more items
        spaces between items
        newline after all items
    input()
        ptints messages, gets user response
        almost always assign to variables
        returns a strl
    eval()
        converts a str to number, if possible
'''

input_num = eval(input("Enter a Number for Double: "))
print("Double of ", input_num, " is ", 2 * input_num)

if(input_num > 3):
    print(input_num, "is greater than 3.")
else:
    print("the value is lesser than 3.") 

''' checking if EVEN or ODD '''
print('input_num % 2', input_num % 2)
print('input_num%2==1', input_num % 2 == 1)

''' Condition: If Odd - Specify '''
if(input_num%2==1):
    print(input_num, 'is ODD')

'''
**Messing around with Command Line
>>> one = 1
>>> two = 2.0
>>> three = 'three'
>>> four = True
>>> type (5)
<class 'int'>
>>> type (four)
<class 'bool'>
>>> type (three)
<class 'str'>
>>> type ('one')
<class 'str'>
>>> three + " & " + three
'three & three'
>>> one+two
3.0
>>> #the answer is a float
>>> print(1,2,5.4)
1 2 5.4
>>> print (one, two)
1 2.0
>>> print(str(one)+str(two))
12.0
>>> f = f

**Separator
>>> print(1,2,3, sep=' ')
1 2 3

**Methods can be assigned - Can Break Program Functionalities
>>> fgs = 'squad'
>>> type(fgs)
<class 'str'>
>>> print = fgs
>>> print
'squad'
>>> print (1,2,3)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print (1,2,3)
TypeError: 'str' object is not callable
'''

#Program 2: Checking if Number Divisble by 2 & 3
#Run Module for Program to execute (F5)
'''
Enter an integer to check if Divisible by 2 & 3: <6> <Program Execute>
6 is Divisible by 2
6 is Divisible by 3
'''
print()
input_num = eval(input('Enter an integer to check if Divisible by 2 & 3: '))

if(input_num % 2 == 0):
    print(input_num, 'is Divisible by 2')
if(input_num % 3 == 0):
    print(input_num, 'is Divisible by 3')

'''
**CONCEPT String - Str
    is 0-based
    indexed
    sequence of characters
    immutable

**Checking the Length of String & Index
>>> s = "here is a string"
>>> len(s) 
16
>>> s[15]
'g'

**Last char is substracted one than its length
>>> s[-1]
'g'
>>> s[-16]
'h'

**Slicing the String Str[Start Index Number : Stop Index Number]
  Value of Stop is not Included
>>> s[0:4]
'here'

>>> s= 'H' + s[1:]
>>> s
'Here is a string'

**CONCEPT List
    [a,b,c]
    0-based
    indexed
    sequence of items (of any type) - Container
    mutable

**Command Line exercises with List
>>> fruit = ['apple','pear', 'orange','kivi']
>>> len(fruit)
4
>>> fruit[0]
'apple'
>>> fruit[-1]
'kivi'
>>> fruit[0:2]
['apple', 'pear']
>>> "lemon" in fruit
False
>>> "pear" in fruit
True
>>> fruit [2] = "lemon"
>>> fruit
['apple', 'pear', 'lemon', 'kivi']
>>> fruit[1][3]
'o'

List has Methods to use {Press Tab after . to check callable methods}
>>> fruit.append('durian')
>>> fruit.sort()
>>> fruit.reverse()
>>> fruit.pop()
>>> last_item=fruit.pop()

**CONCEPT: Range
    similar to a list of integers (concept-wise)

    Has Three Forms:
    range(stop) - start at 0 index, step is 1
    range(start,stop) - step is 1
    range(start,stop,step)

List used for Illustrations Purpose Only
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(4,20,3)[2]
10

Command Line Practice
>>> for num in range (11):
	print(num)
0
1
2
3
4
5
6
7
8
9
10

>>> for i in range (0,23,2):
	print(i)
0
2
4
6
8
10
12
14
16
18
20
22

**CONCEPT: ITERATION

Slow to print each Character alone
i.e.
>>> s = "here"
>>> char = s[0]
>>> print (char)

Faster Method Use Iteration!
for char in s:
    print(char)

>>> fruit = ['apple','pear', 'orange','kivi']
for item in fruit:
    print(item)

Adding Conditions to check if Length > 4    
>>> for item in fruit:
	if len(item) > 4:
		print(item)
'''

#Program 3: Print All Vowels from the String and Count
#Run Module for Program to execute (F5)
print()

count = 0
input_str = input("Enter a String to Check & Count Vowels: ")

for char in input_str:
    if(char in 'aeiouAEIOU'):
        count += 1
        print(char, end=" ") #printing Dynamically in one line
print('\nVowels Count:', count)


#Program 4: Countdown from the Input Integer
#Run Module for Program to execute (F5)
print()

input_num = eval(input("Enter an Integer for Countdown: "))

for i in range(input_num,-1,-1):
    print(i)
print("Happy New Year!")
    

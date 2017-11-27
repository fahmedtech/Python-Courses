'''
Python CSC241
Lab 1 - 6/23/2016
------

Practice Shell.

*1a. The sum of the first 5 negative (< 0) integers
    >>> -5 + -4 + -3 + -2 + -1
    -15

1b. The average age of three people with ages 21, 45, and 14 respectively
    >>> 21 + 45 + 14
    80
    >>> 80/3
    26.666666666666668

1c. 5 to the 4th power
    >>> 5**4
    625
    
1d. The number of times 20 goes into 387 (evenly -- it should produce an integer result)
    >>>20%387
    20

1e. The remainder when 387 is divided by 20
    >>> 387//20
    19

*2a. Assign 3.5 to the variable a, 12 to the variable b, and -3 to the variable c
    >>> a=3.5
    >>> a
    3.5
    >>> b=12
    >>> b
    12
    >>> c=-3
    >>> c
    -3

2b. Assign to variable d the product of variables a, b, and c
    >>> d = a * b * c
    >>> d
    -126.0

*3a. Assign 0.0 to the variable c, the number of degrees Fahrenheit.
    >>> c=0.0
    >>> c
    0.0
    
3b. Write an expression using c that calculates the equivalent temperature in degrees Fahrenheit
    (may need to look this up on the internet) and assigns the result to a variable f.
    Your expression should use the variable c, not the value 0.0.
    >> f = (9/5) * c+32
    >>> f
    32.0

3c. Repeat steps a. and b. for Celsius temperatures 100 and -40, respectively
    >>> c=100
    >>> f = (9/5) * c+32
    >>> f
    212.0

    >>> c=-40
    >>> f = (9/5) * c+32
    >>> f
    -40.0

*4a. Assign to variables first, second, and third the strings 'one', 'two', and 'three'
    >>> first = 'one'
    >>> second = 'two'
    >>> third = 'three'

4b. Assign to the variable formatted str the concatenation of the string variables first, second, and third ...
    That means that in this particular case the value of formatted str should be 'one, two, and three ...'
    where the commas, "and", spaces, and three dots will have to be concatenated with the values in the variables.
    For full credit your expression must use the variables first, second, and third instead of hard-coding the values of the variables.
    >>> first = 'one'
    >>> second = 'two'
    >>> third = 'three'
    >>> first + ', ' + second + ', and ' + third
    'one, two, and three'

*5. Assign c1 = '1' and c2 = '2' in the Python shell.
    Then write string expressions involving only c1 and c2 and the string operators + and * that evaluate to the following.
    Make your string expressions as succinct as you can.

a.  '12'
>>> str (c1) + str (c2)
b.  '2211'
>>> str (c2) * 2 + str (c1) * 2
c.  '111222'
>>> str (c1) * 3 + str (c2) * 3
d.  '12211221122112211221'
>>> (c1 +c2 +c2 +c1) * 5
'''

#Lab 2
'''
1.  Recall that we were able to output a sequence of integers by executing code like this:
    >>> for i in range(10):
           print( i, end=" ")
        0 1 2 3 4 5 6 7 8 9
    Write statements that output the following sequences:

    a.	32 33 34 35 36 37 38 39 40 41 42 43 44
    >>> for i in range(32, 45):
            print(i, end=" ")
    32 33 34 35 36 37 38 39 40 41 42 43 44 
    
    b.	10 12 14 16 18 20 22 24 26 28 30 32 34
    >>> for i in range(10,35,2):
	print(i, end=" ")
    10 12 14 16 18 20 22 24 26 28 30 32 34 
    
    c.	20 18 16 14 12
    >>> for i in range(20, 11, -2):
            print(i, end=" ")
    20 18 16 14 12 
'''

#Program 2: Initials: write a program that inputs the first and last names of the user and then outputs their initials.
#Run Module for Program to execute (F5)
'''
Please enter your first name: Jane
Please enter your last name: Jones
Jane Jones, your initials are JJ
'''

inp_fname = input("Please enter your First Name: ")
inp_lname = input("Please enter your Last Name: ")

print(inp_fname, inp_lname, 'your initials are', inp_fname[0] + inp_lname[0])

#Program 3: Pig Latin Translator.  Write a (simple) Pig Latin Translator.
#           Let the user a word (all in lower case). If the word begins with a vowel, translate it to the same word with “ay” at the end.
#           If it begins with a consonant, move the consonant to the end and at “ay”.
#Run Module for Program to execute (F5)
'''
Please Enter a lower case Word: eric
ericay
Please Enter a lower case Word: sally
allysay

EASY VERSION
vowels = ('a','e','i','o','u','A','E','I','O','U')
name = input('Please enter a lower case English word:')

if name[0] in vowels:
        print (name + 'ay')
else:
    print(name[1:] + name[0] + 'ay')
'''

print()
print('Pig Latin Translator')
vowelList = ['a','e','i','o','u','A','E','I','O','U']

inp_str = input("Please Enter a lower case Word: ")

for char in inp_str:
    if(char[0] in vowelList):
        print(inp_str + 'ay')
    else:
        print(inp_str[1:] + inp_str[0] + 'ay')
    break

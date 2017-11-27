'''
Python CSC241
HW 1 - 6/26/2016
'''

#HW 1

#Shell Practice Exercises
'''
Start by assigning s1 = '&' and s2 = '#' in the Python shell.
Then write string expressions involving only s1 and s2 and the string
operators + and * that evaluate to the following.  Make your string
expressions as succinct as you can.

a.	'&&#'
>>> (s1 * 2 + s2)
'&&#'
b.	'##&'
>>> (s2 * 2 +s1)
'##&'
c.	'&&#&&#'
>>> (s1 * 2 + s2 + s1 * 2 + s2)
'&&#&&#'
d.	'&&&&&&&&&&'
>>> (s1 *10)
'&&&&&&&&&&'
e.	'&&##&&##&&##'
>>> (s1 * 2 + s2 * 2 +s1 * 2 +s2 * 2 + s1 * 2 + s2 * 2)
'&&##&&##&&##'
f.	'&&&&&#####&&&&&#####&&&&&#####'
>>> (s1 * 5 + s2 * 5)*3
'&&&&&#####&&&&&#####&&&&&#####'
'''

#Program 1: Input Price and Quantity
#Run Module for Program to execute (F5)
'''
Enter a Price > 0: 3.3
Enter the Quantity: 5
Total Price is: $16.5

Enter a Price > 0: -2
Enter the Quantity: 3
Error! Both Values Must be Greater than 0

Enter a Price > 0: 2
Enter the Quantity: -3
Error! Both Values Must be Greater than 0
'''

inp_price = float(eval(input("Enter a Price > 0: ")))
inp_quantity = int(eval(input("Enter the Quantity: ")))

if(inp_price <= 0 or inp_quantity <= 0):
    print("Error! Both Values Must be Greater than 0")
else:
    print("Total Price is: ${}".format(round(inp_price * inp_quantity, 2)))

#Program 2: Comparison of Input Value to 0
#Run Module for Program to execute (F5)
'''
Please Enter a Number: -2
-2.0 is LESS than 0

Please Enter a Number: 0.0
0.0 is EQUAL to 0

Please Enter a Number: 2.3
2.3 is GREATER than 0
'''

print()

inp_num = float(eval(input(("Please Enter a Number: "))))

if(inp_num > 0):
    print(inp_num, "is GREATER than 0")
elif(inp_num == 0):
    print(inp_num, "is EQUAL to 0")
else:
    print(inp_num, "is LESS than 0")

#HW 2

#Program 3:
'''
Implement a function Ret3Chars() that takes a string as a parameter and returns
empty string should be returned. The information below shows how you would call
the function Ret3Chars() and what it would display for several sample
parameters:

>>> Ret3Chars('hello')
'hel'
>>> Ret3Chars('BYE')
'BYE'
>>> Ret3Chars('an')
''
'''
#Run Module for Program to execute (F5)
#Type Ret3Chars(<string>) - Name of Method in Shell to execute.

def Ret3Chars(str_word):
    if(len(str_word) >= 3):
        return str_word[:3]
    else:
        return ''

#Program 4:
'''
Implement a function RetXChars() that takes a string and an integer as
parameters and returns the first n characters of the string s.
If the string has length less than n, then an empty string should be returned.
The information below shows how you would call the function returnN()
and what it would display for a few different parameters:

>>> RetXChars('hello', 2)
'he'
>>> RetXChars('hello', 5)
'hello'
>>> RetXChars('BYE', 1)
'B'
>>> RetXChars('BYE', 10)
''
'''
#Run Module for Program to execute (F5)
#Type RetXChars(<string>, <integer>) - Name of Method in Shell to execute.

def RetXChars(str_word, int_num):
    if(len(str_word) >= int_num):
        return str_word[:int_num]
    else:
        return ''

#Program 5:
'''
Implement the function Print1stChars() that takes a list of strings as a
parameter and prints to the screen the first character of each string, one per line.
If the list provided as a parameter is empty, the function prints a message
to that effect.  If any of the strings are empty, they are skipped in the
display. The information below shows how you would call the function
Print1stChars() and what it would display for a couple of parameters:

>>> Print1stChars(['hello','bye','TEST','Done'])
h
b
T
D
>>> Print1stChars(['first','','third'])
f
t
>>> Print1stChars([])
The List Provided in Parameter was Empty!
'''
#Run Module for Program to execute (F5)
#Type Print1stChars(<string>) - Name of Method in Shell to execute.

def Print1stChars(str_list):
    if(len(str_list) == 0):
        print("The List Provided in Parameter was Empty!")

    for item in str_list:
        if(len(item) == 0):
            pass
        else:
            print(item[0])

#Program 6:
'''
Implement a function PrintGreater() that takes as parameters a list of numbers
and a numeric value. It prints the numbers in the list that are greater than
the value, all on one line with a space between them. If an empty list is
provided as the first parameter, the function doesn't print anything.
The information below shows how you would call the function PrintGreater()
and what it would display for some example parameters:

>>> PrintGreater([1,-3,12,-5,0], 0)
1 12 
>>> PrintGreater([2,4,6,8,10], 5)
6 8 10 
>>> PrintGreater([-1,-2,-3], -1)
>>> PrintGreater([], 10)
>>> PrintGreater([1,2,3,4,5,6,7,8], 0)
1 2 3 4 5 6 7 8 
'''
#Run Module for Program to execute (F5)
#Type PrintGreater(<list>, <integer>) - Name of Method in Shell to execute.

def PrintGreater(list_num, int_value):

    for i in list_num:
        if(i > 0 and i > int_value):
            print(i, end=' ')

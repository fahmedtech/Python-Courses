'''
Python CSC241
HW 2 - 6/27/2016
'''

#HW 3

#Program 1:
'''
Implement a function CoinProb() that takes no parameters and enters
a positive integer n from the user.  The value n represents the number of
tosses of a fair coin.  The function checks that n is positive (> 0).
If it is not, it prints an error message.  If n is positive the function
prints the probability of getting n heads in a row when tossing a coin n times.
That probability can be computed as 1 divided by 2 to the power n.
You may assume that the user will enter an integer when prompted.

>>> CoinProb()
Enter the Number of Coin Tosses: 1
Probability of 'Heads' in a row for 1 tosses is:  0.5
>>> CoinProb()
Enter the Number of Coin Tosses: 2
Probability of 'Heads' in a row for 2 tosses is:  0.25
>>> CoinProb()
Enter the Number of Coin Tosses: 10
Probability of 'Heads' in a row for 10 tosses is:  0.0009765625
>>> CoinProb()
Enter the Number of Coin Tosses: 0
Invalid Number of Coin Tosses!
>>> CoinProb()
Enter the Number of Coin Tosses: -3
Invalid Number of Coin Tosses!
'''
#Run Module for Program to execute (F5)
#Type CoinProb() - Name of Method in Shell to execute.

def CoinProb():
    inp_num = int(eval(input("Enter the Number of Coin Tosses: ")))

    if(inp_num > 0):
        print("Probability of 'Heads' in a row for", inp_num, "tosses is: ",
              1/2 ** inp_num)
    else:
        print("Invalid Number of Coin Tosses!")

#Program 2:
'''
Implement a function PrintMultiples() that takes two positive integers n and m
as parameters, and prints, all on one line, all first m multiples of n.
You may assume that n and m will be positive (> 0).

>>> PrintMultiples(10, 2)
10 20 
>>> PrintMultiples(10, 10)
10 20 30 40 50 60 70 80 90 100 
>>> PrintMultiples(2, 12)
2 4 6 8 10 12 14 16 18 20 22 24 
>>> PrintMultiples(3, 5)
3 6 9 12 15 
>>> PrintMultiples(7, 5)
7 14 21 28 35 
'''
#Run Module for Program to execute (F5)
#Type PrintMultiples(<integer>, <integer>) - Name of Method in Shell to execute.

def PrintMultiples(int_num1, int_num2):
    
    if(int_num1 > 0 and int_num2 > 0):
        for i in range(int_num1, (int_num2 + 1) * int_num1, int_num1):
            print(i, end=' ')

#Program 3:
'''
Write a function customSpam() that takes as parameters a string containing
a first name followed by a space followed by a last name, a string representing
a dollar amount spelled out in words, and string representing an e-mail
address and prints a customized spam solicitation to the person using their
name, the dollar amount, and the e-mail address.  The name should use a
capitalized letter for the first and last name regardless of the capitalization
of the string entered and the dollar amount should be in all caps with spaces
between each letter.

>>> customSpam('Joon elam', 'five thousand', 'greatdeals@gmail.com')
Dear Joon Elam,
We would like to let you know about a great opportunity.
You can make FIVE THOUSAND dollars in just a few short weeks!
This is a Limited-Time Offer.
Please Contact us at greatdeals@gmail.com for more information.

>>> customSpam('djengo settle', 'ten thousand', 'hiremenow@hotmail.com')
Dear Djengo Settle,
We would like to let you know about a great opportunity.
You can make TEN THOUSAND dollars in just a few short weeks!
This is a Limited-Time Offer.
Please Contact us at hiremenow@hotmail.com for more information.

>>> customSpam('COOKIE settle', 'two thousand', 'amazingoffer@aol.com')
Dear Cookie Settle,
We would like to let you know about a great opportunity.
You can make TWO THOUSAND dollars in just a few short weeks!
This is a Limited-Time Offer.
Please Contact us at amazingoffer@aol.com for more information.
'''
#Run Module for Program to execute (F5)
#Type customSpam(<string>, <string>, <string>) - Name of Method in Shell to execute.

def customSpam(str_name, str_amount, str_email):
    capNameList = str_name.split()

    str_name = ''
    for item in capNameList:
        str_name += item.capitalize() + " "

    newAmount = ''
    for char in str_amount:
        newAmount += char.upper() + " " 
    
    
    retVal = '''Dear {},
We would like to let you know about a great opportunity.
You can make {} dollars in just a few short weeks!
This is a Limited-Time Offer.
Please Contact us at {} for more information.'''.format(
    str_name.strip(), newAmount.strip(), str_email)

    print(retVal)

#Program 4:
'''
Implement a function ion2e() that takes a string as a parameter.
If the string ends with 'ion' it prints the initial part of the string
(before the 'ion') followed by an 'e' with no extra spaces.
If the string does not end with 'ion', including the circumstance in
which the string contains 'ion' as a substring, it prints the original string.

>>> ion2e("congratulation")
congratulate
>>> ion2e("marathon")
marathon
>>> ion2e("accordionist")
accordionist
>>> ion2e("hyperrational")
hyperrational
>>> ion2e("irradiation")
irradiate
'''
#Run Module for Program to execute (F5)
#Type ion2e(<string>) - Name of Method in Shell to execute.

def ion2e(str_word):
    last3chars = str_word[-3:]

    if(last3chars == "ion"):
        print(str_word[:-3] + 'e')
    else:
        print(str_word)

# This Version use Methods for comparison - BETTER

def ion2eV2(str_word):

    if(str_word.strip().endswith("ion") == True):
        print(str_word.replace("ion", 'e'))
    else:
        print(str_word)

#Program 5:
'''
Implement a function WordOfLength() that takes a string s and an integer n as
parameters, and returns the number of words in the string s that have length n.
Words in the string are non-space characters separated by at least one space.
You may assume that the string has at least one non-space character in it and
that the "sentence" does not have punctuation.

>>> WordOfLength("This is a test", 4)
2
>>> WordOfLength("This is a test", 2)
1
>>> WordOfLength("This is a test", 3)
0
>>> WordOfLength("Zero and the infinite were at the very center", 4)
3
>>> WordOfLength("Zero and the infinite were at the very center", -3)
0
>>> WordOfLength("Zero and the infinite were at the very center", 3)
3
'''
#Run Module for Program to execute (F5)
#Type WordOfLength(<string>, <integer>) - Name of Method in Shell to execute.

def WordOfLength(str_word, int_num):
    _count = 0
    _wordsList = str_word.split()

    for i in range(len(_wordsList)):
        if(len(_wordsList[i]) == int_num):
           _count += 1

    return _count
    
#HW 4

#Program 6:
'''
Write a function partition() that takes a list of strings and a character
as parameters.  It prints the strings in the list that begin with a letter
at or after the character (according to dictionary order), one per line.
The capitalization of the character and the first letter of the string
should not make a difference in whether the string is printed.  Empty strings
should be skipped.  You may assume that the character given as the second
parameter is an upper- or lowercase letter.

>>> partition(['djengo','joon','AMBER','Susy','Cookie'], 'b')
djengo
joon
Susy
Cookie
>>> partition(['Bob','Mary','Zee',''], 'W')
Zee
>>> partition([], 'a')
>>> partition(['Chad','Sigrid','Angel'], 'c')
Chad
Sigrid
'''
#Run Module for Program to execute (F5)
#Type partition(<list>, <string>) - Name of Method in Shell to execute.

def partition(str_list, str_char):

    for item in str_list:
        if(item.strip() != ''):
            if(item[0].upper() >= str_char.upper()):
                print(item)
        
#Program 7:
'''
Write a function points() that takes as parameters four numbers x1, y1, x2, and
y2 that are coordinates of two points (x1, y1) and (x2, y2) in the plane.
Your function should compute:
a.	The slope of the line going through the points,
        unless the line is vertical
b.	The distance between the two points
The function should print the computed slope and distance in the following way:
if the line is vertical, the value of the slope should be the string 'infinity'.
Otherwise the slope and distance will be printed as computed normally.
If you don’t know how to compute the slope and distance find a reference,
for example Wikipedia. Make sure to convert the slope and distance values
to strings before printing them to avoid extra spaces.  

>>> points(0, 0, 1, 1)
Slope is 1.0 and Distance is 1.4142135623730951
>>> points(0, 0, 0, 1)
Slope is 'Infinity' and Distance is 1.0
>>> points(3, 4, 2, 10)
Slope is -6.0 and Distance is 6.082762530298219
'''
#Run Module for Program to execute (F5)
#Type points(<int>, <int>, <int>, <int>) - Name of Method in Shell to execute.

from math import pow

def points(x1, y1, x2, y2):
    '''Prints Slope and Distance'''
    xs = x2-x1
    ys = y2-y1

    try:
        slopeF = float((ys) / (xs))
        distF = float(pow(pow(xs,2) + pow(ys,2), .5))
        print("Slope is", slopeF, "and Distance is", distF)
        
    except ZeroDivisionError:
            print("Slope is 'Infinity' and Distance is", float(pow(pow(xs,2) + pow(ys,2), .5)))

#Program 8:
'''
Write a function CountVowels() that takes a string representing a file name
as a parameter and returns the number of vowels (both upper- and lowercase)
that appear in the file.  For the purpose of this question a vowel is one of
a, e, i, o, or u.

>>> CountVowels('Py-HW 2 CSC241 - empty.txt')
0
>>> CountVowels('Py-HW 2 CSC241 - vowels.txt')
21
>>> CountVowels('Py-HW 2 CSC241 - poppins.txt')
418
'''
#Run Module for Program to execute (F5)
#Type CountVowels(<string>) - Name of Method in Shell to execute.

def CountVowels(str_filename):
    _count = 0
    _vowels = "aeiouAEIOU"

    ifile = open(str_filename, 'r')
    content = ifile.read() #whole file as string
    ifile.close()

    wordsList = content.split()

    for item in wordsList:
        for i in range(len(item)):
            if(item[i] in _vowels):
                _count += 1

    return _count  

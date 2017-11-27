'''
Python CSC241
Day 2 - 6/16/2016
-----

Command Line Practice
list = ['apple', 2, 3.0, True]
for item in list:
    print(item)

r = range(2,12,3)
for i in r:
    print(i)
'''

#Program 1: Check Voting Age
#Run Module for Program to execute (F5)
#Type VotingAge() - Name of Method in Shell to execute.

def VotingAge():
    input_age = eval(input("Enter your Age: "))
    if(input_age >= 18):
        print("You are Old enough to Vote.")
    else:
        print("Wait", 18 - input_age, "years.") 

#Program 2: Define own Maximum Function
#Run Module for Program to execute (F5)
#Type Max(<integer>, <integer>) - Name of Method in Shell to execute.

def Max(param_num1, param_num2):
    print("Parameter Numbers:", param_num1, param_num2)

    if(param_num1 > param_num2):
        return(param_num1)
    else:
        return(param_num2)

#Program 3: Return the Index of Middle Character of a String
#Run Module for Program to execute (F5)
#Type MiddleChar(<string>) - Name of Method in Shell to execute.

def MiddleChar(str_word):
    if(len(str_word) % 2 == 1):
       mid_char = int(len(str_word)/2) + 1
    else:
        mid_char = int(len(str_word)/2)
    print("Index of Middle Character:", mid_char)

#Program 4: Print items in List that begin with Vowel's Characters
#Run Module for Program to execute (F5)
#Type FirstCharVowel(<List>) - Name of Method in Shell to execute.
#Initialize List: fruit = ['apple','pear','orange','guava']

def FirstCharVowel(list_container):
    for item in list_container:
        if item[0] in "aeiouAEIOU":
            print(item)

'''
**Concept String
Slicing Strings
    string[index]
    string[start:stop] - not including the Stop
    string[start:stop:step]
    string[::-1] - reverse the whole string
    string[-3:] - return the last three characters

***String Methods:
string.upper()
string.lower()
string.capitalize()
string.split()

>>> x = 'lowercase'
>>> x.upper()
'LOWERCASE'
>>> x = 'lowercase uppercase'
>>> x.split()
['lowercase', 'uppercase']

Practice:
x = 'lowercase uppercase'
words = x.split()
for word in words:
    print(word.capitalize())

***String Methods:
string.find()
string.count()
string.format()

Practice:
x = 'lowercase uppercase'
>>> x.find('l')
0
>>> x.find('o')
1
>>> x.count('e')
4

Multiple Assignments
>>> f,g,s = 'fishy','goon','squad'

>>> h,m,s = 3,47,12
>>> "{}:{}:{}" .format(h,m,s)

>>> print("Dear {},\nYou are so {}{}".format("Friend","smart","!"))

Misc Practice:
>>> print( '$' , amt, sep='')
$25.65

>>> for i in range(5):
	print(i,end=',')	
0,1,2,3,4,
'''

#Program 5: Monogram - Upcase Initial Char of Each separated word in String
#Run Module for Program to execute (F5)
#Type Monogram(<string>) - Name of Method in Shell to execute.
#i.e. Monogram("faizan ahmed")

def Monogram(str_word):
    str_list = str_word.split() 

    for item in str_list:
        print(item[0].upper(), end='')
        print()

#Program 6: Input F Temperature to check Status
#Run Module for Program to execute (F5)
#Type TempStatus(<integer>) - Name of Method in Shell to execute.

def TempStatus(temp_num):
    if(temp_num >= 80):
        return "Hot"
    elif(temp_num >= 60):
        return "Warm"
    elif(temp_num >= 40):
        return "Cool"
    else:
        return "Cold"


'''
**Concept: ITERATION

Loop Patterns:

for char in string:
    print(char)

for item in list:
    print(item)

for i in range(n):
    print(i)

for print in file:
    print(line)

**Concept: ACCUMULATOR PATTERN
Three steps:
    1. before loop - initialize running value
    2. in loop - accumulate running value
    3. after loop - print/return running value
'''

#Program 7: Add all the Numbers in a given List 
#Run Module for Program to execute (F5)
#Type AddListNumbers(<List>) - Name of Method in Shell to execute.

'''
>>> AddListNumbers([5,10,15])
30
>>> AddListNumbers({5,10,15})
30
'''

def AddListNumbers(list_nums):
    _total = 0

    for item in list_nums:
        _total += item  #_total = _total + item
    return _total

#Program 8: Retrieve all Odd Numbers from a List to a List 
#Run Module for Program to execute (F5)
#Type GetOddsList(<List>) - Name of Method in Shell to execute.

'''
>>> GetOddsList([5,2,3])
[5, 3]
>>> x = [1,2,3,4,5,6,7,8,9]
>>> GetOddsList(x)
[1, 3, 5, 7, 9]
'''

def GetOddsList(list_nums):

    _oddsList = []

    for item in list_nums:
        if(item % 2 == 1):
            _oddsList.append(item)
            #print(item, _oddsList)
    return _oddsList

'''
Problem:
Add all Numbers from 1, 2 ... 1000 in Shell

>>> total = 0
>>> for i in range(0,1001):   #1001 is not included!
	total += i	
>>> total
500500

Other ways to Solve:
>>> sum(range(1,1001))
500500
'''

#Program 9: Get Factorial of an Integer (n * n-1)
#Run Module for Program to execute (F5)
#Type Factorial(<integer>) - Name of Method in Shell to execute.

def Factorial(param_num):
    _totalFactorial = 1

    for i in range(1, param_num + 1): #+1 because param_num was not included!
        _totalFactorial *= i
    return _totalFactorial

#Program 10: Replace Mutliple things from a given String
#Run Module for Program to execute (F5)
#Type MultiReplace(<List>, <string>, <string>) - Name of Method in Shell to execute.

'''
>>> x = "Sentence, with; punctuation.?"
>>> MultiReplace([',','.',';'], "", x)
'Sentence with punctuation?'
'''

def MultiReplace(replace_list, new_string, param_str):

    for item in replace_list:
        param_str = param_str.replace(item, new_string)
    return param_str

#Program 11: Input Three Grade Items to Compute
#Run Module for Program to execute (F5)
#Type LetterGrade(<float>, <float>, <float>) - Name of Method in Shell to execute.

def LetterGrade(hw_scores, midterm_score, final_score):
    _score = .3 * hw_scores + .3 * midterm_score + .4 * final_score
    print(_score)

    if(_score >= 90):
        return 'A'
    elif(_score >= 80):
        return 'B'
    elif(_score >= 70):
        return 'C'
    elif(_score >= 60):
        return 'D'
    else:
        return 'F'

#Program 12: Two Programs that Prints & Returns Words that ends with Char 'S'
#Run Module for Program to execute (F5)
#Type PrintPluralWords(<string>) - Name of Method in Shell to execute.
#Type ReturnPluralWords(<string>) - Name of Method in Shell to execute.

'''
>>> s = "here is a sentence with some words and lines and more words"
>>> PrintPluralWords(s)
is
words
lines
words
>>> ReturnPluralWords(s)
['is', 'words', 'lines', 'words']
'''

def PrintPluralWords(str_sentence):
    _wordList = str_sentence.split()

    for item in _wordList:
        if item[-1] in "sS":
            print(item)

def ReturnPluralWords(str_sentence):
    _pluralList = []
    
    _wordList = str_sentence.split()
    
    for item in _wordList:
        if(item[-1] in "sS"):
            _pluralList.append(item)
    return _pluralList


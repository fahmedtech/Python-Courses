'''
Python CSC241
Day 4 - 6/19/2016
'''

'''
**Concept: Handling Exceptions

>>> a=5
>>> b=0
>>> a/b
ZeroDivisionError
>>> if b==0:
	slope = 'Infinity'
else:
	slope = a/b

**Using try & except to solve this problem.
>>> slope
'Infinity'
>>> try:
	slope=a/b
except:
	slope = 'infinity'

**Another Case of using a try & except
>>> filename='abc.txt'
>>> try:
	open(filename)
except:
	print('couldnt open the file')

**Case: Multiple tries & exceptions.
>>> try:
	1/0
	open('abc.txt')
except ZeroDivisionError:
	print ('error, div by 0')
except:
	print (' file not found')

	
error, div by 0
'''


'''
**Concept: While Loop Iteration
like an if continues to execute the indented block until the condition is false
then continues with non- indented block

while <cond>:
    indented block
non-indented block

loop modifiers (these apply to for loops as well)
return - stops function (and loops)
break - stops the loop
continue - stops current iteration

'''

#Progam 1: Pig Latin (If 1st letter consonant move to end & add 'ay' to all.)
#Run Module for Program to execute (F5)
#Type PigLatin(<string>) - Name of Method in Shell to execute.

'''
>>> PigLatin("owl")
'owlay'
>>> PigLatin("goose")
'oosegay'
'''

def PigLatin(str_word):
    while str_word[0] not in "aeiouAEIOU":
        str_word = str_word[1:] + str_word[0]
    str_word += "ay"

    return str_word

#Progam 2: Add all the Inputted Numbers from the User and return value
#Run Module for Program to execute (F5)
#Type SumUserNums(<integer>) - Name of Method in Shell to execute.

'''
The Program will end (if input value is empty string)
& return the sum of the numbers. We are not using eval
because it gives an error when empty. != means not equals'
Press Enter Key 2x after you are done with entering numbers
to complete accumulation

>>> SumUserNums()
Enter Number for Sum: 5
Enter Number for Sum: 5
Enter Number for Sum: 
10
'''

def SumUserNums():
    _total = 0

    input_num = input("Enter Number for Sum: ")
    while(input_num != ""):
        _total += eval(input_num)
        input_num = input("Enter Number for Sum: ")
    return _total
        
#Same Program as Above but using Infinite Loop Pattern and "break"

'''
>>> SumUserNums2()
Enter Number for Sum: 4
Enter Number for Sum: 4
Enter Number for Sum: 2
Enter Number for Sum: 
10
'''

def SumUserNums2():
    _total = 0

    while True:
        input_num = input("Enter Number for Sum: ")

        if(input_num == ""):
            break
        _total += eval(input_num) #indented else statement
    return _total


#Progam 3: Return Array of All Prime Factors of a given Integer
#Run Module for Program to execute (F5)
#Type PrimeFactors(<integer>) - Name of Method in Shell to execute.

'''
>>> PrimeFactors(12)
[2, 2, 3]
>>> PrimeFactors(11)
[11]
>>> PrimeFactors(70)
[2, 5, 7]
'''

def PrimeFactors(int_num):
    factorsList = []

    while(int_num > 1):
        for divide in range(2, int_num + 1):
            if(int_num % divide == 0): #if divisible
                factorsList.append(divide)

                int_num = int_num // divide #integer division
                break
    return factorsList

#Same Program as Above but using the Nested Loop Method
#while divide is a factor, divide number by divide, add divide to loop

'''
>>> PrimeFactors2(12)
[2, 2, 3]
>>> PrimeFactors2(11)
[11]
>>> PrimeFactors2(70)
[2, 5, 7]
'''

def PrimeFactors2(int_num):
    factorsList = []
    divide = 2

    while(int_num > 1):
        
        while(int_num % divide == 0):
            factorsList.append(divide)

            int_num //= divide
        divide += 1
    return factorsList

'''
**Concept: Dictionary

dict(ionary)
- {} is empty dictionary
- container for key:value pairs
- like a list, but indexed by keys (almost anything)
- not ordered
- dictionareies are mutable
- keys must be IMMUTABLE

dictionary operators:
- in, not in - work on keys
- dict[key] - gives corresponding value

dictionary methods:
- .items() - returns pairs
- .keys() - returns keys
- .values() - returns value
- .pop(key) - removes key:value, returns value
- .update(dictionary) - "updates" with given dictionary

*PRACTICE IN SHELL
>>> phonenums = {'eric':123, 'sue':'364-4564', 'frank':'999-9999'}
>>> phonenums['sue']
'364-4564'
>>> phonenums['sally']='7879' - it gets added to list
>>> phonenums
{'sally': '7879', 'eric': 123, 'frank': '999-9999', 'sue': '364-4564'}
>>> 'sally' in phonenums
True
>>> for name in phonenums:
	print(name,phonenums[name]) 'name' is key

sally 7879
eric 123
frank 999-9999
sue 364-4564
>>> phonenums.values()
dict_values(['7879', 123, '999-9999', '364-4564'])

# change phone number
>>> phonenums['eric']='888-8-888'
>>> phonenums
{'sally': '7879', 'eric': '888-8-888', 'frank': '999-9999', 'sue': '364-4564'}

# capitalize key sue
>>> phonenums.pop('sue')
'364-4564'
>>> phonenums['Sue']='364-4564'
>>> phonenums
{'sally': '7879', 'eric': '888-8-888', 'frank': '999-9999', 'Sue': '364-4564'}


>>> pns = {'frank':'new','joe':'joe'}
>>> phonenums.update(pns)
>>> phonenums
{'sally': '7879', 'eric': '888-8-888', 'frank': 'new', 'Sue': '364-4564', 'joe': 'joe'}


TUPLE
>>> phonenums[ ('Bush','George')] = 'unlisted'
>>> phonenums
{('Bush', 'George'): 'unlisted', 'sally': '7879',
'eric': '888-8-888', 'frank': 'new', 'Sue': '364-4564', 'joe': 'joe'}
>>> phonenums[('bush','george')]
'unlisted'

TUPLE is like a list but immutable, usable as keys in dict
>>> x = 1,2,3,'apple'
>>> type(x)
<class 'tuple'>
>>> x
(1, 2, 3, 'apple')


**Concept Dictionary in Vars() Method Practice
>>> vars()
{'__doc__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__builtins__': <module 'builtins' (built-in)>,
'__name__': '__main__', '__package__': None}
>>> x = 4
>>> vars()
{'__doc__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__builtins__': <module 'builtins' (built-in)>,
'__name__': '__main__', '__package__': None, 'x': 4}
>>> print (2*x)
8
>>> 'x' in vars()
True
>>> 'print' in vars()
False
>>> vars()['y']=99
>>> y
99
>>> vars()
{'__doc__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__builtins__': <module 'builtins' (built-in)>,
'__name__': '__main__', 'y': 99, '__package__': None, 'x': 4}

**Practice Dictionary on Shell
>>> d = {'a':1,'b':2}
>>> d
{'b': 2, 'a': 1}
>>> d['b']
2
>>> d['c']=3
>>> d
{'c': 3, 'b': 2, 'a': 1}
'''

#Progam 4: Return Dictionary Count of Occurence of each Char in a string or int
#Run Module for Program to execute (F5)
#Type CharFrequencies(<integer> or <string> or <list>) - Name of Method in Shell to execute.    

'''
>>> CharFrequencies("sentence")
{'t': 1, 'e': 3, 's': 1, 'c': 1, 'n': 2}
>>> CharFrequencies([1,1,1,2,3,3,3,3,3,11])
{11: 1, 1: 3, 2: 1, 3: 5}
>>> CharFrequencies(['fgs','fgs','faizan'])
{'faizan': 1, 'fgs': 2}
'''

def CharFrequencies(iterable_obj):
    dic_freq = {}

    for item in iterable_obj:
        if item in dic_freq: #check if key is in dic_freq?
            dic_freq[item] += 1
        else:
            dic_freq[item] = 1 #if key is not in dic_freq
    return dic_freq
            
'''
**Concept: Set
- like a list, but doesnt hold duplicates
- use {item1,item2,...} to create
- not ordered

- operations:
    in, not in
    | - union key
    & - intersection
    ==, != - sets are equal
    (doesnt depend on ordering)
    
- methods
    add(item)
    remove(item)

**Shell Practice: Set
>>> s1 = {1,3,3,4,5,5,5,6}
>>> s1
{1, 3, 4, 5, 6}
>>> s2 = set ([0,2,4,6,8,10])
>>> s2
{0, 2, 4, 6, 8, 10}
>>> s1.add(7)
>>> s1.remove(3)
>>> s1
{1, 4, 5, 6, 7}
>>> s1&s2
{4, 6}
>>> s1|s2
{0, 1, 2, 4, 5, 6, 7, 8, 10}
'''

#Progam 4: Cipher the any message or Dicipher Secret codes through Dictionary
#Run Module for Program to execute (F5)
#Type Subcipher(<string>, <dictionary>) - Name of Method in Shell to execute.    

'''
>>> cipher = {'a':'d', 'c':'f'}
>>> Subcipher('cat', cipher)
'fdt'
'''

def Subcipher(code, cipher_dic):
    output = ""

    for char in code:
        if char in cipher_dic:        #translate it
            output += cipher_dic[char]
        else:
            output += char
    return output

#Using Subcipher() Method to decode the secret_code below
secret_code='''
>>> aitmjx xwan
Xwl Flc mo Texwmc, qe Xai Tlxljn

Qlksxaosu an qlxxlj xwkc srue.
Lztuayax an qlxxlj xwkc aituayax.
Naitul an qlxxlj xwkc ymitulz.
Ymitulz an qlxxlj xwkc ymituaykxlh.
Oukx an qlxxlj xwkc clnxlh.
Ntkjnl an qlxxlj xwkc hlcnl.
Jlkhkqauaxe ymscxn.
Ntlyaku yknln kjlc'x ntlyaku lcmsrw xm qjlkb xwl jsuln.
Kuxwmsrw tjkyxaykuaxe qlkxn tsjaxe.
Ljjmjn nwmsuh cldlj tknn naulcxue.
Sculnn lztuayaxue naulcylh.
Ac xwl okyl mo kiqarsaxe, jlosnl xwl xlitxkxamc xm rslnn.
Xwljl nwmsuh ql mcl-- kch tjloljkque mcue mcl --mqdamsn vke xm hm ax.
Kuxwmsrw xwkx vke ike cmx ql mqdamsn kx oajnx sculnn ems'jl Hsxyw.
Cmv an qlxxlj xwkc cldlj.
Kuxwmsrw cldlj an moxlc qlxxlj xwkc *jarwx* cmv.
Ao xwl aitulilcxkxamc an wkjh xm lztukac, ax'n k qkh ahlk.
Ao xwl aitulilcxkxamc an lkne xm lztukac, ax ike ql k rmmh ahlk.
Ckilntkyln kjl mcl wmcbacr rjlkx ahlk -- ulx'n hm imjl mo xwmnl!
'''

cipher = {'L':'e', 'X':'t', 'W':'h', 'K':'a', 'Q':'b', 'J':'r', 'C':'n', 'A':'i', 'N':'s'
          ,'O':'f', 'H':'d', 'E':'y', 'M':'o', 'R':'g', 'U':'l', 'I':'m', 'S':'u', 'D':'v', 'T':'p', 'Y':'c',
          'B':'k', 'Z':'x', 'V':'w'}

print(Subcipher(secret_code.upper(), cipher))
#type import this in Shell

'''
**Concept: Enumeration Iteration

1. Iteration
for item in lst:
    print(item)

2. Indexed Iteration
for i in range(len(lst)):
    print(lst[i])

NEW!
>>> fruit = ['apple','pear','orange']
>>> for i, item in enumerate(fruit):
	print (i,item)
0 apple
1 pear
2 orange
'''

'''
MIDTERM CSC242
'''

#Program 1:
'''
[25pts] Function fileLength, given to you, takes the name of a
file as input and returns the length of the file:

Usage:
>>> fileLength('Test File.txt')
95
>>> fileLength('Test File')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    fileLength('idterm.py')
  File "/Users/lperkovic/courses/csc242/homeworks/midterm.py", line 3, in fileLength
    infile = open(filename)
FileNotFoundError: [Errno 2] No such file or directory: 'idterm.py'

As shown above, if the file cannot be found by the interpreter or if it
cannot be read as a text file, an exception will be raised. Modify function
fileLength so that a friendly message is printed instead:

Usage:
>>> fileLength('Test File.txt')
95
>>> fileLength('Test File')
File Test File not found.
'''
#Run Module for Program to execute (F5)
#Type fileLength(<string>) - Name of Method in Shell to execute.

#Program 2:
'''
[25pts] Write a class named Marsupial that can be used as shown below:

Usage:
>>> m = Marsupial()
>>> m.put_in_pouch('doll')
>>> m.put_in_pouch('firetruck')
>>> m.put_in_pouch('kitten')
>>> m.pouch_contents()
['doll', 'firetruck', 'kitten']

Note: you will need to implement an __init__ constructor in addition to methods
put_in_pouch and pouch_contents.
'''
#Run Module for Program to execute (F5)

#Program 3:
'''
[25 pts] Write a class named Kangaroo as a subclass of Marsupial that
inherits all the attributes of Marsupial and also:
extends the Marsupial __init__ constructor to take, as input, the coordinates
x and y of the Kangaroo object,
supports method jump that takes number values dx and dy as input and moves
the kangaroo by dx units along the x-axis and by dy units along the y-axis, and
overloads the __str__ operator so it behaves as shown below.

Usage:
>>> k = Kangaroo(0,0)
>>> print(k)
I am a Kangaroo located at coordinates (0,0)
>>> k.put_in_pouch('doll')
>>> k.put_in_pouch('firetruck')
>>> k.put_in_pouch('kitten')
>>> k.pouch_contents()
['doll', 'firetruck', 'kitten']
>>> k.jump(1,0)
>>> k.jump(1,0)
>>> k.jump(1,0)
>>> print(k)
I am a Kangaroo located at coordinates (3,0)
'''
#Run Module for Program to execute (F5)

#Program 4:
'''
[25pts] Implement your own string class myStr that behaves like the regular
str class except that:
The addition (+) operator returns the sum of the lengths of the two strings
(instead of the concatenation).
The multiplication (*) operator returns the product of the lengths of
the two strings. 
The two operands, for both operators, are assumed to be strings; the
behavior of your implementation can be undefined if the second operand
is not a string.

Usage:
>>> x = myStr('hello') 
>>> x + 'universe' 
13 
>>> x * 'universe'
40
'''
#Run Module for Program to execute (F5)

'''
Python CSC242
Day 1 - 7/1/2016
'''

#Program 1: Reads the First line of Age from File
#Run Module for Program to execute (F5)
#Type readAge(<string>) - Name of Method in Shell to execute.
'''
>>> readAge("Py-Day 1 CSC242.txt")
Input/Output Error!
>>> readAge("Py-Day 1 CSC242 - age.txt")
Age is 21
'''

def readAge(str_filename):

    try:
        ifile = open(str_filename)
        line = ifile.readline()
        _age = int(line)

        print("Age is", _age)

    except IOError:
        print("Input/Output Error!")
    except ValueError:
        print("Value cannot be Converted to integer!")
    except:
        print("Other Error!")

'''
**Concept: GUI (Graphical User Interface)

Practice in Shell: Drawing Square

>>> import turtle
>>> sc = turtle.Screen()
>>> turtle.Turtle()
<turtle.Turtle object at 0x02DCDD50>
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.undo()
'''

#Program 2: Importing Turtle to Draw (GUI)
#Run Module for Program to execute (F5)

import turtle

t_screen = turtle.Screen()
t = turtle.Turtle()

# turtle t draws a smiley face with chin at coordinate (x, y)
x = 0
y = 0

# set turtle direction and pen size
t.pensize(3)
t.setheading(0)

# move to (x, y) and draw head
t.penup()
t.goto(x, y)
t.pendown()
t.circle(100)

# draw right eye
t.penup()
t.goto(x+35, y+120)
t.pendown()
t.dot(25)

# draw left eye
t.penup()
t.goto(x-35, y+120)
t.pendown()
t.dot(25)

#draw smile
t.penup()
t.goto(x-60.62, y+65)
t.pendown()
t.setheading(-60)  # smile is a 120 degree
t.circle(70, 120)  # section of a circle

#Program 3: Understanding Global Vs Local Scope
#Run Module for Program to execute (F5)
#Type f(<integer>) - Name of Method in Shell to execute.

def f(int_x):
    global y    #global scope has been stated explicitly
    y = 10

    return y * int_x

y = 0
print("f(3) = {}".format(f(3)))
print("y is {}".format(y))

    
#Program 4: Stack Concept - Calling Method within Methods
#Run Module for Program to execute (F5)
#Type h,g,j(<integer>) - Name of Method in Shell to execute.
'''
>>> h(15)
Func h()
0.06666666666666667
15
>>> g(15)
Func g()
Func h()
0.07142857142857142
14
15
>>> j(15)
Func j()
Func g()
Func h()
0.07692307692307693
13
14
15
'''

def h(int_x):
    try:
        print("Func h()")
        print(1 / int_x)
        print(int_x)
    except:
        print("Error!")

def g(int_x):
    print("Func g()")
    h(int_x - 1)
    print(int_x)

def j(int_x):
    print("Func j()")
    g(int_x - 1)
    print(int_x)

'''
**Concept Review: Different Ways of Importing Libraries

>>> from math import sqrt
>>> sqrt(16)
4.0

>>> from random import randint
>>> randint(1, 6)
6

Importing Everything from the Library
>>> from math import *
>>> pi
3.141592653589793
>>> e
2.718281828459045

**Concept Review: String Methods
>>> fgs = "Fishy Goon Squad"
>>> str.lower(fgs)
'fishy goon squad'
>>> str.find(fgs, 'o')
7
>>> str.replace(fgs, "Squad", "SQUAD!")
'Fishy Goon SQUAD!'

Reversing the String:
>>> fgs = "fishy"
>>> print(fgs[::-1])
yhsif

>>> h = "hello"
>>> retVal = ""
>>> for item in h:
	retVal = item + retVal
>>> retVal
'olleh'

**Adding from 0-99
>>> total = 0
>>> for i in range(100):
	total += i
>>> total
4950

**CONCEPT: Order of Unicode Alphabets
>>> for i in range(65, 91):
	print(chr(i), end=" ")
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

>>> char = 'Q'
>>> ord(char) - ord('A') + 1
17
>>> char = 'A'
>>> ord(char) - ord('A') + 1
1
'''

#Program 5: Point Class - represent a point in plane
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = Point()

>>> obj.setX(2)
>>> obj.setY(5)
>>> obj.getX()
2
>>> obj.get()
(2, 5)
>>> obj.move(5, 3)
>>> obj.get()
(7, 8)

Accessing Public variables
>>> obj.x
2
>>> obj.y
5
'''

class Point:

    #setters

    def setX(self, int_x):
        self.x = int_x

    def setY(self, int_y):
        self.y = int_y

    #getters

    def get(self):
        return self.x, self.y

    def getX(self):
        return self.x

    #other methods

    def move(self, mov_x, mov_y):
        self.x += mov_x
        self.y += mov_y

'''Version 2: self is not stated explicitly
Moreover you can initialize the variables when you instantiate Class object.

>>> obj = PointV2(2,5)
>>> obj.get()
(2, 5)

>>> obj.setX(1)
>>> obj.setY(1)
>>> obj.get()
(1, 1)

>>> obj.move(2,  -2)
>>> obj.getX()
3
>>> obj.get()
(3, -1)
'''
class PointV2(object):
    
    #initialize    
    def __init__(self, int_x, int_y):
        self.x = int_x
        self.y = int_y

    #setters
    def setX(self, int_x):
        self.x = int_x

    def setY(self, int_y):
        self.y = int_y

    #getters
    def get(self):
        return self.x, self.y

    def getX(self):
        return self.x

    #other methods
    def move(self, mov_x, mov_y):
        self.x += mov_x
        self.y += mov_y

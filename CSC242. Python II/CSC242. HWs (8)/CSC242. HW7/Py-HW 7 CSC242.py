'''
Python CSC242
HW7 Solutions
'''

#Problem 1: pattern(), square() - Recursive Method
'''
>>> from turtle import Screen, Turtle
>>> s = Screen()
>>> t = Turtle()
>>> square(t,0,0,300)

>>> from turtle import Screen, Turtle
>>> s = Screen()
>>> t = Turtle()
>>> pattern(t,0,0,300,2)

>>> from turtle import Screen, Turtle
>>> s = Screen()
>>> t = Turtle()
>>> pattern(t,0,0,300,3)

>>> from turtle import Screen, Turtle
>>> s = Screen()
>>> t = Turtle()
>>> pattern(t,0,0,300,4)
'''

def jump(t, x, y):
    'makes turtle t jump to coordinates (x, y)'

    t.penup()
    t.goto(x,y)
    t.pendown()

def square(t,x,y,l):
    'draws square centered at (x,y) of side length l'
    jump(t, x-l/2, y-l/2)
    
    t.setheading(0)
    t.color('black', 'red')
    t.begin_fill()
    t.goto(x+l/2,y-l/2)
    t.left(90)
    t.goto(x+l/2,y+l/2)
    t.left(90)
    t.goto(x-l/2,y+l/2)
    t.left(90)
    t.goto(x-l/2,y-l/2)
    t.end_fill()

def pattern(t,x,y,l,n):
    'draws pattern n'

    if(n > 0):
        pattern(t,x+l/2,y+l/2,l/2.2,n-1)
        square(t,x,y,l)
        pattern(t,x-l/2,y+l/2,l/2.2,n-1)
        pattern(t,x+l/2,y-l/2,l/2.2,n-1)
        pattern(t,x-l/2,y-l/2,l/2.2,n-1)

#Problem 2: Game bears(<integer>)
'''
>>> bears(21)
False
>>> bears(22)
True
>>> bears(30)
True
>>> bears(76)
True
>>> bears(250)
False
>>> bears(260)
True
'''

def bears(int_n):
    'returns True if there is a way to apply the rules and end up with 22 bears'

    if(int_n < 22):
        return False
    
    if(int_n == 22):
        return True
    if(int_n % 10 == 0 and bears(int_n -8)):
        return True
    if(int_n % 2 == 0 and bears(int_n // 2)):
        return True
    if(int_n % 3 == 0 and bears(int_n -22)):
        return True
    if(int_n % 4 == 0 and bears(int_n -10)):
        return True

    return False
    
#Problem 3: directory(<string>, <integer>) - Recursive
'''
>>> directory('test', 0)
 test
     test\dir1
         test\dir1\dir3
             test\dir1\dir3\dir4
                 test\dir1\dir3\dir4\file3.txt
                 test\dir1\dir3\dir4\file5.txt
             test\dir1\dir3\file2.txt
         test\dir1\file1.txt
     test\dir2
         test\dir2\file6.txt
         test\dir2\file7.txt
     test\file4.txt
'''
import os

def directory(str_path, int_n):
    '''prints pathanme and, with appropriate indentation, the pathname of
       every item contained directly or indirectly in folder pathname'''

    print(int_n * " ", str_path)

    try:
        items = os.listdir(str_path)

    except:
        return

    for item in items:
        path = os.path.join(str_path, item)
        directory(path, int_n +4)
    
#Problem 4: traverse(<string>) - Recursive Method
'''
>>> traverse('file0.txt')
Visiting file0.txt
Visiting file1.txt
Visiting file3.txt
Visiting file4.txt
Visiting file8.txt
Visiting file9.txt
Visiting file2.txt
Visiting file5.txt
Visiting file6.txt
Visiting file7.txt
'''

def traverse(str_filename):
    'visits file and recursively visits all files listed in file'

    ifile = open(str_filename, 'r')
    print('Visiting', str_filename)

    for item in ifile:
        traverse(item[:-1])

    ifile.close()
    
#Problem 5: permutations(<list>) - Recursive
'''
>>> permutations([1])
[[1]]
>>> permutations([1,2])
[[1, 2], [2, 1]]
>>> permutations([1,2,3])
[[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
>>> permutations([1,2,3,4])
[[1, 2, 3, 4], [2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1], [1, 3, 2, 4], [3, 1, 2, 4], [3, 2, 1, 4], [3, 2, 4, 1], [1, 3, 4, 2], [3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1], [1, 2, 4, 3], [2, 1, 4, 3], [2, 4, 1, 3], [2, 4, 3, 1], [1, 4, 2, 3], [4, 1, 2, 3], [4, 2, 1, 3], [4, 2, 3, 1], [1, 4, 3, 2], [4, 1, 3, 2], [4, 3, 1, 2], [4, 3, 2, 1]]

>>> permutationsV2('212')
{'122', '212', '221'}
>>> permutationsV2('fa')
{'af', 'fa'}
'''

def permutations(lst):
    'returns a list of all permutations (as lists) of list lst'
    retList = []

    if(len(lst) < 2):
        retList.append(lst)
        return retList

    firstItem = lst[0]
    p = permutations(lst[1:])

    for item in p:
        for i in range(len(lst)):
            temp = item[:i]
            temp.append(firstItem)
            temp = temp + item[i:]

            retList.append(temp)
    return retList

#Version 2: using enumerate

def permutationsV2(str_item):
    retList = []

    if(len(str_item) == 1):
        retList = [str_item]

    else:
        for i, j in enumerate(str_item):
            for item in permutationsV2(str_item[:i] + str_item[i +1:]):
                retList += [j + item]

    return set(retList)

# Testing shell - - - - - - - - - - - - - - - - -
# for a in unique(permutations([1,1,2])):
#   print a

'''
if __name__ == '__main__':
    print(bears(21))  # False
    print(bears(22))  # True
    print(bears(30))  # True
    print(bears(76))  # True
    print(bears(250)) # False
    print(bears(260)) # True
    directory('homework7.py', 0)
    directory('test', 0)
    traverse('file0.txt')
    from turtle import Screen, Turtle
    s = Screen()
    t = Turtle()
    pattern(t,0,0,300,2)
'''

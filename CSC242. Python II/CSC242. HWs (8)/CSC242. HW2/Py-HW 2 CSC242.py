'''
Python CSC242
HW2 Solutions
'''

#Problem 1:
'''
>>> obj = Animal()
>>> obj.setSpecies('dog')
>>> obj.setLanguage('bark')
>>> obj.speak()
dog speaks bark.
'''

class Animal:
    'represents an animal'

    #setters
    
    def setSpecies(self, species):
        self.spec = species

    def setLanguage(self, language):
        self.lang = language

    #other method
        
    def speak(self):
        print('{} speaks {}.'.format(self.spec, self.lang))

#Problem 2:
'''
>>> obj = Polygon()
>>> obj.numSides(6)
>>> obj.sideLength(1)
>>> obj.perimeter()
6
>>> obj.area()
2.598076211353316
'''

import math

class Polygon(object):

    def numSides(self, sides):
        self.sides = sides

    def sideLength(self, length):
        self.length = length

    def perimeter(self):
        return self.sides * self.length

    def area(self):
        return (self.sides * self.length ** 2) / (4 * math.tan(math.pi / self.sides))

#Problem 3:
'''
>>> obj = Craps()
>>> obj.newGame()
Throw Total: 8 . Throw FOR POINT!
>>> obj.forPoint()
Throw Total: 6 . Throw FOR POINT!
>>> obj.forPoint()
Throw Total: 8 ... you WON!
'''

from random import randrange

class Craps(object):

    def newGame(self):
        self.initialRoll = randrange(1,7) + randrange(1,7)

        if(self.initialRoll in [7,11]):
            print("Throw Total:", str(self.initialRoll), "... you WON!")
        elif(self.initialRoll in [2,3,12]):
            print("Throw Total:", str(self.initialRoll), "... you LOST!")
        else:
            print("Throw Total:", str(self.initialRoll), ". Throw FOR POINT!")

    def forPoint(self):
        roll = randrange(1,7) + randrange(1,7)

        if(roll == self.initialRoll):
            print("Throw Total:", str(roll), "... you WON!")
        elif(roll == 7):
            print("Throw Total:", str(roll), "... you LOST!")
        else:
            print("Throw Total:", str(roll), ". Throw FOR POINT!")

#Problem 4:
'''
>>> obj = BankAccount(700)
>>> obj.balance()
700
>>> obj.withDraw(70)
>>> obj.balance()
630
>>> obj.deposit(7)
>>> obj.balance()
637
'''

class BankAccount(object):

    def __init__(self, initialAmount = 0):
        self.initialAmount = initialAmount

    def withDraw(self, amount):
        self.initialAmount -= amount

    def deposit(self, amount):
        self.initialAmount += amount

    def balance(self):
        return self.initialAmount

#Problem 5:
'''
>>> obj = Date()
>>> obj.display('MDY')
'07/12/16'
>>> obj.display('MODY')
'Jul 12, 2016'
'''

import time

class Date(object):

    def __init__(self):
        self.time = time.localtime()

    def display(self, form):
        if(form == 'MDY'):
            return time.strftime('%m/%d/%y', self.time)
        elif(form == 'MDYY'):
            return time.strftime('%m/%d/%Y', self.time)
        elif form == 'DMY':
            return time.strftime('%d/%m/%y', self.time)
        elif form == 'DMYY':
            return time.strftime('%d/%m/%Y', self.time)
        elif form == 'MODY':
            return time.strftime('%b %d, %Y', self.time)

        
##### TESTING ALL CLASSES #####

if(__name__ == '__main__'):

    print("-- Animal() Class --")
    snoopy = Animal()
    snoopy.setSpecies('dog') 
    snoopy.setLanguage('bark')
    snoopy.speak()

    print("\n-- Polygon() Class --")
    p = Polygon()
    p.numSides(6)
    p.sideLength(1)
    print(p.perimeter())             
    print(p.area()) 

    print("\n-- BankAccount() Class --")
    x = BankAccount(700)
    print(x.balance())               
    x.withDraw(70)
    print(x.balance())               
    x.deposit(7)
    print(x.balance()) 

    print("\n-- Date() Class --")
    d = Date()
    print(d.display('MDY'))          # '01/14/14'
    print(d.display('MODY'))         # 'Jan 14, 2014'

    print("\n-- Craps() Class --")
    c = Craps()
    c.newGame()

'''
Python CSC242
Day 3 - 7/2/2016

Overriding vs Overloading

Method overriding is an object-oriented programming feature that allows
a subclass to provide a different implementation of a method that is already
defined by its superclass or by one of its superclasses. The implementation
in the subclass overrides the implementation of the superclass by providing a
method with the same name, same parameters or signature, and same return type
as the method of the parent class.

Overloading is the ability to define the same method, with the same name
but with a different number of arguments and types. It's the ability of one
function to perform different tasks, depending on the number of parameters or
the types of the parameters. 
'''

#Class 1: Animal() & Bird() - Understanding Inheritance & Sub Classes
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = baseAnimal()
>>> obj.speak()
animal speaks make sounds.

>>> obj =  baseAnimal("Lion", "Meows")
>>> obj.speak()
Lion speaks Meows.
>>> obj.setLanguage("Roars")
>>> obj.speak()
Lion speaks Roars.
>>> obj.setSpecies("Cat")
>>> obj.speak()
Cat speaks Roars.

Sub Class
>>> obj = Bird("Sparrow", "tweets")
>>> obj.speak()
tweets!tweets!tweets!
'''

class baseAnimal:
    'represents an animal'

    #initialize
    def __init__(self, species="animal", language="make sounds"):
        self.spec = species
        self.lang = language

    #setters
    def setSpecies(self, species):
        self.spec = species

    def setLanguage(self, language):
        self.lang = language

    #other methods
    def speak(self):
        print("{} speaks {}.".format(self.spec, self.lang))

class Bird(baseAnimal):
    'inherits from base class and its methods &'

    #__init__ method is not written explicitly for extend.
    #this class uses the baseClass __init__ instead.

    def speak(self):
        print("{}!".format(self.lang) * 3)


#Class 2: Queue() and EmptyQueueError() and QueueIterator()
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = Queue()
>>> obj.isEmpty()
True
>>> obj.enqueue("fishy")
>>> obj.enqueue("goon")
>>> obj.enqueue("squad")
>>> obj.enqueue("!")
>>> obj.isEmpty()
False
>>> print(obj)
['fishy', 'goon', 'squad', '!']
>>> obj.dequeue()
'fishy'
>>> print(obj)
['goon', 'squad', '!']
'''

class Queue:
    'classic queue class'

    #initialize
    def __init__(self):
        self.itemList = []

    #other methods
    def isEmpty(self):
        return (len(self.itemList) == 0)

    def enqueue(self, item):
        return self.itemList.append(item)

    def dequeue(self):
        'remove & return item at front of queue'
        if(self.isEmpty()):
            raise EmptyQueueError("Queue is Empty!")
        
        return self.itemList.pop(0)

    #similar - toString() in Java
    def __repr__(self):
        return "{}".format(self.itemList)

#error class
class EmptyQueueError(Exception):
    pass

#Making Class iterable
'''
>>> obj = Queue()
>>> obj.enqueue("fishy")
>>> obj.enqueue("squad")

>>> obj2 = QueueIterator(obj.itemList)
>>> for item in obj2:
	print(item)
squad
fishy
>>> for item in QueueIterator(obj.itemList):
	print(item)
squad
fishy

'''

class QueueIterator:

    #constructor
    def __init__(self, itemList):
        self.index = len(itemList) -1
        self.itemList = itemList

    def __iter__(self):
        return self

    def __next__(self):
        '''returns next Queue item; if no next item,
           raises StopIteration exception'''
        if(self.index < 0):
            raise StopIteration()

        retVal = self.itemList[self.index]
        self.index -= 1
        return retVal


# Some Important Implementations to extend this Class

'''
#   Added in Section 8.4
#    def __init__(self, itemList=None):
#        'initialize queue based on list q, default is empty queue'
#        if itemList == None:
#            self.itemList = []
#        else:
#            self.itemList = itemList
#
#    def __eq__(self, other):
#        'return True if queues self and other contain the same items in the same order'
#        return self.itemList == other.itemList
#
#    def __len__(self):
#        'returns number of items in queue'
#        return len(self.itemList)
#
#    def __repr__(self):
#        'return canonical string representation of queue'
#        return 'Queue({})'.format(self.itemList)
#
#    Added in Section 8.6
#    def dequeue(self):
#        'remove and return item at front of queue'
#        if len(self) == 0:
#            raise EmptyQueueError('dequeue from empty queue')
#        return self.itemList.pop(0)
#
#    Solution to Problem 8.9
#    def dequeue(self):
#        'removes and returns item at front of the queue raises KeyboardInterrupt exception if queue is empty'
#        if len(self) == 0:
#            raise KeyboardInterrupt('dequeue from empty queue')
#
#        return self.itemList.pop(0)
#
#    Added in Section 8.7
#    def __iter__(self):
#        'returns Queue iterator'
#        return QueueIterator(self)
'''

#Class 3: MyList()
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = MyList([1,2,3])
>>> obj.choice()
1
>>> obj.choice()
3
>>> obj.choice()
2
>>> obj.choice()
3
'''

import random

class MyList(list):
    'a subclass of list that implements method choice'

    def choice(self):
        'return item from list chosen uniformly at random'
        return random.choice(self)

#Class 4: Super() - Super Classes and Extenders
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = Super()
>>> obj.method()
Super Class!

>>> obj2 = Replacer()
>>> obj2.method()
Override Super. Now Replacer Class!

>>> obj3 = Extender()
>>> obj3.method()
Extender Begins
Super Class!
Extender Ends
'''

class Super:

    def method(self):
        print("Super Class!")

class Inheritor(Super):
    pass

class Replacer(Super):
    'overriding method'
    def method(self):
        print("Override Super. Now Replacer Class!")

class Extender(Super):
    'extending class'

    def method(self):
        print("Extender Begins")
        Super.method(self)
        print("Extender Ends")

#Class 5: SimpleListQueue() 
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = SimpleListQueue([1,2,3,4,5])
>>> obj.isEmpty()
False
>>> obj.dequeue()
1
>>> obj.enqueue(6)
'''

class SimpleListQueue(list):
    'subclass of list'

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, item):
        return self.append(item)

    def dequeue(self):
        return self.pop(0)

#Class 6: Rectangle()
#Run Module for Program to execute (F5)
'''
Assign variable as Class Object to use its Methods - in Shell to execute.

>>> obj = Rectangle()
>>> obj.setSize(5,3)
>>> obj.perimeter()
16
>>> obj.area()
15
'''

class Rectangle:

    #constructor
    def setSize(self, x_length, y_length):
        self.x = x_length
        self.y = y_length

    def perimeter(self):
        return (self.x + self.y) * 2

    def area(self):
        return self.x * self.y

#Class 7: OddList() and ListIterator()
#Run Module for Program to execute (F5)
'''
>>> obj = OddList([1,2,3,4,5])
>>> print(obj)
[1, 2, 3, 4, 5]

>>> for item in obj:
	print(item)
1
3
5
'''

class OddList(list):

    def __iter__(self):
        return ListIterator(self)


class ListIterator(object):
    'peculiar iterator for OddList Class'

    #constructor
    def __init__(self, obj_list):
        self.obj_list = obj_list
        self.index = 0

    def __next__(self):
        'return next OddList item'

        if(self.index >= len(self.obj_list)):
           raise StopIteration

        retVal = self.obj_list[self.index]
        self.index += 2

        return retVal

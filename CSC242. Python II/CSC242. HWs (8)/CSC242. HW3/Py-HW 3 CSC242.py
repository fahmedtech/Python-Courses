'''
Python CSC242
HW2 Solutions
'''

#Problem 1:
'''
>>> print("-- PriorityQueue Class() --")
>>> pq = PriorityQueue()
>>> pq.insert(4)
>>> pq.insert(2)
>>> pq.insert(7)
>>> pq.insert(5)
>>> len(pq)
>>> pq.min()
>>> pq.removeMin()
>>> pq.removeMin()
>>> pq.removeMin()
>>> pq.min()
>>> len(pq)

    def min(self):
        self.q.sort()
        return self.q[0]

    def removeMin(self):
        self.q.sort()
        return self.q.pop(0)
'''

class PriorityQueue(object):

    def __init__(self):
        self.arrList = []

    def insert(self, item):
        self.arrList.append(item)
        self.arrList.sort(reverse=True)

    def min(self):
        return self.arrList[-1]

    def removeMin(self):
        return self.arrList.pop()

    def __len__(self):
        return len(self.arrList)

    def isEmpty(self):
        return len(self) == 0

#Problem 2:
'''
>>> pq = PriorityQueue2()
>>> pq.insert(4)
>>> pq.insert(2)
>>> pq.insert(7)
>>> pq.insert(5)
>>> len(pq)
4
>>> pq.min()
2
>>> pq.removeMin()
>>> pq.removeMin()
>>> pq.removeMin()
>>> pq.min()
7
>>> len(pq)
1
'''

class PriorityQueue2(object):

    def __init__(self):
        self.arrList = []

    def insert(self, item):
        self.arrList.append(item)

    def min(self):
        return min(self.arrList)

    def removeMin(self):
        return self.arrList.remove(min(self.arrList))

    def __len__(self):
        return len(self.arrList)

    def isEmpty(self):
        return len(self) == 0

#Problem 3: Hand() - importing Card() and Deck() Library
'''
>>> obj = Hand('Player ID 1')

>>> deck = Deck()
>>> deck.shuffle()

>>> obj.addCard(deck.dealCard())
>>> obj.addCard(deck.dealCard())
>>> obj.addCard(deck.dealCard())
>>> len(obj)
3
>>> obj.showHand()
Player ID 1:   J ♡   Q ♢  10 ♢
'''

from cards import Card, Deck

class Hand(object):
    'represent hand of playing cards'

    def __init__(self, player):
        self.player = player
        self.arrHand = []

    def __len__(self):
        return len(self.arrHand)

    def addCard(self, card):
        self.arrHand.append(card)

    def showHand(self):
        print("{}:".format(self.player), end='')

        for item in self.arrHand:
            rank = item.getRank()
            suit = item.getSuit()

            print("{:>4} {}".format(rank, suit), end='')

#Problem 4: BlackjackHand() - sub class of Hand
'''
>>> d = Deck()
>>> d.shuffle()

>>> p1 = BlackjackHand('Player 1')
>>> p2 = BlackjackHand('Player 2')

>>> p1.addCard(d.dealCard())
>>> p2.addCard(d.dealCard())
>>> p1.addCard(d.dealCard())
>>> p2.addCard(d.dealCard())

>>> p1.showHand()
Player 1:   2 ♢   Q ♠
>>> p2.showHand()
Player 2:   6 ♠   5 ♠

>>> p1.total()
12
>>> p2.total()
11
'''

class BlackjackHand(Hand):
    'represents a blackjack hand'

    rankVal = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
               '9':9, '1':10, 'J':10, 'Q':10, 'K':10, 'A':11}

    def total(self):
        'returns the value of blackjack hand'
        _result, _numAces = 0, 0

        for item in self.arrHand:
            _result += self.rankVal[item.getRank()]

            if(item.getRank() == 'A'):
                _numAces += 1
                
        #while value of hand is >21 & ACE is in hand with rankVal 11
        #convert ACE value to 1
        while(_result > 21 and _numAces > 0):
            _result -= 10
            _numAces -= 1

        return _result

#Problem 5: Polygon(), Square(), Triangle() 
'''
>>> s = Square(2)
>>> s.perimeter()
8
>>> s.area()
4

>>> t = Triangle(3)
>>> t.perimeter()
9
>>> t.area()
3.8971143170299736
'''

from math import tan, pi

#Polygon Class()
class Polygon(object):
    'regular polygon class'

    def __init__(self, n_sided, side_length):
        self.n = n_sided
        self.s = side_length

    def perimeter(self):
        return self.n * self.s

    def area(self):
        return (self.n * self.s ** 2) / (4 * math.tan(math.pi / self.n))

#SQUARE Class()
class Square(Polygon):
    'extends Polygon class'

    def __init__(self, side_length):
        Polygon.__init__(self, 4, side_length)

    def area(self):
        return self.s ** 2

#TRIANGLE Class()
from math import sqrt

class Triangle(Polygon):
    'extends Polygon class'

    def __init__(self, side_length):
        Polygon.__init__(self, 3, side_length)

    def area(self):
        return (self.s ** 2 * sqrt(3)) / 4
    

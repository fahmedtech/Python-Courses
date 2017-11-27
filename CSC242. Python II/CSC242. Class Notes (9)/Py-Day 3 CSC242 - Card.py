'''
Python CSC242
Day 3 - 7/2/2016
'''

#Class 1: Card()
#Run Module for Program to execute (F5)
'''
>>> obj = Card('A', "Spade")
>>> print(obj)
Card('A', 'Spade')
>>> obj.getRank()
'A'
>>> obj.getSuit()
'Spade'
'''

from random import shuffle

class Card:
    'represents a playing card'

    #initialize
    def __init__(self, card_rank, card_suit):
        self.rank = card_rank
        self.suit = card_suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __repr__(self):
        'return formal representation'
        return "Card('{}', '{}')".format(self.rank, self.suit)

'''
You can also Implement the following Methods.

#    def __eq__(self, other):
#        'self == other if rank and suit are the same'
#        return self.rank == other.rank and self.suit == other.suit
'''

#Class 2: Deck()
#Run Module for Program to execute (F5)
'''
>>> obj = Deck()
>>> print(obj)
Deck([Card('K', '♢'), Card('6', '♢'), Card('Q', '♢'), Card('10', '♢'), Card('9', '♢'), Card('A', '♢'), Card('2', '♢'), Card('7', '♢'), Card('3', '♢'), Card('8', '♢'), Card('5', '♢'), Card('J', '♢'), Card('4', '♢'), Card('K', '♠'), Card('6', '♠'), Card('Q', '♠'), Card('10', '♠'), Card('9', '♠'), Card('A', '♠'), Card('2', '♠'), Card('7', '♠'), Card('3', '♠'), Card('8', '♠'), Card('5', '♠'), Card('J', '♠'), Card('4', '♠'), Card('K', '♣'), Card('6', '♣'), Card('Q', '♣'), Card('10', '♣'), Card('9', '♣'), Card('A', '♣'), Card('2', '♣'), Card('7', '♣'), Card('3', '♣'), Card('8', '♣'), Card('5', '♣'), Card('J', '♣'), Card('4', '♣'), Card('K', '♡'), Card('6', '♡'), Card('Q', '♡'), Card('10', '♡'), Card('9', '♡'), Card('A', '♡'), Card('2', '♡'), Card('7', '♡'), Card('3', '♡'), Card('8', '♡'), Card('5', '♡'), Card('J', '♡'), Card('4', '♡')])
>>> obj.__len__()
52

>>> obj.shuffleCards()
>>> obj.dealCard()
Card('A', '♢')
>>> obj.__len__()
51
>>> print(obj)
Deck([Card('5', '♡'), Card('10', '♢'), Card('K', '♡'), Card('K', '♠'), Card('Q', '♢'), Card('8', '♢'), Card('9', '♠'), Card('4', '♠'), Card('A', '♠'), Card('K', '♢'), Card('5', '♠'), Card('3', '♢'), Card('2', '♡'), Card('6', '♣'), Card('A', '♡'), Card('3', '♠'), Card('2', '♣'), Card('2', '♢'), Card('4', '♡'), Card('Q', '♣'), Card('7', '♢'), Card('7', '♣'), Card('3', '♡'), Card('Q', '♠'), Card('6', '♡'), Card('3', '♣'), Card('7', '♠'), Card('10', '♡'), Card('9', '♣'), Card('A', '♣'), Card('J', '♠'), Card('Q', '♡'), Card('J', '♢'), Card('4', '♣'), Card('K', '♣'), Card('8', '♠'), Card('5', '♣'), Card('6', '♠'), Card('2', '♠'), Card('10', '♠'), Card('9', '♢'), Card('8', '♣'), Card('6', '♢'), Card('5', '♢'), Card('9', '♡'), Card('J', '♣'), Card('7', '♡'), Card('J', '♡'), Card('8', '♡'), Card('10', '♣'), Card('4', '♢')])
'''

class Deck:
    'represent deck of 52 cards'

    _rankDict = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    _suitDict = {'\u2660', '\u2661', '\u2662', '\u2663'} #unicode symbols

    #initialize
    def __init__(self):
        self.deck = []

        for suitItem in Deck._suitDict:
            for rankItem in Deck._rankDict:
                self.deck.append(Card(rankItem, suitItem))

    #other methods
    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        if(len(self.deck) > 0):
            return self.deck.pop()
        else:
            raise EmptyDeckError()

    def shuffleCards(self):
        shuffle(self.deck)

    def __len__(self):
        return len(self.deck)

    #toString
    def __repr__(self):
        return "Deck({})".format(self.deck)
    

'''
Further Implementing __init__ Method - Providing user a new Deck!

#    Solution to Practice Problem 8.5
#    def __init__(self, cardList=None):
#        'initialize deck of cards, either using an input list of cards or by generating a standard deck of 52 cards'
#        
#        if cardList != None:     # input deck provided
#            self.deck = cardList
#        else:                    # no input deck
#            # self.deck is a list of 52 standard playing cards
#            self.deck = []
#            # generate every combination of rank and suit
#            for suit in Deck.suits:
#                for rank in Deck.ranks:
#                    # create Card with rank and suit
#                    # and add to deck
#                    self.deck.append(Card(rank,suit))

#    def __eq__(self, other):
#        'returns True if decks have the same cards in the same order'
#        return self.deck == other.deck
'''
    

#Class 3: EmptyDeckError()
#Run Module for Program to execute (F5)
'''
>>> d = Deck()
>>> for i in range(1,52):
	d.dealCard()

>>> d.__len__()
1
>>> d.dealCard()
Card('9', '♡')

>>> d.dealCard()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d.dealCard()
  File "C:/Users/Ahmed/Downloads/Py-Day 3 CSC242 - Card.py", line 84, in dealCard
    raise EmptyDeckError()
EmptyDeckError: Empty Deck!
>>> 
'''

class EmptyDeckError(Exception):

    def __str__(self):
        return "Empty Deck!"

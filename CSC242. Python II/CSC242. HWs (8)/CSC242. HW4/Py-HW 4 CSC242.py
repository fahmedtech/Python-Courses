'''
Python CSC242
HW4 Solutions
'''

#Problem 1: BankAccount2() Class
'''
>>> x = BankAccount2(-700)
ValueError
>>> x = BankAccount2(700)
>>> x.withDraw(70)
>>> x.balance()
630
>>> x.deposit(-7)
ValueError
>>> x.deposit(7)
>>> x.balance()
637
'''

class BankAccount2(object):

    def __init__(self, initialAmount = 0):
        if(initialAmount < 0):
            raise ValueError

        self.i = initialAmount

    def withDraw(self, amount):
        if(self.i - amount < 0):
            raise ValueError

        self.i -= amount

    def deposit(self, amount):
        if(amount < 0):
            raise ValueError

        self.i += amount

    def balance(self):
        return self.i

#Problem 2:
'''
>>> x = BankAccount3(-5)
NegativeBalance: Negative Balance Exception: -5

>>> x = BankAccount3(5)
>>> x.withDraw(7)
NegativeBalance: Negative Balance Exception: -2

>>> x.deposit(-3)
NegativeDeposit: Negative Deposit Exception: -3

>>> x.withDraw(2)
>>> x.deposit(3)
>>> x.balance()
6
'''

#Exception Classes

class NegativeBalance(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Negative Balance Exception: " + repr(self.value)

class NegativeDeposit(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Negative Deposit Exception: " + repr(self.value)

#BANK ACCOUNT 3

class BankAccount3(object):

    def __init__(self, initialAmount = 0):
        if(initialAmount < 0):
            raise NegativeBalance(initialAmount)

        self.i = initialAmount

    def withDraw(self, amount):
        if(self.i - amount < 0):
            raise NegativeBalance(self.i - amount)

        self.i -= amount

    def deposit(self, amount):
        if(amount < 0):
            raise NegativeDeposit(amount)

        self.i += amount

    def balance(self):
        return self.i
            
#Problem 3: BankAccount4() extends BankAccount3()
'''
>>> x = BankAccount4(4.5,100)
>>> x.balance()
100
>>> x.addInterest()
>>> x.balance()
104.5
>>> x.addInterest()
>>> x.balance()
109.20249999999999
>>> x.addInterest()
>>> x.balance()
114.11661249999997
>>> x.addInterest()
>>> x.balance()
119.25186006249996
>>> x.addInterest()
>>> x.balance()
124.61819376531244
'''

class BankAccount4(BankAccount3):

    def __init__(self, rate, initialAmount = 0):
        BankAccount3.__init__(self, initialAmount)
        self.rate = rate

    def addInterest(self):
        self.i *= (1 + self.rate / 100)
        
#Problem 4: Textfile() Class
'''
>>> t = Textfile('raven.txt')
>>> t.nChars()
6299
>>> t.nWords()
1125
>>> t.nLines()
126
>>> t.grep('nevermore')
75: Of "Never-nevermore."'
89: She shall press, ah, nevermore!
124: Shall be lifted - nevermore!

>>> print(t.read())
Once upon a midnight dreary, while I pondered weak and weary,
Over many a quaint and curious volume of forgotten lore,

>>> t.occurences()
{'then,': 1, 'we': 2, 'Not': 1, 'a': 15, 'God': 2 ..}
'''
from string import punctuation

class Textfile(object):
    'class provides tools to analyze textfile'

    def __init__(self, str_filename):
        self.name = str_filename

        ifile = open(str_filename)
        self.content = ifile.read()
        ifile.close()

    def nChars(self):
        return len(self.content)

    def nWords(self):
        return len(self.content.split())

    def nLines(self):
        return self.content.count('\n') +1

    def read(self):
        return self.content

    def readlines(self):
        return self.content.split('\n')

    def grep(self, target):
        lineLst = self.readlines()

        for i in range(len(lineLst)):
            if(lineLst[i].find(target) >= 0):
                print("{}: {}".format(i, lineLst[i]))

    def occurences(self):
        #table = str.maketrans(punctuation, ' '*len(punctuation))
        #clean = self.content.translate(table)
        wordDict = {}

        for item in self.content.split():
            if(item not in wordDict):
                wordDict[item] = 1
            else:
                wordDict[item] += 1

        return wordDict
                

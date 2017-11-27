'''
Python CSC242
HW 1 - Solutions
'''

#Problem 1: forPoint(<integer>), craps(), testCraps(<integer>)
'''
>>> forPoint(5)
1
>>> forPoint(5)
0

>>> craps()
1

>>> testCraps(1000)
0.5
'''

from random import randint

def forPoint(int_initialRoll):

    while True:
        roll = randint(1,6) + randint(1,6) #randrange is (1,7)

        if(roll == 7):
            return 0
        elif(roll == int_initialRoll):
            return 1

def craps():
    roll = randint(1,6) + randint(1,6)

    if(roll in [7, 11]):
        return 1
    elif(roll not in [2, 3, 12]):
        return forPoint(roll)
    else: 
        return 0

def testCraps(int_num):
    _wins = 0

    for i in range(int_num):
        _wins += craps()

    return _wins/int_num

#Problem 2: Mirror(<string>)
'''
>>> Mirror('boxwood')
'boowxod'
>>> Mirror('bidi')
'ibid'
>>> Mirror('bed')
'INVALID'
>>> Mirror('ddd')
'bbb'
'''

def Mirror(str_word):
    mirDict = {'b':'d', 'd':'b', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}
    retVal = ''

    for item in str_word:
        if(item in mirDict):
            retVal = mirDict[item] + retVal

        else:
            return "INVALID"
        
    return retVal

#Problem 3: Only uppercase quick Sum.
'''
>>> quickSum('ACM')
46
>>> quickSum('MID CENTRAL')
650

>>> testQuickSum('quicksum.txt')
46
650
4690
49
75
14
15
'''

def quickSum(str_line):
    _totalSum, _index = 0, 0

    for item in str_line:
        _index += 1

        if(item != ' ' and item != '\r'):
            _totalSum += _index * (ord(item) - ord('A') +1)

    return _totalSum

def testQuickSum(str_filename):

    ifile = open(str_filename, 'r')
    lineList = ifile.readlines()
    ifile.close()

    for item in lineList:
        item = item.rstrip('\n')

        if('-' in item):
            break

        print(quickSum(item))
    

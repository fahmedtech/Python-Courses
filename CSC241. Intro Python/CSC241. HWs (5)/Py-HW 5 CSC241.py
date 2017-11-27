'''
Python CSC241
HW 5 - 6/30/2016
'''

#HW 7

#Program 1:
'''
Write a function game() that teaches children how to add single-digit numbers.
The function should take an integer n as a parameter and ask the child to
answer n single-digit addition questions.  The numbers should be chosen
randomly from the range [0, 9] (that is including both 0 and 9).  The user will
enter the answer when prompted.  Your function should print 'Correct' for
correct answers and 'Incorrect' for incorrect answers.  After n questions,
the function should print the number of questions answered correctly.

>>> game(1)
4 + 6 = 10
Correct!
You got 1 correct answers out of 1.
>>> game(2)
9 + 4 = 13
Correct!
6 + 9 = 16
Incorrect!
You got 1 correct answers out of 2.
>>> game(3)
0 + 8 = 8
Correct!
1 + 2 = 3
Correct!
1 + 6 = 8
Incorrect!
You got 2 correct answers out of 3.
'''
#Run Module for Program to execute (F5)
#Type game(<integer>) - Name of Method in Shell to execute.

import random

def game(int_questions):
    _count = 0
    _questotal = 1

    while(_questotal <= int_questions):
        
        int_num1 = random.randrange(0, 10)
        int_num2 = random.randrange(0, 10)
        
        answer = int_num1 + int_num2

        inp_answer = eval(input("{} + {} = ".format(int_num1, int_num2)))                        
        _questotal += 1

        if(inp_answer == answer):
            _count += 1
            print("Correct!")
        else:
            print("Incorrect!")

    print("You got {} correct answers out of {}.".format(_count, int_questions))

#Program 2:
'''
Craps is a dice-based game played in many casinos.  Like blackjack,
a player plays against the house.  The game starts with the player throwing
a pair of standard, six-sided dice.  If the player rolls a total of 7 or 11,
the player wins.  If the player rolls a total of 2, 3, or 12, the player loses.
For all other roll values, the player will repeatedly roll the pair of dice
until either she/he rolls the initial value again (in which case she/he wins)
or 7 (in which case she/he loses).

a.  Write a function craps() that takes no parameters, simulates one game of
craps, and returns 1 if the player won and 0 if the player lost.  It should
also print a history of the rolls so that the player can verify that the
function is doing the right thing.

>>> craps()
Roll: 1 & 2 = 3
0
>>> craps()
Roll: 2 & 2 = 4
Roll: 4 & 6 = 10
Roll: 3 & 1 = 4
Roll: 5 & 3 = 8
Roll: 6 & 2 = 8
Roll: 2 & 1 = 3
0
>>> craps()
Roll: 2 & 5 = 7
1
'''
#Run Module for Program to execute (F5)
#Type craps() - Name of Method in Shell to execute.

import random

def craps():
    _total = 1

    while(_total > 0):

        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        diceTotal = dice1 + dice2
        
        print("Roll:", dice1, "&", dice2, '=', diceTotal)
        _total += 1

        if(diceTotal in (7,11)):
            return 1
        elif(diceTotal in (2,3,12)):
            return 0
             
'''
b.  Next, modify your function into one called quietCraps() that simply
returns 0 or 1 but does not display the results of the rolls.  It should
function exactly the same way as craps() but without printing any information.

>>> quietCraps()
0
>>> quietCraps()
1
>>> quietCraps()
1
>>> quietCraps()
1
>>> quietCraps()
0
'''
#Type quietCraps() - Name of Method in Shell to execute.

def quietCraps():

    while True:

        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        diceTotal = dice1 + dice2

        if(diceTotal in (7,11)):
            return 1
        elif(diceTotal in (2,3,12)):
            return 0
        
'''
c.  Finally, implement a function testCraps() that takes a positive integer n
as a parameter, simulates n games of craps using the quietCraps() function,
and returns the fraction of games the player won.

>>> testCraps(100)
0.67
>>> testCraps(1000)
0.646
>>> testCraps(10000)
0.6707
'''
#Type testCraps() - Name of Method in Shell to execute.

import random

def testCraps(int_numOfGames):
    _count = 0

    for i in range(int_numOfGames):
        if(quietCraps() == 1):
            _count += 1

    return _count / int_numOfGames

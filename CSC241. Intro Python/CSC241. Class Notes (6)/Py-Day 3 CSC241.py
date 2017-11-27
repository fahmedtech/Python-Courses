'''
Python CSC241
Day 3 - 6/17/2016
'''

'''
**Practice Iteration(s)

s = 'hello this is a string'
for item in s:
    print(item, end=' ')

>>> for i in range(len(s)):
    print(i, s[i])
0 h
1 e
2 l
...
16 s
17 t
18 r
19 i
20 n
21 g
'''

#Program 1: Find Vowels Index Locations
#Run Module for Program to execute (F5)
#Type VowelIndex() - Name of Method in Shell to execute.

def VowelIndex(str_word):
    for i in range(len(str_word)):
        if(str_word[i] in "aeiouAEIOU"):
           print(str_word[i], i, end=' ')

#Program 2: Return the Index of Target object <string, integer> from the List
#Run Module for Program to execute (F5)
#Type FindTarget() - Name of Method in Shell to execute.

'''
>>> FindTarget(5, [1,2,3,4,5])
4
'''

def FindTarget(obj_target, from_list):
    for i in range(len(from_list)):
        if(from_list[i] == obj_target):
            return i
    return -1

#Program 3: Check if List is sorted
#Run Module for Program to execute (F5)
#Type CheckSorted() - Name of Method in Shell to execute.

def CheckSorted(lst):
    for i in range(len(lst) - 1): #print(i, lst[i],lst[i+1])
        if(lst[i] > lst[i+1]):
            return False
    return True

#Program 4: FindAll Characters from the Word and return Index List
#Run Module for Program to execute (F5)
#Type FindAll() - Name of Method in Shell to execute.

'''
>>> FindAll('o', "Hideo Kojima")
[4, 7]
'''

def FindAll(str_char, str_word):
    index_list = []

    for i in range(len(str_word)):
        if(str_word[i] == str_char):
            index_list.append(i)
    return index_list


'''
Practice: 2D Table List Iteration

table = [[1,2,3],[4,5,6,7],[8,9,10]]
for row in table:
    for item in row:
        print(item, end=' ')
    print(
'''

#Program 5: Get 'X' Locations from the Map as Coordinations
#Run Module for Program to execute (F5)
#Type FindTreasures() - Name of Method in Shell to execute.

'''
>>> FindTreasures(treasure_maps)
['_____________________', '_____________________', '_____X_______________', '________X_____X______', '_____________________', '_X___________________', '_________X___________', '__________________X__']
[(2, 5), (3, 8), (3, 14), (5, 1), (6, 9), (7, 18)]
'''

treasure_maps='''
_____________________
_____________________
_____X_______________
________X_____X______
_____________________
_X___________________
_________X___________
__________________X__
'''

def FindTreasures(treasure_maps):

    lines = treasure_maps.split()
    print(lines)

    coordinations = []

    for i in range(len(lines)): #looping over index 0-7
        for j in range(len(lines[i])): #looping over chars
            if(lines[i][j] == 'X'):
               coordinations.append((i,j))
    return coordinations

#Program 6: Return Price of Pizza based on Size and Topping
#Run Module for Program to execute (F5)
#Type PizzaPrice(<string>, <int>) - Name of Method in Shell to execute.

'''
>>> PizzaPrice('Small',1)
12.75
>>> PizzaPrice('Medium',1)
16.25
'''

def PizzaPrice(str_size, int_toppings): #str_size[0].upper() == 'S'
    if(str_size[0] in ['S','s']):
        return 12 + .75 * int_toppings
    elif(str_size[0] in ['M','m']):
        return 15 + 1.25 * int_toppings
    else:
        return 17 + 1.50 * int_toppings

#Program 7: Print Words from Sentence of exact Length
#Run Module for Program to execute (F5)
#Type PrintWordsOfLength(<string>, <int>) - Name of Method in Shell to execute.

'''
>>> PrintWordsOfLength("This has four words", 4)
This four 
'''

def PrintWordsOfLength(str_sentence, int_length):
    wordsList = str_sentence.split()

    for item in wordsList:
        if(len(item) == int_length):
            print(item, end=" ")
    '''
    Practice: Get the Index from the List
    for i in range(len(wordsList)):
        if(i == int_length):
           print(wordsList[i])
    '''

#Program 8: Count the Capitals in a Sentence
#Run Module for Program to execute (F5)
#Type CountCapitals(<string>) - Name of Method in Shell to execute.

'''
>>> CountCapitals("This has Four Capital Letters")
4
'''

def CountCapitals(str_sentence):
    count = 0

    for char in str_sentence:
        if(char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            count += 1
    return count
    
#Program 9: Mutliply Two List and return a List of answers
#Run Module for Program to execute (F5)
#Type ListMulti(<list>, <list>) - Name of Method in Shell to execute.

'''
>>> list1 = [2,4]
>>> list2 = [1,2,3,4,5]
>>> ListMulti(list1, list2)
[2, 4, 6, 8, 10, 4, 8, 12, 16, 20]
'''

def ListMulti(list1, list2):
    answerList = []
    
    for i in list1:
        for j in list2:
            answerList.append(i * j)
    return answerList

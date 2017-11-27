'''
Python CSC241
MIDTERM Solutions
'''

#Program 1:

def pizzaPrice(str_size, int_toppings):
    str_size = str_size.strip()
    
    smallPizza = .75 * int_toppings + 12.0
    mediumPizza = 1.25 * int_toppings + 15.0
    largePizza = 1.50 * int_toppings + 17.0

    if(str_size[0].lower() == 's'):
        return smallPizza
    elif(str_size[0].lower() == 'm'):
        return mediumPizza
    elif(str_size[0].lower() == 'l'):
        return largePizza
    else:
        return "Invalid Input!"

    
#Program 2:

def wordsOfLength(str_words, int_length):
    wordList = str_words.split()

    for item in wordList:
        if(len(item) == int_length):
            print(item)


#Program 3:
    
def PrintBs(float_list):
    _retList = []

    for item in float_list:
        if(item >= 80 and item < 90):
            _retList.append(item)

    print(_retList)

            
#Program 4:

from string import ascii_uppercase

def countCaps(str_word):
    _count = 0

    for char in str_word:
        if(char in ascii_uppercase):
            _count += 1

    return _count
    

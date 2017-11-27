'''
Python CSC241
Practice 3

Contains Collections of Program
Run Module to execute (F5)
Type Method() - Name in Shell to execute.
'''

#Program 1:
'''
Not QUIET WORKING
>>> bubbleSort([5,4,3,1,2,3,1])
[1, 2, 3, 3, 4, 5, 1]
>>> bubbleSort([5,4,3,1,2,3,60])
[1, 2, 3, 3, 4, 5, 60]
'''

def bubbleSort(list_name):

    for i in range(len(list_name) -2, 0, -1):

        for j in range(i):

            if(list_name[j] > list_name[j+1]):

                list_name[j], list_name[j+1] = list_name[j+1], list_name[j]

    return list_name


#Program 2:
'''
>>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
>>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
>>> Add2DLists(t,s)
>>> for item in t:
	print(item)

	
[4, 8, 4, 5]
[5, 2, 10, 3]
[8, 4, 6, 6]
'''

def Add2DLists(lists1, lists2):

    _rows = len(lists1)
    _cols = len(lists1[0])

    for i in range(_rows):
        for j in range(_cols):
            lists1[i][j] += lists2[i][j]

#Program 3:
'''
>>> citiesList()
Enter City to Add in List: Chicago
Enter City to Add in List: Jeddah
Enter City to Add in List: Lahore
Enter City to Add in List: 
['Chicago', 'Jeddah', 'Lahore']

>>> citiesListV2()
Enter City:Chicago
Enter again a city:Jeddah
Enter again a city:Lahore
Enter again a city:
['Chicago', 'Jeddah', 'Lahore']

>>> citiesListV3()
Enter City to Add in List: chicago
Enter City to Add in List: jeddah
Enter City to Add in List: lahore
Enter City to Add in List: 
['chicago', 'jeddah', 'lahore']
'''
def citiesList():
    retList = []
    temp = True

    while(temp):
        inp_city = input("Enter City to Add in List: ")
        retList.append(inp_city)

        if(inp_city == ''):
            temp = False
            retList.pop()

    return retList

#This version contains different while loop
def citiesListV2():
    lst = []
    
    city = input('Enter City:')
    
    while city!= '':
        lst.append(city)
        city = input('Enter again a city:')
        
    return lst

#This version contains Half Loop - BETTER
def citiesListV3():
    retList = []

    while True:
        inp_city = input("Enter City to Add in List: ")

        if(inp_city == ''):
            return retList

        else:
            retList.append(inp_city)

#Program 4:
'''
>>> birthState('Ronald Wilson Reagan')
'Illinois'

REVERSING DICTIONARY
>>> states_dict = {'Barack Hussein Obama II':'Hawaii',
              'George Walker Bush':'Connecticut',
              'William Jefferson Clinton':'Arkansas',
              'George Herbert Walker Bush':'Massachussetts',
              'Ronald Wilson Reagan':'Illinois',
              'James Earl Carter, Jr':'Georgia'}

>>> newDict = dict( (val, key) for key, val in states_dict.items())

>>> newDict
{'Arkansas': 'William Jefferson Clinton', 'Illinois': 'Ronald Wilson Reagan',
 'Georgia': 'James Earl Carter, Jr', 'Massachussetts': 'George Herbert Walker Bush',
 'Hawaii': 'Barack Hussein Obama II', 'Connecticut': 'George Walker Bush'}
'''

def birthState(str_presName):
    'returns the birth state of the given president'
    
    states_dict = {'Barack Hussein Obama II':'Hawaii',
              'George Walker Bush':'Connecticut',
              'William Jefferson Clinton':'Arkansas',
              'George Herbert Walker Bush':'Massachussetts',
              'Ronald Wilson Reagan':'Illinois',
              'James Earl Carter, Jr':'Georgia'}
    
    return states_dict[str_presName]

#Program 5:
'''
>>> phonebook = {'(123)456-78-90':['Anna','Karenina'],
'(901)234-56-78':['Yu', 'Tsun'],
'(321)908-76-54':['Hans', 'Castorp']}

>>> LookupNum(phonebook)
Enter phone# in(xxx)xxx-xx-xx format: (123456-78-90
Number not in use.
Enter phone# in(xxx)xxx-xx-xx format: (123)456-78-90
['Anna', 'Karenina']
'''

def LookupNum(dict_phonebook):

    while True:
        inp_num = input("Enter phone# in(xxx)xxx-xx-xx format: ")

        if(inp_num in dict_phonebook):
            print(dict_phonebook[inp_num])

        else:
            print("Number not in use.")

#Program 6:
'''
>>> wordCountText("Hello Hello, Universe, cool? right? right! right.")
Hello    appears 2 time.
Universe appears 1 time.
cool     appears 1 time.
right    appears 3 time.
'''
import string

def wordCountText(str_words):
    wordsDict = {}
    
    transPunct = str_words.maketrans(string.punctuation, len(string.punctuation) * " ")
    newString = str_words.translate(transPunct)

    wordList = newString.split()
    
    for item in wordList:
        if(item in wordsDict):
            wordsDict[item] += 1
        else:
            wordsDict[item] = 1

    for item in wordsDict:
        print("{:8} appears {} time.".format(item, wordsDict[item])) 
        
#Program 7:
'''
>>> studentsList = ["gabriel", "david", "ilia", "gabriel", "pedro", "gabriel"]
>>> Frequency(studentsList)
{'pedro': 1, 'ilia': 1, 'david': 1, 'gabriel': 3}
'''

def Frequency(obj_list):
    itemsDict = {}

    for item in obj_list:
        if(item in itemsDict):
            itemsDict[item] += 1
        else:
            itemsDict[item] = 1

    return itemsDict

#Program 8:
'''
>>> phonebook = {('Anna','Karenina'):'(123)456-78-90',
('Yu', 'Tsun'):'(901)234-56-78',
('Hans', 'Castorp'):'(321)908-76-54'}

>>> InteractiveLookup(phonebook)
Enter First Name: Anna
Enter Last Name: Karenina
(123)456-78-90
Enter First Name: Yu
Enter Last Name: Tsun
(901)234-56-78
Enter First Name: 
Enter Last Name: 
Name Entered not Found!
'''

def InteractiveLookup(dict_phonebook):

    while True:
        inp_fname = input("Enter First Name: ")
        inp_lname = input("Enter Last Name: ")

        key_name = (inp_fname, inp_lname)

        if(key_name in dict_phonebook):
            print(dict_phonebook[key_name])
        else:
            print("Name Entered not Found!")
            

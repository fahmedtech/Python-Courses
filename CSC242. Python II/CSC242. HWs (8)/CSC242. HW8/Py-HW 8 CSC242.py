'''
Python CSC242
HW8 Solutions
'''

#Problem 1: Greater Common Denominator gcd(<int>, <int>)
'''
>>> gcd(5, 2)
1
>>> gcd(4, 2)
2
'''

def gcd(intx, inty):
    if(inty == 0):
        return intx

    return gcd(inty, intx % inty)

#Problem 2: binary(int) - Recursive
'''
>>> binary(0)
0
>>> binary(1)
1
>>> binary(3)
11
>>> binary(9)
1001
'''

def binary(int_n):
    'prints binary representation of int_n'

    if(int_n in [0,1]):
        print(int_n, end='')

    else:
        binary(int_n // 2)
        print(int_n % 2, end='')

#Problem 3: Class ContentParser()
'''
>>> getContent('http://www.nytimes.com')
The New York Times - Breaking News, World News & Multimediawindow.NREUM||
(NREUM={}),
'''

from html.parser import HTMLParser
from urllib.request import urlopen

class ContentParser(HTMLParser):

    def handle_data(self, data):
        print(data.strip(), end='')
#end of class

def getContent(url):
    content = urlopen(url).read().decode()
    cp_obj = ContentParser()
    cp_obj.feed(content)
    
#Problem 4: emails(<string>)
'''
>>> url = "http://www.impawards.com/intl/india/"
>>> content = urlopen(url).read().decode()
>>> emails(content)
[]

>>> url = "http://www.cdm.depaul.edu"
>>> content = urlopen(url).read().decode()
>>> emails(content)
['admission@cdm.depaul.edu', 'advising@cdm.depaul.edu', 'webmaster@cdm.depaul.edu', 'wwwfeedback@cdm.depaul.edu']
'''
from re import findall

def emails(content):
    'return list of email addresses contained in string content'
    dictionary = {}
    emailList = []

    regexPattern = '[\w\._]+@[\w_\.]+'
    duplicates = findall(regexPattern, content)

    for item in duplicates:
        if item not in dictionary:
            dictionary[item] = item
            emailList.append(item)

    return emailList

#Problem 5: spam(<string>, <int>)
'''
>>> url = "https://www.cdm.depaul.edu/Current%20Students/Pages/Dean'sList.aspx"
>>> spamDict = {}
>>> spam(url, 0)
>>> spamDict
{'advising@cdm.depaul.edu': 'advising@cdm.depaul.edu', 'wwwfeedback@cdm.depaul.edu': 'wwwfeedback@cdm.depaul.edu', 'admission@cdm.depaul.edu': 'admission@cdm.depaul.edu', 'webmaster@cdm.depaul.edu': 'webmaster@cdm.depaul.edu'}
'''
from ch11 import Collector

spamDict = {}

def spam(str_url, int_num):
    '''recursively, and up to recursive depth n, collects email addresse
       in WWW HTML documents starting at page wuth URL url'''

    global spamDict

    content = urlopen(str_url).read().decode()
    emailList = emails(content)

    for item in emailList:
        if(item not in spamDict):
            spamDict[item] = item

    if(int_num == 0):
        return

    c_obj = Collector(str_url)
    c_obj.feed(content)

    for item in c_obj.getLinks():
        try:
            spam(item, int_num -1)
        except:
            pass

##### T E S T I N G  S H E L L #####

if __name__ == "__main__":
    print("Problem 1")
    print(gcd(3,0))              # 3
    print(gcd(18,12))            # 6
    print(gcd(820930,2277093))   # 439

    print("\nProblem 2")
    binary(0);print()            # 0
    binary(1);print()            # 1
    binary(3);print()            # 11
    binary(9);print()            # 1001

'''
    print("\nProblem 3")
    getContent('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html')
                                 # Test pageHello WorldLink
                                 # to test2.htmlLink to test3.htmlParis Paris ParisTokyo

    print("\n\nProblem 4")
    url = 'http://reed.cs.depaul.edu/lperkovic/csc242/test2.html'
    content = urlopen(url).read().decode()
    print(emails(content))       # ['lperkovic@cs.depaul.edu']

    print("\nProblem 5")
    spam_dict = {}
    url = 'http://reed.cs.depaul.edu/lperkovic/csc242/test1.html'
    spam(url, 2)
    print(spam_dict.keys())      # dict_keys(['nobody@xyz.com', 'lperkovic@cs.depaul.edu'])
'''

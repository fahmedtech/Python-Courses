'''
Python CSC242
Final Practice Solutions
'''

#Problem 1:
'''
>>> obj = Mortgage().mainloop()
or
>>> Mortgage().mainloop()
'''

from tkinter import Frame, Entry, Button, Label, END, Tk

class Mortgage(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        
        Label(self, text='Loan Amount:').grid(row=0, column=0)
        Label(self, text='Interest Rate:').grid(row=1, column=0)
        Label(self, text='Loan Terms:').grid(row=2, column=0)
        
        self.amount = Entry(self)
        self.amount.grid(row=0, column=1)
        
        self.rate = Entry(self)
        self.rate.grid(row=1, column=1)
        
        self.terms = Entry(self)
        self.terms.grid(row=2, column=1)
        
        Button(self, text='Compute Mortgage', command=self.compute).grid(row=3 ,
                                                                    column=0)
        self.mortgage = Entry(self)
        self.mortgage.grid(row=3, column=1)


    def compute(self):
        _amount = float(self.amount.get())
        _rate = float(self.rate.get())/1200
        _terms = float(self.terms.get())
        
        _monthly = _amount *(_rate *(1+ _rate)** _terms)/((1+ _rate)** _terms -1)

        self.mortgage.delete(0,END)
        self.mortgage.insert(0, _monthly)

#Problem 2:
'''
another method to solve this
return lst[0]*prod(lst[1:])
'''

def prod(lst):

    if(len(lst) == 0):
        return 1

    lastItem = lst.pop()
    return lastItem * prod(lst)


#Problem 3:

from re import findall

def test(str_filename):

    ifile = open(str_filename)
    content = ifile.read()
    ifile.close()

    print("Exercise i: the number of times the string Frankenstein appears in the text:")
    print(len(findall('Frankenstein', content)), '\n')
    
    print("Exercise ii: the list of all different numbers appearing in the text")
    print(list(set(findall('\d+', content))), '\n') #expression for digits
    
    print("Exercise iii: the list of strings of the form 'horror of <lowercase string> <lowercase string>'")
    print(findall('horror\sof\s\w+\s\w+', content), '\n')

    print("Exercise iv: the sentences containing the word 'laboratory'")
    lst = findall('[\.\!\?][a-zA-Z\s\,\;\:\-]+laboratory[a-zA-Z\s\,\;\:\-]*[\.\!\?]', content)
    for item in lst:
        print(item[2:], '\n') #skip first 2

    
#Problem 4:
'''
>>> obj = Collector('http://www.impawards.com/intl/india/')
>>> content = urlopen(obj.url).read().decode().lower()
>>> obj.feed(content)

>>> obj.getLinks()
['http://www.impawards.com', 'http://www.impawards.com', ..]
'''

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.request import urljoin

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.arrLinks = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlinks in absolute format'

        if(tag == 'a'):
            for item in attrs:
                if(item[0] == 'href'):
                    absLink = urljoin(self.url, item[1])
                    
                    if(absLink[:4] == 'http'):
                        self.arrLinks.append(absLink)

    def getLinks(self):
        return self.arrLinks
'''
>>> d = {}
>>> search('http://www.impawards.com/intl/india/', d, 1)
>>> for key in d:
	print(key, d[key])

'''
def search(str_url, dict_name, int_num):
    'crawler - computes number of occurences of hyperlinks'

    content = urlopen(str_url).read().decode()
    obj_col = Collector(str_url)
    obj_col.feed(content)

    arrLinks = obj_col.getLinks()

    for item in arrLinks:
        if(item in dict_name):
            dict_name[item] += 1
        else:
            dict_name[item] = 1

    if(int_num > 0):
        for item in arrLinks:
            search(item, dict_name, int_num -1)

#Additional Problems - R E C U R S I O N S

#Program 1: Return copy of list in which every element has duplicate
#Run Module for Program to execute.
#Type Duplicate(<list>) - Name of Method in Shell to execute.
'''
>>> Duplicate([3,6,2])
[3, 3, 6, 6, 2, 2]
'''

def Duplicate(obj_list):

    if(len(obj_list) == 0):
        return obj_list

    lastItem = obj_list.pop()

    return Duplicate(obj_list) + [lastItem, lastItem]

#Program 2: Return the number of times 0 occurs in list
#Run Module for Program to execute.
#Type Zeros(<list>) - Name of Method in Shell to execute.
'''
>>> Zeros([0,2,3,45,4,5,5,0,0,0,5,4,41,4,8,6,4,0])
5
'''

def Zeros(num_list):

    if(len(num_list) == 0):
        return 0

    lastItem = num_list.pop()

    if(lastItem == 0):
        return Zeros(num_list) +1
    else:
        return Zeros(num_list)

#Program 3: Return number of items that matches in both list
#Run Module for Program to execute.
#Type Equals(<list>, <list>) - Name of Method in Shell to execute.
'''
>>> Equals([3,4,5],[3,8,9])
1
>>> Equals([3,4,5],[8,0,9])
0
'''

def Equals(listA, listB):

    if(len(listA) == 0):
        return 0

    lastItemA = listA.pop()
    lastItemB = listB.pop()

    if(lastItemA == lastItemB):
        return Equals(listA, listB) +1
    else:
        return Equals(listA, listB)


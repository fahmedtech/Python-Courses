'''
Python CSC242
Final Exam Solutions
'''

#Problem 1: GUI Widget Class - Increment()
'''
>>> Increment().mainloop()
'''


from tkinter import Tk, Frame, Entry, Button, LEFT, RIGHT, END

class Increment(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.entry = Entry(self, width=36)
        self.entry.grid(row=0, column=0)
        self.entry.insert(0,0)

        Button(self, text="Increment", command= self.compute).grid(
                row=0, column=1)

    def compute(self):
        inpVal = int(self.entry.get())
        self.entry.delete(0, END)

        inpVal += 1
        self.entry.insert(0, inpVal)

#Problem 2: oddCount(<list>) - Recursive

def oddCount(int_lst):

    if(len(int_lst) == 0):
        return 0

    else:
        return(int_lst[0] % 2 + oddCount(int_lst[1:]))
    
#Problem 3: Regular Expressions

from re import findall

def test(str_filename):

    ifile = open(str_filename)
    content = ifile.read()
    ifile.close()

    print("\nExercise i: words that end with string 'ible'")
    print(list(set(findall('[\w]+ible', content))))

    print("\nExercise ii: words that start with an upper case and end with letter y")
    print(list(set(findall('[A-Z][\w]*y', content)))) 

    print("\nExercise iii: expressions consisting of a word followed by the word 'death'")
    print(list(set(findall('[\w]+[\s]+death', content)))) 

#Problem 4: Web Crawler
'''
>>> url = 'http://www.impawards.com/intl/india/'
>>> obj = Collector(url)
>>> content = urlopen(obj.url).read().decode().lower()
>>> obj.feed(content)
>>> obj.getLinks()
['http://www.impawards.com', 'http://www.impawards.com', ..]
'''

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

class Collector(HTMLParser):
    'collects hyperlink urls into a list'

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.arrLinks = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlink urls in absolute format'

        if(tag == 'a'):
            for item in attrs:
                if(item[0] == 'href'):
                    absUrl = urljoin(self.url, item[1])

                    if(absUrl[:4] == 'http'):
                        self.arrLinks.append(absUrl)

    def getLinks(self):
        return self.arrLinks

'''
>>> webdir('http://www.addatoday.com/', 1,0)
'''
def webdir(str_url, int_depth, int_indent):
    print(int_indent * '    ', str_url)

    try:
        
        obj_parse = Collector(str_url)
        content = urlopen(str_url).read().decode()
        obj_parse.feed(content)

        arrLinks = obj_parse.getLinks()

        if(int_depth > 0):
            for item in set(arrLinks):
                webdir(item, int_depth -1, int_indent +1)

    except:
        pass
    

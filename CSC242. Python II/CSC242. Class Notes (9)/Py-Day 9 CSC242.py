'''
Python CSC242
Day 9 - 7/8/2016
'''

#Program 1: Counts Resource with URL the frequency of each topic in list
#Run Module for Program to execute (F5)
#Type news(<string>, <list>) - Name of Method in Shell to execute.
'''
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()

>>> news('http://www.nytimes.com',['police','president','attacks'])
police appears 46
president appears 4
attacks appears 9
'''

from urllib.request import urlopen

def news(str_url, lst_topics):

    _content = urlopen(str_url).read().decode().lower()

    for item in lst_topics:
        print(item, 'appears', _content.count(item))

#Class 1: MyHTMLParser() - Prints Tags indented by Depth
#Run Module for Program to execute (F5)
'''
>>> obj = MyHTMLParser()

>>> ifile = open('HTML DOCS/links.html')
>>> content = ifile.read()
>>> ifile.close()

>>> obj.feed(content)
html start
    body start
        h4 start
        h4 start
        a start
        a start
        h4 start
        h4 start
        a start
        a start
        h4 start
        h4 start
        a start
        a start
    body start
html start

############################################
>>> obj = MyHTMLParser()
>>> url = 'http://www.nytimes.com'
>>> content = urlopen(url).read().decode().lower()
>>> obj.feed(content)
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        if(tag not in ['br', 'p']):
            print('{}{} start'.format(self.indent*' ', tag))
            self.indent += 4

    def handle_endtag(self, tag):
        if(tag not in ['br', 'p']):
            self.indent -= 4
            print('{}{} end'.format(self.indent*' ', tag))
            
#Class 2: MyHTMLParser2() - Handling Data
#Run Module for Program to execute (F5)
'''
>>> obj = MyHTMLParser2()

>>> ifile = open('HTML DOCS/links.html')
>>> content = ifile.read()
>>> ifile.close()

>>> obj.feed(content)

Absolute HTTP link

Absolute link to Google

Relative HTTP link

Relative link to test.html.

mailto scheme

Click here to email me.

#####################################################

>>> obj = MyHTMLParser2()

>>> url = 'http://www.nytimes.com'
>>> content = urlopen(url).read().decode().lower()
>>> obj.handle_data(content)
<!doctype html>

#####################################################

Testing Method:
>>> getContent('http://www.twitter.com')
'''

from html.parser import HTMLParser
from urllib.request import urlopen

class MyHTMLParser2(HTMLParser):

    def handle_data(self, data):
        print(data)

#getContent - Calls on MyHTMLParser2

def getContent(str_url):
    parse_obj = MyHTMLParser2()

    _response = urlopen(str_url).read().decode()
    _newRes = parse_obj.feed(_response)

    print(_newRes, end=' ')

            
           
    

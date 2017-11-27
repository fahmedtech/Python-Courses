'''
Python CSC242
Day 8 - 7/8/2016

**CONCEPT - Working with Website Parsing
'''

#Program 1: Return Content of Resource from Url as String
#Run Module for Program to execute (F5)
#Type getSource(<string>) - Name of Method in Shell to execute.
'''
>>> getSource('http://www.fb.com/')
'<!DOCTYPE html>\n<html lang="en" id="facebook" class="no_js">\n<head><meta charset="utf-8" />
'''

from urllib.request import urlopen

def getSource(str_url):

    _response = urlopen(str_url)
    content = _response.read()
    return content.decode()

#Class 1: LinkParser()
#Print Values of href attributes in anchor start tags
#Run Module for Program to execute (F5)
'''
>>> ifile = open('HTML DOCS/links.html')
>>> content = ifile.read()

>>> obj = LinkParser()
>>> obj.feed(content)
http://www.google.com
test.html
mailto:me@example.net
'''

from html.parser import HTMLParser

class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        if(tag == 'a'):

            for item in attrs:
                if(item[0] == 'href'):
                    print(item[1])

#Class 2: Collector()
#Collects hyperlinks URLs into a List
#Run Module for Program to execute (F5)
'''
>>> url = 'http://www.w3.org/Consortium/mission.html'
>>> response = urlopen(url)
>>> content = response.read().decode()

>>> obj = Collector(url)
>>> obj.feed(content)

>>> obj.getLinks()
['http://www.w3.org/', 'http://www.w3.org/standards/',  ..]
>>> obj.getData()
'\nW3C Mission\n     @import url("/2008/site/css/advanced");\n\n

>>> obj.handle_data('www') #adds 'www' text at end of html file
'''

from urllib.parse import urljoin
from html.parser import HTMLParser

class Collector(HTMLParser):

    #constructor
    def __init__(self, url):

        HTMLParser.__init__(self)
        self.url = url
        self.linkArray = []

        self.text = ''

    #overriding other methods
        
    def handle_starttag(self, tag, attrs):

        if(tag == 'a'):
            for item in attrs:
                if(item[0] == 'href'):

                    _absURL = urljoin(self.url, item[1])
                    
                    if(_absURL[:4] == 'http'):
                        self.linkArray.append(_absURL)

    def handle_data(self, data):
        self.text += data

    def getLinks(self):
        return self.linkArray

    def getData(self):
        return self.text
        
#Program 2:
''' Print Frequency of Every Word in Web Page Url and Print and Return
the list of http links, in absolute format'''
#Run Module for Program to execute (F5)
#Type Analyze(<string>) - Name of Method in Shell to execute.
'''
>>> Analyze('http://reed.cs.depaul.edu/lperkovic/one.html')

Visiting http://reed.cs.depaul.edu/lperkovic/one.html

URL                                           word       count
http://reed.cs.depaul.edu/lperkovic/one.html  Paris          5
http://reed.cs.depaul.edu/lperkovic/one.html  Beijing        3
http://reed.cs.depaul.edu/lperkovic/one.html  Chicago        5

URL                                           link      
http://reed.cs.depaul.edu/lperkovic/one.html  http://reed.cs.depaul.edu/lperkovic/two.html
http://reed.cs.depaul.edu/lperkovic/one.html  http://reed.cs.depaul.edu/lperkovic/three.html
['http://reed.cs.depaul.edu/lperkovic/two.html', 'http://reed.cs.depaul.edu/lperkovic/three.html']
'''

def Analyze(str_url):
    print('\n\nVisiting', str_url)

    #obtaining links from webpage
    _content = urlopen(str_url).read().decode()
    _objCollect = Collector(str_url)
    _objCollect.feed(_content)

    arrayUrl = _objCollect.getLinks()

    #compute word frequencies
    _content = _objCollect.getData()
    _freq = Frequency(_content)
    
    #print the frequency of every text data word in web page
    print('\n{:45} {:10} {:5}'.format('URL', 'word', 'count'))
    
    for word in _freq:
        print('{:45} {:10} {:5}'.format(str_url, word, _freq[word]))

    # print the http links found in web page
    print('\n{:45} {:10}'.format('URL', 'link'))
    
    for link in arrayUrl:
        print('{:45} {:10}'.format(str_url, link))

    return arrayUrl
    
#Frequency Program
from re import findall

def Frequency(str_content):
    _wordsDict = {}
    
    _pattern = '[a-zA-Z]+'
    _words = findall(_pattern, str_content)

    for item in _words:
        if(item in _wordsDict):
            _wordsDict[item] += 1
        else:
            _wordsDict[item] = 1

    return _wordsDict
    
#Program 3: Crawlers - Extends on Analyze()
#Run Module for Program to execute (F5)
'''
>>> RCrawl('http://reed.cs.depaul.edu/lperkovic/one.html')

>>> RCrawlExtended('http://reed.cs.depaul.edu/lperkovic/one.html')

Visiting http://reed.cs.depaul.edu/lperkovic/one.html

URL                                           word       count
http://reed.cs.depaul.edu/lperkovic/one.html  Beijing        3
http://reed.cs.depaul.edu/lperkovic/one.html  Chicago        5
http://reed.cs.depaul.edu/lperkovic/one.html  Paris          5

URL                                           link      
http://reed.cs.depaul.edu/lperkovic/one.html  http://reed.cs.depaul.edu/lperkovic/two.html
http://reed.cs.depaul.edu/lperkovic/one.html  http://reed.cs.depaul.edu/lperkovic/three.html


Visiting http://reed.cs.depaul.edu/lperkovic/two.html
'''

def RCrawl(str_url):
    '''Warning! Infinite Looping'''

    arrLinks = Analyze(str_url)

    for item in arrLinks:
        try:
            RCrawl(str_url)
        except:
            pass

#Better Version of the Crawler Program
_visited = set()
def RCrawlExtended(str_url):
    
    global _visited
    _visited.add(str_url)

    arrLinks = Analyze(str_url)

    for item in arrLinks:
        if(item not in _visited):
            try:
                RCrawlExtended(item)
            except:
                pass

#Class 3: Crawler() - Uses Analyze() Method
'''
>>> obj = Crawler()
>>> obj.crawl('http://reed.cs.depaul.edu/lperkovic/one.html')


Visiting http://reed.cs.depaul.edu/lperkovic/one.html

URL                                           word       count
http://reed.cs.depaul.edu/lperkovic/one.html  Chicago        5
http://reed.cs.depaul.edu/lperkovic/one.html  Paris          5
http://reed.cs.depaul.edu/lperkovic/one.html  Beijing        3

URL                                           link      
http://reed.cs.depaul.edu/lperkovic/one.html  http://reed.cs.depaul.edu/lperkovic/two.html
http://reed.cs.depaul.edu/lperkovic/one.html  http://reed.cs.depaul.edu/lperkovic/three.html
'''
class Crawler:

    def __init__(self):
        self._visited = set()

    def crawl(self, str_url):

        _arrLinks = Analyze(str_url)
        self._visited.add(str_url)

        for item in _arrLinks:
            if(item not in self._visited):
                try:
                    self.Crawl(str_url)
                except:
                    pass

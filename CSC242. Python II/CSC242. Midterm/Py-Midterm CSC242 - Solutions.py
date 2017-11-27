'''
Python CSC242
MIDTERM Solutions
'''

#Program 1: fileLength(<string>)

def fileLength(str_filename):

    try:
        ifile = open(str_filename, 'r')
        _len = len(ifile.read())
        ifile.close()

        return _len
    
    except FileNotFoundError:
        print('File', str_filename, 'not found.')

#Program 2: Class - Marsupial()

class Marsupial:

    def __init__(self):
        self.marsupialList = []

    def put_in_pouch(self, item):
        self.marsupialList.append(item)

    def pouch_contents(self):
        return self.marsupialList

#Program 3: Class Kangaroo() extends Marsupial()

class Kangaroo(Marsupial):

    def __init__(self, _x = 0, _y = 0):
        Marsupial.__init__(self)
        self.x = _x
        self.y = _y

    def jump(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        retVal = "I am a Kangaroo located at coordinates ({},{})".format(
                    self.x, self.y)
        return retVal

#Program 4: Class myStr() extends str()

class myStr(str):

    def __init__(self, str_word):
        self.word = str_word

    def __add__(self, str_word):
        return len(self) + len(str_word)

    def __mul__(self, str_word):
        return len(self) * len(str_word)
    

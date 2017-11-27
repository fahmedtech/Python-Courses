'''
Python CSC241
Day 6 - 6/22/2016
'''

'''
SHELL Print Practice
>>> print(2,3,4)
2 3 4
>>> print(2,3,4,sep=':')
2:3:4
>>> print(2,3,4,sep=':',end='')

**Concept Files input/output

when processing a file
    - open it
    - read and or/ write to file
    - close the file

File Objects
    - .open(<filename>, <mode>)
    - opens a file in current directory
    - returns a file object

Modes
    - 'r'ead
    - 'w'rite
    - 'a'ppend
    - close()

File Methods
    - all reads start at cursor (current loc)
    - read() - read to end of file, returns a string
    - readline() - reads through next '\n', returns a string
    - readlines() - reads to eof, returns a list of strings!
    - write(s) - write string s to file
    - close() - closes the file

Example 1. Practice Reading File in Shell

>>> open('example.txt')
<_io.TextIOWrapper name='example.txt' mode='r' encoding='cp1252'>

**Read whole File as a single String
>>> infile = open('Py-Day 6 CSC241 - ex.txt','r')
>>> infile.read()

**Read a single Line from File
>>> infile = open('Py-Day 6 CSC241 - ex.txt','r')
>>> line = infile.readline()
>>> line
'This is a file with some \n'
>>> infile.close()

**Read all Lines at once from File (as a List)
>>> infile = open('Py-Day 6 CSC241 - ex.txt','r')
>>> infile = open('Py-Day 6 CSC241 - ex.txt', 'r')
>>> lines = infile.readlines()
>>> lines
['This is a file with some \n', 'text in it.\n', '\n', 'There are numbers in this file too 123.\n', '\n', 'FGS']
>>> infile.close()

**Iterating over a File
>>> infile = open('Py-Day 6 CSC241 - ex.txt', 'r')
>>> for lines in infile:
	print(lines)

This is a file with some 
text in it.
There are numbers in this file too 123.
FGS
>>> infile.close()

Example 2. Practice Writing to a File

>>> outfile = open('Py-Day 6 CSC241 - out.txt','w')
>>> outfile.write('put this stuff in the file')
26
>>> outfile.write('more stuff')
10
>>> outfile.close()

*Reading the Newly written File
>>> open('Py-Day 6 CSC241 - out.txt').read()
'put this stuff in the filemore stuff'

>>> open('output.txt').read().split()
['put', 'this', 'stuff', 'in', 'the', 'filemore', 'stuff']
'''

#Program 1: Get Number of Chars from the File
#Run Module for Program to execute (F5)
#Type NumChars(<string>) - Name of Method in Shell to execute.

'''
>>> NumChars('Py-Day 6 CSC241 - out.txt')
36
>>> NumChars('Py-Day 6 CSC241 - ex.txt')
83
'''

def NumChars(file_name):

    infile = open(file_name, 'r')
    content_str = infile.read()
    infile.close()

    return len(content_str)


#Program 2: Strip '#' Comments from the Input File
#Run Module for Program to execute (F5)
#Type StripComments(<string>, <string>) - Name of Method in Shell to execute.

'''
>>> StripComments('Py-Day 6 CSC241 - commented.py','Py-Day 6 CSC241 - uncommented.txt')
'''

def StripComments(inp_file, out_file):
    ''' strip '#' comment lines from inp_file'''

    infile = open(inp_file, 'r')
    lines = infile.readlines()
    infile.close()

    outfile = open(out_file, 'w')

    for item in lines:
        #outfile.write(item)

        if('#' not in item):
            outfile.write(item)
        else:
            comment_index = item.find('#')
            outfile.write(item[:comment_index] + '\n')

    outfile.close()

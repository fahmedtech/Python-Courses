'''
Python CSC242
TempConvert Class()
'''

class TempConvert(object):

    def main():
        _fahr = eval(input("Enter Temp in F: "))
        _cel = (_fahr -32) * 5.0/9.0

        print("Temperature in C: {:5.1f}".format(_cel))

if(__name__ == '__main__'):
    TempConvert.main()

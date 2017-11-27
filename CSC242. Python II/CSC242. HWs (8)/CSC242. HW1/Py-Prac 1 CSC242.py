'''
Python CSC242
Practice Problems - D I C T I O N A R Y
'''

#Program 1: Age Dictionary
#Run Module for Program to execute (F5)

dict_age = {21:'Gabriel', 19:'Pedro'}

inp_age = int(eval(input(("Provide Age: "))))

for keys in dict_age.keys():
    if(keys == inp_age):
        keyName = dict_age[keys]

        print(keyName)
               

#Program 2: Mirror Characters
#Run Module for Program to execute (F5)
#Type Mirror(<string>) - Name of Method in Shell to execute.
'''
>>> Mirror('b')
d
>>> Mirror('d')
b
'''

def Mirror(str_char):
    mirDict ={'b':'d', 'd':'b', 'o':'o', 'i':'i', 'v':'v', 'w':'w',
              'x':'x', 'p':'q', 'q':'p'}

    for keys in mirDict.keys():
        if(keys == str_char):
            outVal = mirDict[keys]

            print(outVal)

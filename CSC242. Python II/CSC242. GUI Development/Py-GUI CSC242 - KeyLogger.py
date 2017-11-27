'''
Python CSC242
GUI Development

'''
#KeyLogger GUI
#Run Module for Program to execute (F5)

from tkinter import Tk, Text, BOTH

def recordKey(event):
    '''event handling function for key press event;
       input event is of type tkinter.Event'''

    print("Key Pressed = {}".format(event.keysym))

#GUI
root = Tk()

#textbox 
text = Text(root,
            width=20,  # set width to 20 characters
            height=5)  # set height to 5 rows of characters

# Bind a key press event with the event handling function record()
text.bind('<KeyPress>', recordKey)

# widget expands if the master does
text.pack(expand=True, fill=BOTH)

root.mainloop()

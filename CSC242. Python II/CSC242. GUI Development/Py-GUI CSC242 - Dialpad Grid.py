'''
Python CSC242
GUI Development

'''
#Drawing Phone Dialpad Grid
#Run Module for Program to execute (F5)

from tkinter import Tk, Label, RAISED

root = Tk()

labelList = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]

for lists in range(4):
    for char in range(3):

        label = Label(root, relief=RAISED,      # raised border
                      padx=10,                  # make label wide
                      text=labelList[lists][char]) # label text

        label.grid(row=lists, column=char)

root.mainloop()


'''
Python CSC242
GUI Development

'''
#Picture and Label
#Run Module for Program to execute (F5)

from tkinter import Tk, Label, PhotoImage, BOTH, RIGHT, LEFT

root = Tk()

label1 = Label(root, text='Peace & Love', background='black',
               width=20, height=5, foreground='white',
               font=('Helvetica', 18, 'italic'))
label1.pack(side=LEFT)

photo = PhotoImage(file='Py-GUI CSC242 - Pic - peace.gif')
label2 = Label(root, image=photo)
label2.pack(side=RIGHT, expand=True, fill=BOTH)

root.mainloop()

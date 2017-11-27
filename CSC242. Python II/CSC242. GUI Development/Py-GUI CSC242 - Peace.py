'''
Python CSC242
GUI Development

'''
#One Picture in GUI
#Run Module for Program to execute (F5)

from tkinter import Tk, Label, PhotoImage

root = Tk()

# transform GIF image to a format tkinter can display     
photo = PhotoImage(file='Py-GUI CSC242 - pic - peace.gif')

peace = Label(master=root,
              image=photo,
              width=300,   # width of label, in pixels
              height=180)  # heigh of label, in pixels

peace.pack()
root.mainloop()

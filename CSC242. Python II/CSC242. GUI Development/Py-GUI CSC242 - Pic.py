'''
Python CSC242
GUI Development

'''
#Pack Pictures in GUI
#Run Module for Program to execute (F5)

from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE

# GUI illustrates widget constructor options and method pack()
root = Tk()

# label with text "Peace begins with a smile."
text = Label(root,                                              
             font=('Helvetica', 16, 'bold italic'),           
             foreground='white',   # letter color          
             background='black',   # background color         
             padx=25,  # widen label 25 pixels left and right 
             pady=10,  # widen label 10 pixels up and down    
             text='Peace begins with a smile.')
text.pack(side=BOTTOM)

# label with peace symbol image
peace = PhotoImage(file='Py-GUI CSC242 - Pic - peace.gif')
peaceLabel = Label(root, borderwidth=3,  # label border width
                   relief=RIDGE,         # label border style
                   image=peace)
peaceLabel.pack(side=LEFT)

# label with smiley face image
smiley = PhotoImage(file='Py-GUI CSC242 - Pic - smiley.gif')
smileyLabel = Label(root, image=smiley)
smileyLabel.pack(side=RIGHT)        

root.mainloop()

from tkinter import *

print('Hello World')


#Create the root widget, where everything is put
#Create and the to display

root = Tk()

#Creating a lablel widger
mylabel1 = Label(root, text='Hello World')
mylabel2 = Label(root, text='Soy Alan... de nuevo')


#Shoving in onto the screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)

root.mainloop()

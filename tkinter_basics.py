from tkinter import *

#Create the root widget, where everything is put
#Create and the to display

root = Tk()

#Function that gets called with button
def myClick():
    mylabel3 = Label(root, text='Hello World')
    mylabel3.grid(row=1, column=1)

#Creating a lablel widger
mylabel1 = Label(root, text='Hello World')
mylabel2 = Label(root, text='Soy Alan... de nuevo')
myButton=Button(root, text="Buen clickeo", padx=50,pady=60, command = myClick)


#Shoving in onto the screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)
myButton.grid(row=2,column=0)



root.mainloop()

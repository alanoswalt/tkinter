from tkinter import *

#Create the root widget, where everything is put
#Create and the to display

root = Tk()

#Function that gets called with button
def myClick():
    mylabel3 = Label(root, text=e.get())
    mylabel3.grid(row=1, column=1)

#Creating a lablel widger
mylabel1 = Label(root, text='Hello World')
mylabel2 = Label(root, text='Soy Alan... de nuevo')

#Creating buttons
myButton=Button(root, text="Buen clickeo", padx=50,pady=60, command = myClick)

#Creating entries or texboxes
e=Entry(root, bg='blue')

e.get() #This gets the value in the textbox
e.insert(0, 'Random text') #This allows to enter random text in the textbox

#Shoving in onto the screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)

e.grid(row=0, column=2)



root.mainloop()

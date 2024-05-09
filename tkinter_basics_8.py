from tkinter import *

#SLIDERS

root = Tk()
root.title('SLIDER')

root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/image_view/bicycle.ico') #add icons to the window


def update():
    mylablel=Label(root, text=var.get())
    mylablel.pack()

#var = IntVar() creates a tikter string value
var = StringVar() #creates a tikter string value
c = Checkbutton(root, text="Check this if your name is Alan", variable=var, onvalue="On", offvalue="Off") #value of the on and offs
c.deselect() #resets a value
c.pack()

myButton = Button(root, text="Click", command=update)
myButton.pack()

#mylablel=Label(root, text=str(var.get()))
#mylablel.pack()

#DROP DOWN MENU
varMenu = StringVar()
varMenu.set("Dia")
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
drop = OptionMenu(root, varMenu, *dias)
drop.pack()


root.mainloop() 
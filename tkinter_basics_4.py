#frames
from tkinter import *
from PIL import ImageTk, Image #Manage images

#Frames separate section from the rest of the code, 
# one can put elements in frame and the frame in root

root = Tk()
root.title('Frames')

root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/image_view/bicycle.ico') #add icons to the window

#----------FRAMES------------#
frame= LabelFrame(root, text='This is my frame', padx=50, pady=50) #size of the widget
frame.pack(padx=100, pady=100)

b2= Button(frame, text='Click here t00')
b2.grid(row=0, column=2) #Frames also have grids so you can put them in a grid

b= Button(frame, text='Click here')
b.grid(row=0, column=4) #Frames also have grids so you can put them in a grid


button_quit=Button(root, text='Exit', command=root.quit) #exit program
button_quit.pack() 

#----------FRAMES------------#

#----------Radio butons------------#
#Buttons like 

#r=IntVar()
#r=StringVar


def chage_label(num):
    myLabel=Label(root, text=num).pack()

#Variables helps change the current value of r in this case
#Radiobutton(root, text='Option 1', variable=r, value=1,command= lambda: chage_label(r.get())).pack()
#Radiobutton(root, text='Option 2', variable=r, value=2,command= lambda: chage_label(r.get())).pack()


def chage_pizza(num):
    myLabel=Label(root, text=num).pack()


MODES = [
    ('Pep','Pep'),
    ('Che','Che'),
    ('Msh','Msh'),
    ('Oni','Oni'),
]

pizza = StringVar()
pizza.set('Pep')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode, command= lambda: chage_label(pizza.get())).pack()





myLabel=Label(root, text=pizza.get()).pack()


root.mainloop()
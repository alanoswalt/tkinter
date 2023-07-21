#frames and new windows
from tkinter import *
from PIL import ImageTk, Image #Manage images
from tkinter import messagebox

#Frames separate section from the rest of the code, 
# one can put elements in frame and the frame in root

root = Tk()
root.title('Frames')

root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/image_view/bicycle.ico') #add icons to the window

def pupop():
    #messagebox.showinfo('Que pedooooo', 'Hola')
    #messagebox.showwarning('Que pedooooo', 'Hola')
    #messagebox.showerror('Que pedooooo', 'Hola')
    #messagebox.askquestion('Que pedooooo', 'Hola') #this returns a yes and no
    #messagebox.askokcancel('Que pedooooo', 'Hola') #this returns a 1 and 0
    response = messagebox.askyesno('Que pedooooo', 'Hola')
    Label(root, text=response).pack()


Button(root, text='Click please', command=pupop).pack()


root.mainloop()
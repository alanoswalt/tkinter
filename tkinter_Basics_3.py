#images
from tkinter import *
from PIL import ImageTk, Image #Manage images

#Create the root widget, where everything is put
#Create and the to display

root = Tk()
root.title('Images')

root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/bicycle.ico') #add icons to the window


button_quit=Button(root, text='Exit', command=root.quit) #exit program
button_quit.pack()


my_img = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/mario.jpg'))
my_label=Label(image=my_img)
my_label.pack()

root.mainloop()
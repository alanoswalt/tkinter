#images
from tkinter import *
from PIL import ImageTk, Image #Manage images

#Create the root widget, where everything is put
#Create and the to display

root = Tk()
root.title('Images')
root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/bicycle.ico') #add icons to the window

def forward():
    global my_label
    global current_image
    if current_image < 3:
        my_label.grid_forget() #to remove an image from the label
        my_label=Label(image=image_list[current_image+1])
        my_label.grid(row=0, column=0,columnspan=3)
        current_image=current_image+1


def back():
    global my_label
    global current_image
    if current_image > 0:
        my_label.grid_forget() #to remove an image from the label
        my_label=Label(image=image_list[current_image-1])
        my_label.grid(row=0, column=0,columnspan=3)
        current_image=current_image-1





#Images
my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/mario.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/luigi.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/peach.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/zelda.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4]
global current_image
current_image=0
my_label=Label(image=my_img1)

#Buttons
button_quit=Button(root, text='Exit', padx=50, command=root.quit) #exit program
button_left=Button(root, text="<<<", padx=50, command=lambda: back())
button_right=Button(root, text=">>>", padx=50, command=lambda: forward())


#Display all 
my_label.grid(row=0, column=0,columnspan=3)
button_left.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_right.grid(row=1, column=2)

root.mainloop()
#images
from tkinter import *
from PIL import ImageTk, Image #Manage images

#Create the root widget, where everything is put
#Create and the to display

root = Tk()
root.title('Images')
root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/image_view/bicycle.ico') #add icons to the window

def forward():
    global my_label
    global my_label_txt
    global current_image
    global my_label_status
    if current_image < (len(image_list)-1):
        #Change image
        my_label.grid_forget() #to remove an image from the label
        my_label=Label(root, image=image_list[current_image+1])
        my_label.grid(row=0, column=0,columnspan=3)
        
        #Change description
        my_label_txt.grid_forget() #to remove an image from the label
        my_label_txt=Label(root, text=image_text[current_image+1])
        my_label_txt.grid(row=1, column=0,columnspan=3)
        
        current_image=current_image+1
        #Update status
    else: #Return to start 
        #Change image
        my_label.grid_forget() #to remove an image from the label
        my_label=Label(root, image=image_list[0])
        my_label.grid(row=0, column=0,columnspan=3)

        #Change description
        my_label_txt.grid_forget() #to remove an image from the label
        my_label_txt=Label(root, text=image_text[0])
        my_label_txt.grid(row=1, column=0,columnspan=3)

        current_image=0
    
    my_label_status.grid_forget() #to remove an image from the label
    my_label_status=Label(root, text= str(current_image+1)+' image of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    my_label_status.grid(row=3, column=0, columnspan=3, sticky=W+E)

def back():
    global my_label
    global my_label_txt
    global current_image
    global my_label_status
    if current_image > 0:
        #Change image
        my_label.grid_forget() #to remove an image from the label
        my_label=Label(image=image_list[current_image-1])
        my_label.grid(row=0, column=0,columnspan=3)

        #Change description
        my_label_txt.grid_forget() #to remove an image from the label
        my_label_txt=Label(root, text=image_text[current_image-1])
        my_label_txt.grid(row=1, column=0,columnspan=3)

        current_image=current_image-1

    else: #Go to end
        #Change image
        my_label.grid_forget() #to remove an image from the label
        my_label=Label(image=image_list[len(image_list)-1])
        my_label.grid(row=0, column=0,columnspan=3)

        #Change description
        my_label_txt.grid_forget() #to remove an image from the label
        my_label_txt=Label(root, text=image_text[len(image_list)-1])
        my_label_txt.grid(row=1, column=0,columnspan=3)

        current_image=len(image_list)-1
    
    my_label_status.grid_forget() #to remove an image from the label
    my_label_status=Label(root, text= str(current_image+1)+' image of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    my_label_status.grid(row=3, column=0, columnspan=3, sticky=W+E)

#Images
my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/image_view/mario.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/image_view/luigi.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/image_view/peach.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('C:/Users/alan_/Documents/tkinter/tkinter/image_view/zelda.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4]
image_text = ['This is Mario', 'This is Luigi','This is Peach','This is Zelda']
list_len=len(image_list)
global current_image
current_image=0

#Labels
my_label=Label(image=image_list[0])
my_label_txt = Label(root, text=image_text[0])
#bd is border
my_label_status = Label(root, text= '1 image of '+str(list_len), bd=1, relief=SUNKEN, anchor=E) #anchot in a direction

#Buttons
button_quit=Button(root, text='Exit', padx=50, command=root.quit) #exit program
button_left=Button(root, text="<<<", padx=50, command=lambda: back())
button_right=Button(root, text=">>>", padx=50, command=lambda: forward())


#Display all 
my_label.grid(row=0, column=0,columnspan=3)
my_label_txt.grid(row=1, column=0,columnspan=3)
my_label_status.grid(row=3, column=0, columnspan=3, sticky=W+E) #Sticky is for strech from left to right
button_left.grid(row=2, column=0)
button_quit.grid(row=2, column=1)
button_right.grid(row=2, column=2)

root.mainloop()
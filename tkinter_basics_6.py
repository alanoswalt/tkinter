#open new windows and files
from tkinter import *
from PIL import ImageTk, Image #Manage images
from tkinter import filedialog

#Create new windows

root = Tk()
root.title('Windows')

root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/image_view/bicycle.ico') #add icons to the window

#This returns the location 
#root.filename = filedialog.askopenfilename(initialdir = '/image_view', title = 'Select file', filetypes = ("jpg files" , "*.jpg")) 

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "C:/Users/alan_/Documents/tkinter/tkinter/image_view/", title = "Select file", filetypes = (("jpg files","*.jpg"),("all files","*.*")))
    myLable=Label(root, text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    myImageLabel=Label(image=my_image).pack()


bu=Button(root, text='Open file', command=open).pack()

#Open different windows
#def open():
    #Inside here variables are locals, issues with images
#    top=Toplevel()
#    mylabel = Label(top, text='Que pedo').pack()
#    top.title('Second Window')
#    closeButton=Button(top, text='Close me', command=top.destroy).pack()


#goodButton=Button(root, text='Open window', command=open).pack()



root.mainloop()
from tkinter import *

#SLIDERS

root = Tk()
root.title('SLIDER')

root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/image_view/bicycle.ico') #add icons to the window
root.geometry("400x400") #mage window bigger
#Function that gets called with button
def slider(num):
    mylabel = Label(root, text=num)
    mylabel.pack()

#Creating s slider
vertical = Scale(root, from_=0, to=100) # is not good to pack it in the same line, this has to happend in different line
horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
button = Button(root, text="Save num", command=lambda: slider(horizontal.get())).pack()


horizontal.pack()
vertical.pack()




root.mainloop()
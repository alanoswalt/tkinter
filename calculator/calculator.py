from tkinter import *


root = Tk()
root.title('Calculator')


def calculate(sign):
    if sign == '+':
        result = num1+num2

    if sign == '-':
        result = num1+num2
    if sign == '+':
        result = num1+num2
    if sign == '+':
        result = num1+num2
    if sign == '+':
        result = num1+num2

operation = ''

def button_click(button):
    #textbox.delete(0, END)
    if isinstance(button, int):
        current=textbox.get()
        textbox.delete(0, END)
        textbox.insert(0, str(current)+str(button))
    #elif button=='c':
    #    textbox.delete(0, END)

def button_clear():
    #textbox.delete(0, END)
    textbox.delete(0, END)

def button_add():
    first_number=textbox.get()
    global f_num
    f_num = int(first_number)
    textbox.delete(0, END)


def button_equal():
    first_number=f_num
    second_number=int(textbox.get())
    textbox.delete(0, END)
    result = first_number+second_number
    textbox.insert(0,result)



#textbox
textbox=Entry(width=35, borderwidth=5)

#buttons
button9=Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button8=Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button7=Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button6=Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button5=Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button4=Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button3=Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button2=Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button1=Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button0=Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
buttonEq=Button(root, text="=", padx=20, pady=20, command=lambda: button_equal())
buttonPlus=Button(root, text="+", padx=20, pady=20, command=lambda: button_add())
ButtonMinus=Button(root, text="-", padx=20, pady=20, command=lambda: button_click('-'))
buttonDiv=Button(root, text="/", padx=20, pady=20, command=lambda: button_click('/'))
buttonMult=Button(root, text="*", padx=20, pady=20, command=lambda: button_click('*'))
buttonDot=Button(root, text=".", padx=20, pady=20, command=lambda: button_click('.'))

buttonClear=Button(root, text="Clear", padx=80 ,pady=20, command=lambda: button_clear())


#Buttons in screen
textbox.grid(row=0,column=0,columnspan=4)#esto ultimo toma el tamaño de las columnas
button9.grid(row=1,column=2)
button8.grid(row=1,column=1)
button7.grid(row=1,column=0)
button6.grid(row=2,column=2)
button5.grid(row=2,column=1)
button4.grid(row=2,column=0)
button3.grid(row=3,column=2)
button2.grid(row=3,column=1)
button1.grid(row=3,column=0)
button0.grid(row=4,column=0)
buttonDot.grid(row=4,column=1)
buttonEq.grid(row=4,column=2)
buttonPlus.grid(row=1,column=3)
ButtonMinus.grid(row=2,column=3)
buttonMult.grid(row=3,column=3)
buttonDiv.grid(row=4,column=3)
buttonClear.grid(row=5,column=0,columnspan=4)



root.mainloop()

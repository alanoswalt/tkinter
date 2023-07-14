#Calculator Version 1.0
from tkinter import *


root = Tk()
root.title('Calculator')

class operations_Calculator:


    def button_click(self, button):
        current=textbox.get()
        textbox.delete(0, END)
        textbox.insert(0, str(current)+str(button))
        #elif button=='c':
        #    textbox.delete(0, END)

    def button_clear(self):
        #textbox.delete(0, END)
        textbox.delete(0, END)

    def button_operation(self, op):
        global f_num
        f_num= float(textbox.get())
        textbox.delete(0, END)
        global operation
        operation = op

    def button_equal(self):
        first_number=float(f_num)
        second_number=float(textbox.get())
        textbox.delete(0, END)
        if operation == '+':
            result = first_number+second_number
        if operation == '-':
            result = first_number-second_number
        if operation == '*':
            result = first_number*second_number
        if operation == '/':
            result = first_number/second_number
        textbox.insert(0,result)


calculator=operations_Calculator()

#textbox
textbox=Entry(width=35, borderwidth=5)

#buttons
button9=Button(root, text="9", padx=20, pady=20, command=lambda: calculator.button_click(9))
button8=Button(root, text="8", padx=20, pady=20, command=lambda: calculator.button_click(8))
button7=Button(root, text="7", padx=20, pady=20, command=lambda: calculator.button_click(7))
button6=Button(root, text="6", padx=20, pady=20, command=lambda: calculator.button_click(6))
button5=Button(root, text="5", padx=20, pady=20, command=lambda: calculator.button_click(5))
button4=Button(root, text="4", padx=20, pady=20, command=lambda: calculator.button_click(4))
button3=Button(root, text="3", padx=20, pady=20, command=lambda: calculator.button_click(3))
button2=Button(root, text="2", padx=20, pady=20, command=lambda: calculator.button_click(2))
button1=Button(root, text="1", padx=20, pady=20, command=lambda: calculator.button_click(1))
button0=Button(root, text="0", padx=20, pady=20, command=lambda: calculator.button_click(0))
buttonEq=Button(root, text="=", padx=20, pady=20, command=lambda: calculator.button_equal())
buttonPlus=Button(root, text="+", padx=20, pady=20, command=lambda: calculator.button_operation('+'))
ButtonMinus=Button(root, text="-", padx=20, pady=20, command=lambda: calculator.button_operation('-'))
buttonDiv=Button(root, text="/", padx=20, pady=20, command=lambda: calculator.button_operation('/'))
buttonMult=Button(root, text="*", padx=20, pady=20, command=lambda: calculator.button_operation('*'))
buttonDot=Button(root, text=".", padx=20, pady=20, command=lambda: calculator.button_click('.'))

buttonClear=Button(root, text="Clear", padx=80 ,pady=20, command=lambda: calculator.button_clear())


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

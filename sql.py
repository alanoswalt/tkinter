from tkinter import *
from PIL import ImageTk, Image #Manage images
import sqlite3
#SLIDERS

root = Tk()
root.title('SLIDER')

#root.iconbitmap('C:/Users/alan_/Documents/tkinter/tkinter/image_view/bicycle.ico') #add icons to the window



#Create a DB or connect to one

connection = sqlite3.connect("address_book.db")

#Create a cursur, like a pointer, does stuff
cur = connection.cursor()



#Create table
#Is not necesary to execute the table when its already created
#cur.execute("""CREATE TABLE addresses(
#            first_name text,
#            last_name text,
#            address text,
#            city text,
#            state text, 
#            number integer
#)""")


def submit():

    #This needs to happend again inside the function
    connection = sqlite3.connect("address_book.db")

    #Create a cursur, like a pointer, does stuff
    cur = connection.cursor()

    #Insert in tablee
    cur.execute("INSERT INTO addreses VALUES (:f_name, :l_name, :address, :city, :state, :number)",
                {
                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'number':number.get()
                })

    #To commit the changes
    connection.commit()

    #Close the connection to data base
    connection.close()

    #Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    number.delete(0, END)

def update():

    #This needs to happend again inside the function
    connection = sqlite3.connect("address_book.db")

    #Create a cursur, like a pointer, does stuff
    cur = connection.cursor()

    #Insert in tablee
    cur.execute("INSERT INTO addreses VALUES (:f_name, :l_name, :address, :city, :state, :number)",
                {
                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'number':number.get()
                })
    record_id = id_box.get()
    cur.execute("""UPDATE addreses SET
                
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state, 
            number = :number
                
            WHERE oid = :oid""",
            {
                'first':f_name_editor.get(),
                'last':l_name_editor.get(),
                'address':address_editor.get(),
                'city':city.get(),
                'state':state_editor.get(),
                'number':number_editor.get(),
                'oid': record_id
            })

    #To commit the changes
    connection.commit()

    #Close the connection to data base
    connection.close()
    editor.destroy()

def delete():
        #This needs to happend again inside the function
    connection = sqlite3.connect("address_book.db")

    #Create a cursur, like a pointer, does stuff
    cur = connection.cursor()

    #Insert in tablee
    cur.execute("DELETE from addreses WHERE oid = " + id_box.get())

    #To commit the changes
    connection.commit()

    #Close the connection to data base
    connection.close()

    id_box.delete(0, END)

def query():

    connection = sqlite3.connect("address_book.db")

    #Create a cursur, like a pointer, does stuff
    cur = connection.cursor()


    print_records=""

    #Query Data base
    cur.execute("SELECT *, oid FROM addreses")
    records = cur.fetchall()
    #records = cur.fetchone()
    #records = cur.fetchmany(2)
    print(records)

    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11,column=0, columnspan=2)

    #To commit the changes
    connection.commit()

    #Close the connection to data base
    connection.close()

#Edit function to update record
def edit():
    global editor
    #Another Tk to open a window
    editor = Tk()
    editor.title('Update record')
    editor.geometry("400x600")
    connection = sqlite3.connect("address_book.db")

    #Create a cursur, like a pointer, does stuff
    cur = connection.cursor()

    records_id=id_box.get()

    #Query Data base
    cur.execute("SELECT * FROM addreses WHERE oid = " + records_id)
    records = cur.fetchall()

    #Create global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global number_editor

    #Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    number_editor = Entry(editor, width=30)
    number_editor.grid(row=5, column=1, padx=20)

    #Create label 
    name_Label_editor = Label(editor, text="Enter name")
    name_Label_editor.grid(row=0, column=0, padx=20)

    last_Label_editor = Label(editor, text="Last name")
    last_Label_editor.grid(row=1, column=0, padx=20)

    address_Label_editor = Label(editor, text="Address")
    address_Label_editor.grid(row=2, column=0, padx=20)

    city_Label_editor = Label(editor, text="City")
    city_Label_editor.grid(row=3, column=0, padx=20)

    state_Label_editor = Label(editor, text="State")
    state_Label_editor.grid(row=4, column=0, padx=20)

    number_Label_editor = Label(editor, text="Number")
    number_Label_editor.grid(row=5, column=0, padx=20)

    #Save button
    save_but= Button(editor, text="Save Changes", command=update)
    save_but.grid(row=6,column=0, columnspan=2, padx=10, pady=10, ipadx=100)

    #Loop results and put them in the boxes
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        number_editor.insert(0, record[5])

    #To commit the changes
    connection.commit()

    #Close the connection to data base
    connection.close()
    
#Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

number = Entry(root, width=30)
number.grid(row=5, column=1, padx=20)

id_box = Entry(root, width=30)
id_box.grid(row=8, column=1, padx=20, pady=(10,0))

#Create label 
name_Label = Label(root, text="Enter name")
name_Label.grid(row=0, column=0, padx=20)

last_Label = Label(root, text="Last name")
last_Label.grid(row=1, column=0, padx=20)

address_Label = Label(root, text="Address")
address_Label.grid(row=2, column=0, padx=20)

city_Label = Label(root, text="City")
city_Label.grid(row=3, column=0, padx=20)

state_Label = Label(root, text="State")
state_Label.grid(row=4, column=0, padx=20)

number_Label = Label(root, text="Number")
number_Label.grid(row=5, column=0, padx=20)

id_Label = Label(root, text="ID")
id_Label.grid(row=8, column=0, padx=20)



#Subbmit button
sub_but= Button(root, text="Add to DB", command=submit)
sub_but.grid(row=6,column=0, columnspan=2, padx=10, pady=10, ipadx=100)

#Query button
q_but= Button(root, text="See data", command=query)
q_but.grid(row=7,column=0, columnspan=2, padx=10, pady=10, ipadx=137)


#Delete button
delete_but= Button(root, text="Delete", command=delete)
delete_but.grid(row=9,column=0, columnspan=2, padx=10, pady=10, ipadx=136)

#Update butto
edit_but= Button(root, text="Update Record", command=edit)
edit_but.grid(row=10,column=0, columnspan=2, padx=10, pady=10, ipadx=136)

#To commit the changes
connection.commit()

#Close the connection to data base
connection.close()


root.mainloop() 
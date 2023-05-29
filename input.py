from tkinter import *
import mysql.connector

def takedetails1():

    sr_number = entry1.get()
    starting_city = entry2.get()
    destination_city = entry3.get()
    train_details = entry4.get()


    Mydatabase = mysql.connector.connect(host="localhost",user="root",password="manager",database="pythondb1" )
    cursor = Mydatabase.cursor()
    query = f"insert into train values({sr_number},'{starting_city}','{destination_city}','{train_details}');"
    cursor.execute(query)
    Mydatabase.commit()
   

tkwindow1=Tk()
tkwindow1.title("Python Mini Project")

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

Maintitle = Label(tkwindow1, text ='Insert Train Details', font='Bold')
Maintitle.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

lable1 = Label(tkwindow1, text ='Sr. Number')
lable1.pack()
entry1 = Entry(tkwindow1)
entry1.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()


lable2 = Label(tkwindow1, text ='Starting City')
lable2.pack()
entry2 = Entry()
entry2.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

lable3 = Label(tkwindow1, text ='Destination City')
lable3.pack()
entry3 = Entry(tkwindow1)
entry3.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

lable4 = Label(tkwindow1, text ='Train Details')
lable4.pack()
entry4 = Entry(tkwindow1)
entry4.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

SubmitButton = Button(tkwindow1,text='Submit',command = takedetails1)
SubmitButton.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

format_lable = Label(tkwindow1, text ='Train_No.- Train_Name , Arrival Time : Time , Departure Time : Time , Destination Time : Time')
format_lable.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()

Spacelabel1 = Label(tkwindow1,text=" ")
Spacelabel1.pack()


tkwindow1.mainloop()


# import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="manager",database="pythondb1")
# cursor=mydatabase.cursor()

# query="update dept set loc=%s where deptno=%s"
# loc=input("Enter location")
# deptno=input("Enter deptno")
# cursor.execute(query,[loc,deptno])
# mydatabase.commit()
   
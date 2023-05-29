from tkinter import *
import mysql.connector



def takedetails():
   
    startvalue = Entry1.get()
    endvalue = Entry2.get()

   
    Mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="manager",
        database="pythondb1"
    )

    cursor = Mydatabase.cursor()
    
    query = f"select traindetails from train where start1='{startvalue}' and end1='{endvalue}'"

    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    Mydatabase.close()
    resultwindow.delete(1.0, END)


    if (startvalue.casefold() == endvalue.casefold()):
        resultwindow.insert(END ,f"\n")
        resultwindow.insert(END ,f"You have entered both locations same")
        resultwindow.pack()
        

    else: 
     for row in rows:
        resultwindow.insert(END , f"\n")
        resultwindow.insert(END , f"      {row}\n")
        #result_text.insert(END, f"------------------------------------------------------------------------------")
        resultwindow.insert(END , f"\n")
        resultwindow.pack() 
        
        
tkwindow = Tk()
tkwindow.title("Python Project : Train Suggestions")
#tkwindow.geometry()

Spacelabel0 = Label(tkwindow,text=" ")
Spacelabel0.pack()

Maintitle = Label(tkwindow, text = "Indian Railways : भारतीय रेल ", font="bold")
Maintitle.pack()

Spacelabel1 = Label(tkwindow,text=" ")
Spacelabel1.pack()

Startlabel = Label(tkwindow, text="Starting location :", font =("calibri",12)) 
Startlabel.pack()

Entry1 = Entry(tkwindow) #######
Entry1.pack()

Endlabel = Label(tkwindow, text="Destination :", font =("calibri",12))
Endlabel.pack()

Entry2 = Entry(tkwindow) ########
Entry2.pack()

Searchbutton = Button(tkwindow, text="Search Trains", command = takedetails)
Searchbutton.pack()

Spacelabel2 = Label(tkwindow,text=" ")
Spacelabel2.pack()

resultwindow = Text(tkwindow, width=130, height=30)
resultwindow.pack()


tkwindow.mainloop()
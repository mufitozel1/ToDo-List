from tkinter import *

numbertasks = 0
i = 1 
globlanumberoftaskstoadd = 0

window=Tk()
window.title("To-Do List")
window.geometry("200x250")

def addtasks():
    numberoftaskstoadd = int(input("How many tasks would you like to enter(Please enter just a integer): "))
    globlanumberoftaskstoadd = numberoftaskstoadd
    for i in range(numberoftaskstoadd):
        if numberoftaskstoadd == 0:
            break
        List.insert(i,str(input("What would you like to add as your new action item: ")))
        i+=1

def deletetask():
    selected=List.curselection()
    List.delete(selected[0])

def markcompleted():
    marked=List.curselection()
    temp=marked[0]
    temp_marked=List.get(marked)
    temp_marked=temp_marked+" ✔"
    List.delete(temp)
    List.insert(temp,temp_marked)
           
Frame1 = Frame()
Frame1.pack()

Label1 =Label(window)
Label1.pack()

List = Listbox(Frame1)
List.pack()
numbertasks += globlanumberoftaskstoadd

AddButton = Button(window, text="Add New Task", command= addtasks)
AddButton.pack(side= LEFT)

DeleteButton = Button(window, text="Remove A Task", command= deletetask)
DeleteButton.pack(side=RIGHT)

CheckButton = Button(window, text="Complete Task", command= markcompleted)
CheckButton.pack(side=BOTTOM)

window.mainloop()

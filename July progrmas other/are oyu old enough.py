from age_function import *
from tkinter import *
def execute():
    dob = e.get()
    age = Age(dob)
    Passed = Pass18(age)
    label2=Label(window,text=Passed)
    label2.pack()

window = Tk()
window.geometry('1000x1000')
window.title("Bank Project")                                                                                                                  
label = ["Please enter your DOB in the ddmmyyyy format."]
for n in label:
    l = Label(window,text=n)
    e = Entry(window)
    l.pack()
    e.pack()
b = Button(window, text = "Submit",command=execute)
b.pack()
window.mainloop()

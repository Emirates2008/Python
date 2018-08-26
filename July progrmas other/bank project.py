
from tkinter import *
window = Tk()
window.geometry('1000x1000')
window.title("Bank Project")                                                                                                                  
label = ["Enter your name","Enter phone number.","Enter your address"]
c = ["Please enter your DOB in the ddmmyyyy format."]
for n in c:
    l = Label(window,text=n)
    e = Entry(window)
    l.pack()
    e.pack()
for i in label:
    l = Label(window,text=i)
    e = Entry(window)
    l.pack()
    e.pack()
b = Button(window, text = "Submit")
b.pack()
window.mainloop()

sl = c[4:]
age = 2018 - sly
if (age < 18):
        print("You are to young to get a bank account.")
    
            

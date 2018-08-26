from tkinter import *
window = Tk()
window.geometry('1000x1000')
window.title("GUI- Tkinter prog 1")                                                                                                                  
label = ["Enter your name","Enter your age","Enter phone number.","Enter your address"]

for i in label:
    l = Label(window,text=i)
    e = Entry(window)
    l.pack()
    e.pack()

b = Button(window, text = "Submit your answers")
b.pack()
window.mainloop()


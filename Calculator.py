import getpass
from tkinter import *
window = Tk()
window.title("Draft Calc")
a = Entry(window, width=35, borderwidth=5)
a.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Button Definitions
def add(number):
    curr = a.get()
    a.delete(0,END)
    a.insert(0,str(curr) + str(number))
    return
but1 = Button(window, text="1", padx=40, pady=15, command=lambda: add(1))
but2 = Button(window, text="2", padx=40, pady=15, command=lambda: add(2))
but3 = Button(window, text="3", padx=40, pady=15, command=lambda: add(3))
but4 = Button(window, text="4", padx=40, pady=15, command=lambda: add(4))
but5 = Button(window, text="5", padx=40, pady=15, command=lambda: add(5))
but6 = Button(window, text="6", padx=40, pady=15, command=lambda: add(6))
but7 = Button(window, text="7", padx=40, pady=15, command=lambda: add(7))
but8 = Button(window, text="8", padx=40, pady=15, command=lambda: add(8))
but9 = Button(window, text="9", padx=40, pady=15, command=lambda: add(9))
but0 = Button(window, text="0", padx=40, pady=15, command=lambda: add(0))
butad = Button(window,text="+", padx=39, pady=15, command=add)
buteq = Button(window,text="=", padx=88, pady=15, command=add)
butcl = Button(window, text="0", padx=88, pady=15, command=add)


#Button output format

but1.grid(row= 3, column=0)
but2.grid(row= 3, column=1)
but3.grid(row= 3, column=2)
but4.grid(row= 2, column=0)
but5.grid(row= 2, column=1)
but6.grid(row= 2, column=2)
but7.grid(row= 1, column=0)
but8.grid(row= 1, column=1)
but9.grid(row= 1, column=2)
but0.grid(row= 4, column=0)

butad.grid(row= 5,column=0)
buteq.grid(row= 5,column=1, columnspan=2)
butcl.grid(row= 4,column=1, columnspan=2)




window.mainloop()


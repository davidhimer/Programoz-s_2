
"""
A bolt termékeit itt lehet megadni
"""

from tkinter import *
import backend

backend.connect()

def get_selected_row(event):
   global selected_tuple
   index=list1.curselection()[0]
   selected_tuple=list1.get(index)
   e1.delete(0,END)
   e1.insert(END,selected_tuple[1])
   e2.delete(0,END)
   e2.insert(END,selected_tuple[2])


def add_new():
    backend.insert(nev_text.get(),ar_text.get())

    list1.delete(0, END)
    for row in backend.all_products():
        list1.insert(END, row)

def delete():
    backend.torles(selected_tuple[0])

    list1.delete(0, END)
    for row in backend.all_products():
        list1.insert(END, row)

window = Tk()

window.wm_title("Termék hozzáadása")

l1= Label(window,text ="Név")
l1.grid(row = 0, column = 0)

l2= Label(window,text ="Ár")
l2.grid(row = 1, column = 0)

nev_text=StringVar()
e1=Entry(window,textvariable=nev_text)
e1.grid(row=0, column= 1)

ar_text=StringVar()
e2=Entry(window,textvariable=ar_text)
e2.grid(row=1, column= 1)

list1 = Listbox(window, height=10, width=55)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

b1=Button(window,text="Hozzáad",width=13 ,command = add_new)
b1.grid(row =0 , column = 3)

b2=Button(window,text="Töröl",width=13 ,command = delete)
b2.grid(row =1 , column = 3)

list1.bind('<<ListboxSelect>>',get_selected_row)

for row in backend.all_products():
    list1.insert(END, row)

window.mainloop()

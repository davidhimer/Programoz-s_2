from tkinter import *
import backend

backend.connect_sl()

def get_selected_row(event):
   global selected_tuple
   index=list1.curselection()[0]
   selected_tuple=list1.get(index)
   e1.delete(0,END)
   e1.insert(END,selected_tuple[1])
   e2.delete(0,END)
   e2.insert(END,selected_tuple[2])

def get_selected_row_sl(event):
   global selected_tuple
   index=list2.curselection()[0]
   selected_tuple=list2.get(index)
   f1.delete(0,END)
   f1.insert(END,selected_tuple[1])
   f2.delete(0,END)
   f2.insert(END,selected_tuple[2])
   f3.delete(0,END)
   f3.insert(END,selected_tuple[3])
   f4.delete(0,END)
   f4.insert(END,selected_tuple[4])
   f5.delete(0,END)
   f5.insert(END,selected_tuple[5])

"""
Itt vannak definiálva a backendből meghívott funkciók amiket aztán megadunk alul a gomboknak.
"""

def add_sl():
    backend.insert_sl(nev.get(), price.get(), darab.get())

    list2.delete(0, END)
    for row in backend.all_shoppinglist():
        list2.insert(END, row)

def del_sl():
    backend.torles_sl(selected_tuple[0])

    list2.delete(0, END)
    for row in backend.all_shoppinglist():
        list2.insert(END, row)

def bill():
    list3.delete(0, END)
    list3.insert(0, backend.bill())

window = Tk()

"""
A fő ablak és a szövegek.
"""

window.wm_title("Products")

l1 = Label(window, text="Terméklista")
l1.grid(row=0, column=0)

l2 = Label(window, text="Kosár")
l2.grid(row=0, column=3)

l3 = Label(window, text="Darab")
l3.grid(row=12, column=0)

l4 = Label(window, text="Név")
l4.grid(row=11, column=0)

l5 = Label(window, text="Nettó Ár")
l5.grid(row=11, column=3)

l6 = Label(window, text="Egységár")
l6.grid(row=13, column=0)

l6 = Label(window, text="Brutto Ár")
l6.grid(row=12, column=3)

l7 = Label(window, text="Végösszeg")
l7.grid(row=13, column=3)

"""
Ezek a textfieldek.
"""
nev = StringVar()
e1 = f1 = Entry(window, textvariable=nev)
e1.grid(row=11, column=1)


price = StringVar()
e2 = Entry(window, textvariable=price)
e2.grid(row=13, column=1)
f2 = e2

darab = StringVar()
f3 = Entry(window, textvariable=darab)
f3.grid(row=12, column=1)

ar_netto = StringVar()
f4 = Entry(window, textvariable=ar_netto)
f4.grid(row=11, column=4)

ar_brutto = StringVar()
f5 = Entry(window, textvariable=ar_brutto)
f5.grid(row=12, column=4)

"""
Ezek a listák.
"""

list1 = Listbox(window, height=10, width=55)
list1.grid(row=1, column=0, rowspan=6, columnspan=2)

list2 = Listbox(window, height=10, width=55)
list2.grid(row=1, column=3, rowspan=6, columnspan=2)

list3 = Listbox(window,height = 1)
list3.grid(row=13, column=4)

list1.bind('<<ListboxSelect>>',get_selected_row)
list2.bind('<<ListboxSelect>>',get_selected_row_sl)

"""
Scrollbars.
"""
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

sb2 = Scrollbar(window)
sb2.grid(row=1, column=5, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)

"""
Ezek a gombok amik a funkciókat vazérlik.
"""

b1 = Button(window, text="Hozzáad", width=16, command=add_sl)
b1.grid(row=14, column=0)

b2 = Button(window, text="Termék törlése", width=16, command=del_sl)
b2.grid(row=14, column=1)

b3 = Button(window, text="Végösszeg mutatása", width=16, command=bill)
b3.grid(row=14, column=4)

for row in backend.all_products():
    list1.insert(END, row)

for row in backend.all_shoppinglist():
    list2.insert(END, row)

window.mainloop()
import tkinter as tk
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = display.curselection()[0]
        selected_tuple = display.get(index)

        e1.delete(0, tk.END)
        e1.insert(tk.END, selected_tuple[1])

        e2.delete(0, tk.END)
        e2.insert(tk.END, selected_tuple[2])

        e3.delete(0, tk.END)
        e3.insert(tk.END, selected_tuple[3])
    except IndexError:
        pass



def view_command():
    display.delete(0,tk.END)
    for row in backend.view():
        display.insert(tk.END, row)

def search_command():
    display.delete(0,tk.END)
    for row in backend.search(item_value.get()):
            display.insert(tk.END, row)

def add_command():
    backend.insert(item_value.get(), price_value.get(), quantity_value.get())
    display.delete(0, tk.END)
    display.insert(tk.END, (item_value.get(), price_value.get(), quantity_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], item_value.get(), price_value.get(), quantity_value.get())


window = tk.Tk()

window.wm_title("Shop Inventory")

l1 = tk.Label(window, text="Item")
l1.grid(row=0,column=0)


l2 = tk.Label(window, text="Price")
l2.grid(row=0,column=2)


l3 = tk.Label(window, text="Quantity")
l3.grid(row=0,column=4)

item_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=item_value)
e1.grid(row=0,column=1,rowspan=2)

price_value = tk.StringVar()
e2 = tk.Entry(window, textvariable=price_value)
e2.grid(row=0,column=3,rowspan=2)

quantity_value = tk.StringVar()
e3 = tk.Entry(window, textvariable=quantity_value)
e3.grid(row=0,column=5,rowspan=2)

display = tk.Listbox(window, height=20, width=50)
display.grid(row=4,column=0, rowspan=11, columnspan=4)

scroll = tk.Scrollbar(window)
scroll.grid(row=4, column=4, rowspan=12)

display.configure(yscrollcommand=scroll.set)
scroll.configure(command=display.yview)

display.bind("<<ListboxSelect>>", get_selected_row)

b1 = tk.Button(window, text="View All", width=12, command=view_command)
b1.grid(row=3,column=5)


b2 = tk.Button(window, text="Update Selected", width=12, command=update_command)
b2.grid(row=5,column=5)


b3 = tk.Button(window, text="Add", width=12, command=add_command)
b3.grid(row=7,column=5)


b4 = tk.Button(window, text="Search", width=12, command=search_command)
b4.grid(row=9,column=5)


b5 = tk.Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=11,column=5)


b6 = tk.Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=13,column=5)










window.mainloop()
import tkinter
from tkinter import *
from tkinter import messagebox
import random

window = tkinter.Tk()

window.configure(bg = "bisque")

window.title("TO DO LIST")

window.geometry("400x380")

tasks = []

'''FUNCTIONING'''
def update_listbox():
    clear_listbox()
    for task in tasks:
        listBox_tasks.insert("end", task)

def clear_listbox():
    listBox_tasks.delete(0, "end")

def add_task():
    task = text_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning", "No TASK entered")
    text_input.delete(0, "end")

def delete_all():
    confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
    if confirmed == True:
        # Since we are changing the list, it needs to be global.
        global tasks
        # Clear the tasks list
        tasks = []
        # Update the listbox
        update_listbox()

def delete_one():
    # Get the text of the currently selected item
    task = listBox_tasks.get("active")
    # confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    # update the listbox
    update_listbox()

def sort_asc():
    # sort the list
    tasks.sort()
    #update the listbox
    update_listbox()

def sort_desc():
    # sort the list
    tasks.sort()
    # then reverse the list
    tasks.reverse()
    # update the listbox
    update_listbox()


def show_number_of_tasks():
    # Get the number of tasks
    number_of_tasks = len(tasks)
    # Create and format the message
    msg = "Number of tasks: %s" % number_of_tasks
    # Display the message
    label_display["text"] = (msg)
def reminder():
    destroy.listBox_tasks()
    destroy.button_sort_asc()
    destroy.button_sort_desc()


''' DESIGN'''

#label_title = tkinter.Label(window, text = "GET SET DO !", bg = "bisque", fg='Orange')
#label_title.place(x=20,y=0,height=30,width=90)

menubar = Menu(window)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label='new')

label_display = tkinter.Label(window, text = "", bg="bisque")
label_display.place(x=200,y=5,height=10,width=110)

text_input = tkinter.Entry(window, width = 20)
text_input.place(x=160,y=40,height=40,width=160)

button_add_task = tkinter.Button(window, text = "Add TASK", bg = "white", command = add_task,font=('Georgia',12,'bold'))
button_add_task.place(x=10,y=40,height=30,width=100)

button_delete_all = tkinter.Button(window, text = "Clear all ", bg = "white", command = delete_all,font=('Georgia',12,'bold'))
button_delete_all.place(x=10,y=80,height=30,width=100)

button_delete_one = tkinter.Button(window, text = "Remove", bg = "white", command = delete_one,font=('Georgia',12,'bold'))
button_delete_one.place(x=10,y=120,height=30,width=100)

button_sort_asc = tkinter.Button(window, text = "SORT (ASC) ", bg = "white", command = sort_asc,font=('Georgia',10,'bold'))
button_sort_asc.place(x=10,y=160,height=35,width=100)

button_sort_desc = tkinter.Button(window, text = "SORT (DESC)", bg = "white", command = sort_desc,font=('Georgia',10,'bold'))
button_sort_desc.place(x=10,y=200,height=30,width=100)


button_number_of_tasks = tkinter.Button(window, text = "Number of \n Tasks", bg = "white", command = show_number_of_tasks ,font=('Georgia',12,'bold'))
button_number_of_tasks.place(x=10,y=240,height=40,width=100)

button_exit = tkinter.Button(window, text = "Reminder", bg = "white", command = reminder,font=('Georgia',12,'bold'))
button_exit .place(x=10,y=290,height=30,width=100)

listBox_tasks = tkinter.Listbox(window)
listBox_tasks.place(x=120,y=100,height=220,width=250)

window.config(menu=menubar)
window.mainloop()

from tkinter import *
import math

def add():
    add=float(e1_value.get())+float(e2_value.get())
    t1.insert(END,add)

def sub():
    sub=float(e1_value.get())-float(e2_value.get())
    t1.insert(END,sub)

def mult():
    mult=float(e1_value.get())*float(e2_value.get())
    t1.insert(END,mult)

def div():
    div=float(e1_value.get())/float(e2_value.get())
    t1.insert(END,div)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    t1_value.set("")

def log():
    log=math.log(float(e1_value.get()))
    t1.insert(END,log)

def cos():
    cos=math.cos(float(e1_value.get()))
    t1.insert(END,cos)

def sin():
    sin=math.log(float(e1_value.get()))
    t1.insert(END,sin)

def tan():
    tan=math.tan(float(e1_value.get()))
    t1.insert(END,tan)

def sqrt():
    sqrt=math.sqrt(float(e1_value.get()))
    t1.insert(END,sqrt)


#NORMAL CALCULATOR
def normal():
    e2_value.set('')
    b1=Button(window,text="ADD",width=14,command=add)
    b1.grid(row=7,column=0)

    b2=Button(window,text="SUBTRACT",width=14,command=sub)
    b2.grid(row=7,column=1)

    b3=Button(window,text="MULTIPLY",width=14,command=mult)
    b3.grid(row=8,column=0)

    b4=Button(window,text="DIVIDE",width=14,command=div)
    b4.grid(row=8,column=1)

    b5=Button(window,text="CLEAR",width=14,command=clear)
    b5.grid(row=9,column=0)

    b6=Button(window,text="EXIT",width=14,command=window.destroy)
    b6.grid(row=10,column=0)

    b7=Button(window,text="SCIENTIFIC",width=14,command=science)
    b7.grid(row=9,column=1)


#SCIENTIFIC CALCULATOR'''
def science():
    e2_value.set('above')
    b1=Button(window,text="Sin",width=14,command=sin)
    b1.grid(row=7,column=0)

    b2=Button(window,text="Cos",width=14,command=cos)
    b2.grid(row=7,column=1)

    b3=Button(window,text="Tan",width=14,command=tan)
    b3.grid(row=8,column=0)

    b4=Button(window,text="Log",width=14,command=log)
    b4.grid(row=8,column=1)

    b5=Button(window,text="Square root",width=14,command=sqrt)
    b5.grid(row=9,column=0)

    b7=Button(window,text="NORMAL",width=14,command=normal)
    b7.grid(row=9,column=1)

window = Tk()
window.wm_title("CALCULATOR")

'''LABELS'''
l1=Label(window,text="FIRST NUMBER :")
l1.grid(row=0,column=0)

l2=Label(window,text="SECOND NUMBER :")
l2.grid(row=2,column=0)

l3=Label(window,text="RESULT :")
l3.grid(row=4,column=0)


'''ENTRIES'''
e1_value=StringVar()
# if we replace StringVar with IntVar then e1 get a default value set as '0'
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=2,column=1)

t1_value=StringVar()
t1=Entry(window,textvariable=t1_value)
t1.grid(row=4,column=1)

'''BUTTONS'''
b1=Button(window,text="ADD",width=14,command=add)
b1.grid(row=7,column=0)

b2=Button(window,text="SUBTRACT",width=14,command=sub)
b2.grid(row=7,column=1)

b3=Button(window,text="MULTIPLY",width=14,command=mult)
b3.grid(row=8,column=0)

b4=Button(window,text="DIVIDE",width=14,command=div)
b4.grid(row=8,column=1)

b5=Button(window,text="CLEAR",width=14,command=clear)
b5.grid(row=9,column=0)

b7=Button(window,text="SCIENTIFIC",width=14,command=science)
b7.grid(row=9,column=1)

b6=Button(window,text="EXIT",width=14,command=window.destroy)
b6.grid(row=10,column=0)

window.mainloop()

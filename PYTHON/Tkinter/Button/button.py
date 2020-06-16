#!/usr/bin/python3
from tkinter import Tk,messagebox,Button
top=Tk()
top.geometry("300x300")


def fun():
    messagebox.showinfo("Hello", "Button clicked")

b1 = Button(top,text="Click Here",command=fun,activeforeground = "red",activebackground = "pink")
b1.pack()
top.mainloop()
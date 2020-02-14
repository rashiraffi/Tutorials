from tkinter import *
from tkinter import messagebox
top = Tk()  
top.geometry("200x100")  
def fun():
    messagebox.showwarning("Hello", "Red Button clicked")  
  
b1 = Button(top,text = "Red",command = fun,activeforeground = "black",activebackground = "green",pady=10,bd=2,bg="red")  
b2 = Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10)  
b3 = Button(top, text = "Green",activeforeground = "green",activebackground = "pink",pady = 10)  
b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
b1.pack(side = LEFT)  
b2.pack(side = RIGHT)  
b3.pack(side = TOP)  
b4.pack(side = BOTTOM)  
top.mainloop()  

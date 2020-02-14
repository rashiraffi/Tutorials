import tkinter as tk
from functools import partial
top = tk.Tk()  
top.geometry("400x250")
def msg(label,s):
    ss=(s.get())
    label.config(text="Hai %s"%ss)
    return

name = tk.Label(top, text = "Name").place(x = 30,y = 50)  
email = tk.Label(top, text = "Email").place(x = 30, y = 90)  
password = tk.Label(top, text = "Password").place(x = 30, y = 130)
lab=tk.Label(top).place(x=250,y=250)
name1=tk.StringVar()

  
e1 = tk.Entry(top,textvariable=name1).place(x = 80, y = 50)  
e2 = tk.Entry(top).place(x = 80, y = 90)  
e3 = tk.Entry(top).place(x = 95, y = 130)
msg=partial(msg,lab,name1)
sbmitbtn = tk.Button(top, text = "Submit",command=msg,activebackground = "pink", activeforeground = "blue").place(x = 30, y = 170)
top.mainloop()  

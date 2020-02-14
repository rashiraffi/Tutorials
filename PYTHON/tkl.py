import tkinter as tk
from functools import partial
def msg(label_result,s):
    result = (s.get())
    label_result.config(text="Name %s" % result)
    return
root = tk.Tk()
root.geometry("400x250")
root.title('Name')
name1=tk.StringVar()
name = tk.Label(root, text = "Name").place(x = 30,y = 50)  
email = tk.Label(root, text = "Email").place(x = 30, y = 90)
labelResult = tk.Label(root)  
labelResult.place(x=250,y=180)
e1 = tk.Entry(root,textvariable=name1).place(x = 80, y = 50)  
e2 = tk.Entry(root).place(x = 80, y = 90)
msg = partial(msg,labelResult,name1)
buttonCal = tk.Button(root, text="Calculate", command=msg).grid(row=3, column=0)  
root.mainloop() 

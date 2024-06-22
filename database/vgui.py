'''from tkinter import *
top=Tk()
top.title("welcome")
top.geometry("700x400")

btn1= Button (top, text="Login",bg='lightseagreen',width= 10)
btn1.pack(side= LEFT)
btn2= Button(top,text= "back",bg='lightseagreen',width= 10)
btn2.pack(side=RIGHT)
btn3= Button(top,text= "OK" ,bg='lightseagreen',width= 10)
btn3.pack(side=BOTTOM)
top.mainloop()'''
#====================================================================================================
'''from tkinter import *
parent=Tk()
parent.title("welcome")
parent.geometry("700x400")
name=Label(parent, text= "Name:" ,font=('times new roman',20,'bold'))
name.grid(row=0,column=0,padx=5,pady=10)
e1=Entry(parent)
e1.grid(row=0,column=1)
regno=Label(parent, text= "Regd No :",font=('times new roman',20,'bold'))
regno.grid(row=1,column=0,padx=5,pady=10)
e2=Entry(parent)
e2.grid(row=1,column=1)
btn=Button(parent,text="SUBMIT",bg='lightseagreen',width= 10)
btn.grid(row=3,column=1)

parent. mainloop()
'''
#====================================================================================================
'''from tkinter import *
parent=Tk()
parent.title("welcome")
parent.geometry("700x400")
name=Label(parent, text= "Name:" ,font=('times new roman',15,'bold'))
name.place(x=50,y=50)
e1=Entry(parent)
e1.place(x=150,y=50)
regno=Label(parent, text= "Regd No :",font=('times new roman',15,'bold'))
regno.place(x=50,y=100)
e2=Entry(parent)
e2.place(x=150,y=100)
parent. mainloop()'''
#====================================================================================================
from tkinter import *
from tkinter import messagebox
top=Tk()
top.title("welcome")
top.geometry("700x400")
def fun():
    messagebox.showinfo("Hello", "Blue Butthon Clicked")
btn1=Button (top,text="Red", bg="red" ,fg="white",width=10)
btn1.pack(side=LEFT)
btn2=Button (top,text="Green", bg="green",fg="pink" ,width=10,height=5,activebackground="yellow")
btn2.pack(side=TOP)
btn3=Button (top,text="Red", bg="blue",fg="yellow" ,width=10,command=fun)
btn3.pack(side=BOTTOM)
top.mainloop()




















'''from tkinter import*
top=Tk()
top.geometry("400x500")
cbtn1=Checkbutton(top,text="red",fg="red")
cbtn1.pack()
cbtn2=Checkbutton(top, text="Green",fg="green", activebackground="orange")
cbtn2.pack()
cbtn3=Checkbutton(top, text="Blue", bg="yellow", fg="blue", width=10,height=3)
cbtn3.pack()
top.mainloop()'''
#=======password============================================================
"""from tkinter import *
top=Tk()
top.geometry("400x500")
e1=Entry(top,width="30")
e1.place(x=50,y=40)
e2=Entry(top,bg="yellow")
e2.place(x=50,y=70)
e3=Entry(top,fg="red",show="*")
e3.place(x=50,y=100)
top.mainloop()"""
#=====FRAME=====================================================================
'''from tkinter import *
top=Tk()
top.geometry("400x500")
tframe=Frame(top,width="100",height="100",bg="yellow")
tframe.pack()
lframe=Frame(top,width="100",height="50",bg="seagreen")
lframe.pack(side=LEFT)
rframe=Frame(top,width="100",height="50",bg="green")
rframe.pack(side=RIGHT)
btn1=Button(tframe,text="Submit",fg="red")
btn1.place(x=10,y=10)
top.mainloop()'''
#====LABEL==================================================================
'''from tkinter import *
top=Tk()
top.geometry("400x500")
lbl1=Label(top,text="Name")
lbl1.place(x=10,y=10)
lbl2=Label(top,text="Password",bg="yellow",fg="red")
lbl2.place(x=10,y=40)
lbl3=Label(top,text="Age",padx=10,pady=10,bg="green")
lbl3.place(x=10,y=70)
top.mainloop()
'''
#===LISTBOX===========================================================
'''from tkinter import *
top=Tk()
top.geometry("400x500")
lbl1=Label(top,text="list of colours",bg="yellow",fg="red")
lbl1.place(x=10,y=10)
lb=Listbox(top,height=5)
lb.insert(1, "red")
lb.insert(2, "yellow")
lb.insert(3, "green")
lb.insert(4, "blue")
lb.place(x=10,y=30)
lbl2=Label(top,text="list of fruits",bg="green",fg="blue")
lbl2.place(x=160,y=10)
lb1=Listbox(top,height=5)
lb1.insert(1, "mango")
lb1.insert(2, "grapes")
lb1.insert(3, "banana")
lb1.insert(4, "berry")
lb1.place(x=160,y=30)
top.mainloop()'''
#RADIOBUTTON===========================================
'''from tkinter import *
top=Tk()
top.geometry("400x500")
radio=IntVar()
rbtn1=Radiobutton(top,text="red",variable=radio,value="1")
rbtn1.pack()
rbtn2=Radiobutton(top,text="green",variable=radio,value="2")
rbtn2.pack()
rbtn3=Radiobutton(top,text="blue",variable=radio,value="3")
rbtn3.pack()
top.mainloop()'''
#===text==================================================
'''from tkinter import *
top=Tk()
top.title("Address")
top.geometry("400x500")
lbl1=Label(top,text="Address:", fg="red",bg="yellow")
lbl1.place(x=10,y=10)
txt=Text(top,width=15,height=5)
txt.place(x=10,y=40)
top.mainloop()'''
#==========================================
'''from tkinter import *
top=Tk()

top.geometry("400x500")
lbl=Label(top,text="Price:",bg="yellow",fg="red")
lbl.pack()
scale=Scale(top,from_=100,to=1000,orient=VERTICAL)
scale.pack(anchor=CENTER)
top.mainloop()'''
#===============================================================
from tkinter import *
top=Tk()
top.geometry("400x500")
def fun():
    child=Toplevel(top)
    child.mainloop()
btn1=Button(top,text="open",width=10,command=fun)
btn1.place(x=50,y=50)
top.mainloop()










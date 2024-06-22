
#GUI==============================================================
from tkinter import *
top=Tk()
top.title("welcome")
top.geometry("700x400")

manage_frame=Frame(top,bd=4,relief=RIDGE,bg='lightseagreen')
manage_frame.place(x=0,y=0,width=400,height=400)
btn1= Button (manage_frame, text="Login",bg='seagreen',width= 10)
btn1.pack(side= LEFT)
btn2= Button(manage_frame,text= "back",bg='seagreen',width= 10)
btn2.pack(side=RIGHT)
btn3= Button(manage_frame,text= "OK" ,bg='seagreen',width= 10)
btn3.pack(side=BOTTOM)
top.mainloop()

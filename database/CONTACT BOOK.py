from tkinter import*
from tkinter import ttk
import mysql.connector

root=Tk()
root.title('CONTACT BOOK ANOTOMY ')
root.geometry('1350x700+0+0')
title=Label(root,text='CONTACT BOOK ANOTOMY',bd=10,relief=GROOVE,font=('ALGERIAN',40,'bold'),bg='teal',fg='white')
title.pack(side=TOP,fill=X)

#=========ALL VARIABLES============================================

serno_var=StringVar()
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
contact_var=StringVar()
dob_var=StringVar()
search_by=StringVar()
search_txt=StringVar()
       

#=========MANAGE FRAME==============================================
manage_frame=Frame(root,bd=4,relief=RIDGE,bg='lightseagreen')
manage_frame.place(x=20,y=100,width=450,height=580)
        
m_title=Label(manage_frame,text='MANAGE RECORD',bg='lightseagreen',fg='white',font=('times new roman',26,'bold'))
m_title.grid(row=0,columnspan=2,pady=20)
        
lbl_serno=Label(manage_frame,text='SER NO',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_serno.grid(row=1,column=0,pady=10,padx=20,sticky='w')
        
txt_serno=Entry(manage_frame,textvariable=serno_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_serno.grid(row=1,column=1,pady=10,padx=20,sticky='w')
        
lbl_name=Label(manage_frame,text='NAME',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')
        
txt_name=Entry(manage_frame,textvariable=name_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

lbl_email=Label(manage_frame,text='EMAIL',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky='w')
        
txt_email=Entry(manage_frame,textvariable=email_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_email.grid(row=3,column=1,pady=10,padx=20,sticky='w')

lbl_gender=Label(manage_frame,text='GENDER',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')

combo_gender=ttk.Combobox(manage_frame,textvariable=gender_var,font=('times new roman',13,'bold'),state='readonly')
combo_gender['values']=('male','female','other')
combo_gender.grid(row=4,column=1,padx=20,pady=10)
        

lbl_contact=Label(manage_frame,text='CONTACT',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')

txt_contact=Entry(manage_frame,textvariable=contact_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')

lbl_dob=Label(manage_frame,text='D.O.B',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky='w')

txt_dob=Entry(manage_frame,textvariable=dob_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky='w')


lbl_residence=Label(manage_frame,text='RESIDENCE',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_residence.grid(row=7,column=0,pady=10,padx=20,sticky='w')

txt_residence=Text(manage_frame,width=30,height=4,font=("",10))
txt_residence.grid(row=7,column=1,pady=10,padx=20,sticky='w')


def add_student():
    con=mysql.connector.connect(host='localhost',
                                password='Admin@123',
                                user='root',
                                database='stms')
    cur=con.cursor()
    cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)',(serno_var.get(),
                                                                    name_var.get(),
                                                                    email_var.get(),
                                                                    gender_var.get(),
                                                                    contact_var.get(),
                                                                    dob_var.get(),
                                                                    txt_residence.get('1.0',END)))
    con.commit()
    fetch_data()
    clear()
    con.close()

def update_data():
    con=mysql.connector.connect(host='localhost',
                                password='Admin@123',
                                user='root',
                                database='stms')
    cur=con.cursor()
    cur.execute('update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,residence=%s where serno=%s',(
                                                                        name_var.get(),
                                                                        email_var.get(),
                                                                        gender_var.get(),
                                                                        contact_var.get(),
                                                                        dob_var.get(),
                                                                        txt_residence.get('1.0',END),
                                                                        serno_var.get()
                                                                        ))
    con.commit()
    fetch_data()
    clear()
    con.close()

def fetch_data():
    con=mysql.connector.connect(host='localhost',
                                password='Admin@123',
                                user='root',
                                database='stms')
    cur=con.cursor()
    cur.execute('select*from student ')
    rows=cur.fetchall()
    if len(rows)!=0:
        for item in student_table.get_children():
            student_table.delete(item)
        for row in rows:
            student_table.insert('',END,values=row)
        con.commit()
    con.close()

def clear():
        serno_var.set("")
        name_var.set("")
        email_var.set("")
        gender_var.set("")
        contact_var.set("")                                                                   
        dob_var.set("")
        txt_residence.delete("1.0",END)

def get_cursor(ev):
    cursor_row=student_table.focus()
    contents=student_table.item(cursor_row)
    row=contents['values']
    serno_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    gender_var.set(row[3])
    contact_var.set(row[4])                                                                 
    dob_var.set(row[5])
    txt_residence.delete("1.0",END)
    txt_residence.insert(END,row[6])


     
def delete_data():
    con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='stms')
    cur=con.cursor()
    cur.execute('delete from student where serno=%s',(serno_var.get(),))
    con.commit()
    con.close()
    fetch_data()
    clear()
def search_data():
    con=mysql.connector.connect(host='localhost',password='Admin@123',user='root',database='stms')
    cur=con.cursor()
               
    cur.execute('select*from student where serno=%s',(search_txt.get(),))
    rows=cur.fetchall()
    if len(rows)!=0:
        for item in student_table.get_children():
            student_table.delete(item)
            
        
        for row in rows:
            student_table.insert('',END,values=row)
        con.commit()
    con.close()

#=========BUTTON FRAME==================================

btn_Frame=Frame(manage_frame,bd=4,relief=RIDGE,bg='lightseagreen')
btn_Frame.place(x=15,y=510,width=420)
        
add_btn=Button(btn_Frame,text='ADD',width=10,command=add_student).grid(row=0,column=0,padx=10,pady=10)

update_btn=Button(btn_Frame,text='UPDATE',width=10,command=update_data).grid(row=0,column=1,padx=10,pady=10)

delete_btn=Button(btn_Frame,text='DELETE',width=10,command=delete_data).grid(row=0,column=2,padx=10,pady=10)

clear_btn=Button(btn_Frame,text='CLEAR',width=10,command=clear).grid(row=0,column=3,padx=10,pady=10)
             

        
#=============DETAIL FRAME==============================================        
detail_frame=Frame(root,bd=4,relief=RIDGE,bg='lightseagreen')
detail_frame.place(x=500,y=100,width=800,height=580)

lbl_search=Label(detail_frame,text='SEARCH BY',bg='lightseagreen',fg='white',font=('times new roman',20,'bold'))
lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')

combo_search=ttk.Combobox(detail_frame,textvariable=search_by,width=10,font=('times new roman',13,'bold'),state='readonly')
combo_search['values']=('serno')
combo_search.grid(row=0,column=1,padx=20,pady=10)

txt_search=Entry(detail_frame,textvariable=search_txt,width=15,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

search_btn=Button(detail_frame,text='SEARCH',width=10,pady=5,command=search_data).grid(row=0,column=3,padx=10,pady=10)

showall_btn=Button(detail_frame,text='SHOW ALL',width=10,pady=5,command=fetch_data).grid(row=0,column=4,padx=10,pady=10)


#=================TABLE FRAME===========================================

table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='lightseagreen')
table_frame.place(x=10,y=70,width=760,height=500)

scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(table_frame,orient=VERTICAL)

student_table=ttk.Treeview(table_frame,columns=('serno','name','email','gender','contact','D.O.B','residence'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
        
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
        
student_table.heading('serno',text='Ser no')
student_table.heading('name',text='Name')
student_table.heading('email',text='Email')
student_table.heading('gender',text='Gender')
student_table.heading('contact',text='Contact')
student_table.heading('D.O.B',text='D.O.B')
student_table.heading('residence',text='Residence')

student_table['show']='headings'
student_table.column('serno',width=100)
student_table.column('name',width=100)
student_table.column('email',width=100)
student_table.column('gender',width=100)
student_table.column('contact',width=100)
student_table.column('D.O.B',width=100)
student_table.column('residence',width=150)
        
student_table.pack(fill=BOTH,expand=1)
student_table.bind('<ButtonRelease-1>',get_cursor)
        
        
fetch_data()

   
root.mainloop()

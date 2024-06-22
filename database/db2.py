'''import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin@123',
    database='vsics_database01'
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Students (name VARCHAR(255) , course VARCHAR(225))")'''
#==============================================================================
'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="vsics_database01")

mycursor=mydb.cursor()
sql="INSERT INTO students (name,course) VALUES (%s,%s)"
val=("puneet","ECE")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")'''
#==============================================================================
'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="vsics_database01")
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM students")
myresult=mycursor.fetchall()
for x in  myresult:
    print(x)'''
#====================================================================================
'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="school")
mycursor = mydb.cursor()
sql= "SELECT * FROM student WHERE stream='PCB' "
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in  myresult:
    print(x)'''
#=========================================================
'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="school")
mycursor = mydb.cursor()
sql= "SELECT * FROM student WHERE name LIKE '%raj%'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in  myresult:
    print(x)'''
#=================================================
'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="school")
mycursor = mydb.cursor()
sql= "SELECT * FROM student ORDER BY name"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in  myresult:
    print(x)'''
#======================================================
'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="school")
mycursor = mydb.cursor()
sql= "SELECT * FROM student ORDER BY name DESC"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in  myresult:
    print(x)'''
#======================================================
'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="school")
mycursor = mydb.cursor()
sql= "DELETE FROM student WHERE stream='PCM' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")
'''

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="school")
mycursor = mydb.cursor()
sql= "UPDATE student SET stream= 'CS' WHERE stream='CSE' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) AFFECTED")
print(mycursor.rowcount,"record(s) deleted")

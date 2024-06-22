'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE vandita_db01")'''
#creating the table ==================================
'''
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin@123',
    database='vandita_db01'
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Std (name VARCHAR(255) , course VARCHAR(225))")
'''
#entering the data==============================

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="vandita_db01")
mycursor=mydb.cursor()
sql="INSERT INTO Std (name , course) Values(%s,%s)"
val=[
('Vandita', 'BCA'),
('Saumya','BCA'),
('Shubhi','BCA'),
('Isha','BBA'),
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) inserted")

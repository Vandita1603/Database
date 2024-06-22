'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE contact")
'''
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="contact")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE details (serno VARCHAR(255),name VARCHAR(255),email VARCHAR(255), gender VARCHAR(255), contact VARCHAR(255),dob VARCHAR(255),residence VARCHAR(255))")


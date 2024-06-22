'''from mysql import connector
try:
    with connector.connect(
        host="localhost",
        user="root",
        password="Admin@123"
    ) as database:
        print(database)
except connector.Error as e:
    print(e)'''
#=======================================================
# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Admin@123")

# mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE v1")
#=======================================================
# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Admin@123",
#     database="vsics_database01")

#mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE vsics_database01")
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="vandita")










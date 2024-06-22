import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin@123',
    database='vsics_database01'
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Students (name VARCHAR(255) , course VARCHAR(225))")
#==============================================================================

"""
pip install pymysql

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="python400"
)

mycursor = mydb.cursor()
print("Database Connected Successfully")


host="localhost" → MySQL server is running on your computer.
user="root" → MySQL username.
password="" → Empty password (common in XAMPP).
database="python400" → Database name.
mydb.cursor() → Creates a cursor to execute SQL queries.


"""

import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

#Database create
mycursor.execute("create database if not exists pydb")
#print("Database Created Successfully")


#database connect after db created
mydb = pymysql.connect(host="localhost",user="root",password="",database="pydb")
mycursor=mydb.cursor()
#print("Database connected Successfully")


#table create
mycursor.execute("""create table if not exists user(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)""")
#print("Table user created Successfully")



#insert data
# data = ("Rajesh", "rajesh@gmail.com")
# mycursor.execute("insert into user(name,email) value(%s,%s)", data)
# mydb.commit()   # use always commit() after insert update delete
# print("Data Inserted Successfully")


#get all data
# mycursor.execute("select * from user")
# result=mycursor.fetchall()
# for row in result:
#     print(row);  # get data in tuple ()


# #get single id where data
# id = int(input("Enter Student ID: "))
# mycursor.execute("select * from user where id=%s",(id,))
# data=mycursor.fetchone()
# if data:
#     print("Student Found")
#     print("ID:", data[0])
#     print("Name:", data[1])
#     print("Email:", data[2])
# else:
#     print("Student Not Found")
# mydb.close()

# get serach pattern data
# name = input("Enter Student Name: ")
# data=name + "%"
# mycursor.execute("SELECT * FROM user WHERE name LIKE %s",(data,))
# data = mycursor.fetchall()
# for row in data:
#     print(row);  # get data in tuple ()


# update data
# data = ("Raj nagar", 1)
# mycursor.execute("UPDATE user SET name=%s WHERE id=%s", data)
# mydb.commit()
# print("user Updated success");


# Delete data
# data = (3,)
# mycursor.execute("DELETE FROM user WHERE id=%s", data)
# mydb.commit()
# print("user Deleted success");


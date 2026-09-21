"""
import pymysql
mydb=pymysql.connect()
mycursor=mydb.cursor()
mycursor.execute(query)

"""

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor() 

while True:

    menu = """
    Press 1 for Insert Data
    Press 2 for Fetch All Data
    Press 3 for Fetch Single Data
    Press 4 for Fetch Data by Name
    Press 5 for Update Data
    Press 6 for Delete Data
    Press 7 for Exit
    """

    print(menu)

    choice = int(input("Enter Choice : "))

    # INSERT
    if choice == 1:

        name = input("Enter Name : ")
        email = input("Enter Email : ")

        query = "INSERT INTO user(name, email) VALUES (%s, %s)"

        mycursor.execute(query, (name, email))
        mydb.commit()

        print("Data Inserted!!")


    # FETCH ALL
    elif choice == 2:

        query = "SELECT * FROM user"
        mycursor.execute(query)
        data = mycursor.fetchall()

        for row in data:
            print(row)


    # FETCH SINGLE
    elif choice == 3:

        id = int(input("Enter ID : "))

        query = "SELECT * FROM user WHERE id=%s"
        mycursor.execute(query, (id,))
        data = mycursor.fetchone()
        print(data)


    # SEARCH BY NAME
    elif choice == 4:

        name = input("Enter Name : ")

        search = name + "%"
        query = "SELECT * FROM user WHERE name LIKE %s"
        mycursor.execute(query, (search,))
        data = mycursor.fetchall()

        for row in data:
            print(row)


    # UPDATE
    elif choice == 5:

        id = int(input("Enter ID : "))
        name = input("Enter Updated Name : ")
        email = input("Enter Updated Email : ")

        query = "UPDATE user SET name=%s, email=%s WHERE id=%s"
        mycursor.execute(query, (name, email, id))
        mydb.commit()

        print("Data Updated!!")


    # DELETE
    elif choice == 6:

        id = int(input("Enter ID : "))

        query = "DELETE FROM user WHERE id=%s"
        mycursor.execute(query, (id,))
        mydb.commit()

        print("Data Deleted!!")


    # EXIT
    elif choice == 7:

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")
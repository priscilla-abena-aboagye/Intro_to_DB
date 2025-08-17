import mysql.connector
from mysql.connector import Error

def create_database():
    mydb = None
    mycursor = None
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="WeOwnTheN!ght2025"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()


if __name__ == "__main__":
    create_database()

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )
        
        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

create_database()


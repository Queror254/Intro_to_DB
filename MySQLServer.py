 import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root', 
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:  # Specific exception handling for MySQL errors
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()


import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL on port 33061
        connection = mysql.connector.connect(
            host="localhost",
            port=33061,  # Specify the correct port
            user="root",
            password="password",
            use_pure=True,  
            ssl_disabled=True,
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Call the function
create_database()

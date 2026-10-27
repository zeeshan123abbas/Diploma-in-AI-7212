# connect_test.py
# Step 1 of database work: can Python connect to MySQL?
import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG

try:
    connection = mysql.connector.connect(**DB_CONFIG)   # open the connection
    if connection.is_connected():
        print("Connected to MySQL server version", connection.server_info)
        cursor = connection.cursor()                    # a cursor runs SQL
        cursor.execute("SELECT DATABASE()")
        print("Current database:", cursor.fetchone()[0])
        cursor.close()
except Error as error:
    print("Connection failed:", error)
finally:
    if "connection" in locals() and connection.is_connected():
        connection.close()                              # always close
        print("Connection closed")

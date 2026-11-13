import mysql.connector

def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass123",
        database="sales_management"
    )

    return conn
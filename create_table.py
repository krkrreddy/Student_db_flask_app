import sqlite3
import pyodbc

# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()
conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

cursor = conn.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username nvarchar(10), password nvarchar(10)"
cursor.execute(create_table)

create_table = "CREATE TABLE student (student text PRIMARY KEY, roll_number INTEGER)"
cursor.execute(create_table)

conn.commit()

conn.close()
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
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS student (student text PRIMARY KEY, roll_number INTEGER)"
cursor.execute(create_table)

conn.commit()

conn.close()
from flask import Flask,request,render_template
from flask_restful import Resource, Api,reqparse
import json
import csv
import sqlite3
import json
import pyodbc


class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
    @classmethod
    def find_by_username(cls,username):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username =?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def find_by_id (cls,_id):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id =?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user

class UserRegister(Resource):
    TABLE_NAME = 'users'
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))
        conn.commit()
        conn.close()

        return {"message": "User created successfully."}, 201





# conn = pyodbc.connect('Driver={SQL Server};'
#                               'Server=LAPTOP-QKUAIV9T;'
#                               'Database=flask;'
#                               'Trusted_Connection=yes;')
#
# cursor = conn.cursor()
# #create_table ="(CREATE TABLE IF NOT EXISTS flask.dbo.users(id  int,username text,password text)"
# #create_table ="(IF object_id(users) IS NULL BEGIN CREATE TABLE flask.dbo.users(id  int,username text,password text) END)"
#
# #cursor.execute(create_table)
#
# user = (35,'ravi','welcome')
# insert_query = "INSERT INTO flask.dbo.users VALUES(?,?,?)"
# cursor.execute(insert_query,user)
# results=[]
# for row in cursor.execute("select * from flask.dbo.users"):
#     results.append([x for x in row])
#
# conn.commit()
# conn.close()
#
# print(results)


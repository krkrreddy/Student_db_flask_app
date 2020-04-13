from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import pyodbc

class Student(Resource):
    TABLE_NAME = 'flask.dbo.student'
    parser = reqparse.RequestParser()
    parser.add_argument('roll_number',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def __init__(self):
        pass
    def get(self,name):
        student = self.find_by_name(name)
        if student:
            return student
        return {'message': 'student not found'}, 404

    def find_by_name(cls, name):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        query = "SELECT * FROM {table} WHERE student=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()
        if row:
            return {'student': {'name': row[0], 'roll_number': row[1]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "Student with name '{}' already exists.".format(name)}

        data = Student.parser.parse_args()
        student = {'name': name, 'roll_number': data['roll_number']}

        try:
            Student.insert(student)
        except:
            return {"message": "An error occurred inserting the student detail."}

        return student
    @classmethod
    def insert(cls, student):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (student['name'], student['roll_number']))
        conn.commit()
        conn.close()

    @jwt_required()
    def delete(self, name):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()
        return {'message': 'student details deleted'}

    @jwt_required()
    def put(self, name):
        data = Student.parser.parse_args()
        student = self.find_by_name(name)
        updated_student = {'name': name, 'roll_number': data['roll_number']}
        if student is None:
            try:
                Student.insert(updated_student)
            except:
                return {"message": "An error occurred inserting the student."}
        else:
            try:
                Student.update(updated_student)
            except:
                return {"message": "An error occurred updating the student."}
        return updated_student

    @classmethod
    def update(cls, student):

        query = "UPDATE {table} SET roll_number=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (student['name'], student['roll_number']))
        conn.commit()
        conn.close()


class Studentlist(Resource):
    def get(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-QKUAIV9T;'
                              'Database=flask;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        select_query = "select * from flask.dbo.student"
        lis = []
        for row in cursor.execute(select_query):
            lis.append({'name': row[0], 'roll_number': row[1]})
        conn.close()
        if lis:
            return {'results': lis}
        return {'results':None},404



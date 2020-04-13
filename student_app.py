from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from db_user import UserRegister
from student import Student, Studentlist

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'ravi'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Student, '/student/<string:name>')
api.add_resource(Studentlist, '/students')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Blueprint, request, session
from models.User import User
from setup import engine
from sqlalchemy import insert, delete, select

users = Blueprint(name='users', import_name=__name__, url_prefix='/users')


@users.route('/', methods=['GET'])
def get_users():
    statement = select([User])
    resultProxy = engine.execute(statement)
    resultSet = resultProxy.fetchall()
    toDict = lambda row: {c.name: str(getattr(row, c.name)) for c in row.__table__.columns}
    return {
        'users': [toDict(row) for row in resultSet]
    }


@users.route('/', methods=['POST'])
def create():
    stmt = User.insert().values({
        'username': 'Jael',
        'password': 123456,
        'email': 'Jael@gmaiz.com'
    })
    try:
        res = engine.execute(stmt)
        print(res.inserted_primary_key)
        return {
            'success': 'User inserted successfully'
        }
    except Exception as e:
        print(e)
        return {
            'error': 'Error creating a new user'
        }

@users.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return {
        'message': 'successful'
    }
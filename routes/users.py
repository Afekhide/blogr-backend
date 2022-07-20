from flask import Blueprint, request
import time
from models.User import User
from schemas import UserSchema
from setup import session as dbsession
from setup import schema_list_to_dict
from flask_cors import cross_origin
from sqlite3 import IntegrityError

users = Blueprint(name='users', import_name=__name__, url_prefix='/users')


@cross_origin()
@users.route('/', methods=['GET'])
def create():
    users = dbsession.query(User).order_by(User.id).all()
    users_schema = UserSchema()
    users = users_schema.dumps(users, many=True)
    return {
        'users': schema_list_to_dict(users)
    }


@cross_origin()
@users.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return {
        'message': 'successful'
    }


@users.route('/', methods=['POST'])
def new_user():
    post_data = request.get_json()
    print(post_data)
    temp_user = User(username=post_data['username'], email=post_data['email'], password=post_data['password'])
    try:
        dbsession.add(temp_user)
        dbsession.commit()
        time.sleep(5)
        return {
            'success': 'user created successfully'
        }

    except IntegrityError as e:
        print(e.__cause__)
        return {
            'error': 'integrity error'
        }

    except Exception as e:
        return {
            'error': 'could\'nt create new user'
        }


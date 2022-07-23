from flask import Blueprint, request, make_response
import time
from models.User import User
from schemas import UserSchema, UserSchemaMinimal
from setup import session as dbsession
from setup import schema_list_to_dict
from sqlite3 import IntegrityError

user_blueprint = Blueprint(name='users', import_name=__name__, url_prefix='/users')
users_schema = UserSchema()


@user_blueprint.route('/', methods=['GET'])
def create():
    users = dbsession.query(User).order_by(User.id).all()
    users = users_schema.dumps(users, many=True)
    return {
        'users': schema_list_to_dict(users)
    }


@user_blueprint.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    query = dbsession.query(User)
    target_user = query.where(User.id == id).first()
    if target_user is None:
        return {
            'error': {
                'message': f'no such user with id: {id}'
            }
        }

    try:
        from models.Post import Post
        (dbsession.query(Post).filter(Post.authorId == id).delete())
        # dbsession.commit()
        dbsession.delete(target_user)
        dbsession.commit()
        return {
            'success': {
                'message': f'user {id} deleted successfully'
            }
        }
    except Exception as e:
        print(e)
        return {
            'error': {
                'message': f'unknown error whilst deleting user: {id}'
            }
        }


@user_blueprint.route('/', methods=['POST'])
def new_user():
    post_data = request.get_json()
    print(post_data)
    temp_user = User(username=post_data['username'], email=post_data['email'], password=post_data['password'])
    try:
        dbsession.add(temp_user)
        dbsession.commit()
        time.sleep(5)
        return {
            'success': {'user': users_schema.dump(temp_user)}
        }

    except IntegrityError as e:
        print(e.__cause__)
        return {
            'error': {'message': 'email already registered'}
        }

    except Exception as e:
        return {
            'error': 'could\'nt create new user'
        }


@user_blueprint.route('/login', methods=['POST'])
def login():
    sent_data = request.get_json()
    print(sent_data)
    if ('email' not in sent_data) or ('password' not in sent_data):
        return {
            'error': {
                'message': 'Incomplete request'
            }
        }

    temp_user = dbsession.query(User).where(User.email == sent_data['email']).first()
    if temp_user is None:
        return {'error': {'message': f'no user found for {sent_data["email"]}'}}
    if temp_user.verify_password(sent_data['password']):
        return {
            'success': {
                'user': (users_schema.dump(temp_user))
            }
        }

    else:
        return {'error': {'message': f'invalid credentials'}}

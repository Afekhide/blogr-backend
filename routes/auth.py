from flask import Blueprint

auth = Blueprint(name='auth', import_name=__name__, url_prefix='/auth')


@auth.route('/', methods=['GET'])
def signIn():
    return {
        'message': 'Sign in route'
    }

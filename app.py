import secrets
from flask import Flask
from routes.blogs import blogs
from routes.users import users
from routes.auth import auth


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(blogs)


@app.route('/', methods=['GET', 'POST'])
def index():
    return {
        'error': {
            'code': 403,
            'message': 'Forbidden path'
        }
    }


if __name__ == '__main__':
    app.run(port=9999, debug=True)

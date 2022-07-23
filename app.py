

import os
import secrets
from flask import Flask
from flask_cors import CORS
from routes.blogs import blogs
from routes.users import user_blueprint
from routes.auth import auth


app = Flask(__name__)
# CORS(app, origins=['https://fascinating-medovik-2b06ac.netlify.app'])
CORS(app, origins=['*'])
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.register_blueprint(auth)
app.register_blueprint(user_blueprint)
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
    app.run(debug=True, port=os.getenv('PORT', 5000))

import os
from sqlalchemy import create_engine
from models.User import User
from models.Post import Post

DB_PATH = os.path.dirname(__file__)
DB_URL = f'sqlite:///{DB_PATH}/database.db'

engine = create_engine(DB_URL)


def init_db():
    Post.create(engine)
    User.create(engine)

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base

DB_PATH = os.path.dirname(__file__)
DB_URL = f'sqlite:///database.db'
print(DB_URL)
engine = create_engine(DB_URL)
session = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)

import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base

DB_PATH = os.path.dirname(__file__)
DB_URL = f'sqlite:///database.db?check_same_thread=False'
print(DB_URL)
engine = create_engine(DB_URL)
session = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)


def schema_list_to_dict(schema_list):
    return json.loads(schema_list)

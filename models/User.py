from sqlalchemy import Table, String, Column, Integer, Text, DateTime, MetaData
from datetime import datetime
from . import metadata


User = Table('users', metadata,
             Column('id', Integer, primary_key=True, unique=True, autoincrement=True),
             Column('username', String(30), nullable=False),
             Column('email', String(30), nullable=False, unique=True),
             Column('password', String(150), nullable=False),
             Column('joinedAt', DateTime, nullable=False, default=datetime.utcnow)
             )

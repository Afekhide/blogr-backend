from sqlalchemy import Table, MetaData
from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime
from . import metadata

Post = Table('posts', metadata,
             Column('id', Integer, primary_key=True, unique=True, autoincrement=True),
             Column('title', String(50), nullable=False),
             Column('content', Text, nullable=False),
             Column('createdAt', DateTime, nullable=False, default=datetime.utcnow)
             )

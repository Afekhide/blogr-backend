from sqlalchemy import String, Column, Integer, Text, DateTime
from datetime import datetime
from . import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    joinedAt = Column(DateTime, nullable=False, default=datetime.utcnow)

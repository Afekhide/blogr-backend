
from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime
from . import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=datetime.utcnow)

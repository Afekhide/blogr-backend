
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from . import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=datetime.utcnow)
    authorId = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"Post<id:{self.id}, title:{self.title}, createdAt:{self.createdAt}, authorId:{self.authorId}>"

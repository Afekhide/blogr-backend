from sqlalchemy import String, Column, Integer, Text, DateTime
from datetime import datetime
from . import Base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    passwordHash = Column(String(150), nullable=False)
    posts = relationship('Post', back_populates='author', lazy=False)
    joinedAt = Column(DateTime, nullable=False, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('Password property is not readable')

    @password.setter
    def password(self, newPassword):
        self.passwordHash = generate_password_hash(newPassword, salt_length=16)

    def verify_password(self, password):
        return check_password_hash(self.passwordHash, password)

    def __repr__(self):
        return f"User<id:{self.id}, username:{self.username}, email:{self.email}, joinedAt:{self.joinedAt}>"

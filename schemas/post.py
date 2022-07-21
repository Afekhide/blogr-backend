from models.Post import Post
from .user import UserSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested


class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
        include_fk = True
        include_relationships = True

    author = Nested(UserSchema, exclude=('posts',))

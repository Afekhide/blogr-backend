from models.Post import Post
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
        include_relationships = True

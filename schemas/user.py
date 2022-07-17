from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.User import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True

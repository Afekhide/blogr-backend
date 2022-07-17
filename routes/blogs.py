from flask import Blueprint
from models.Post import Post

blogs = Blueprint(name='blogs', import_name=__name__, url_prefix='/blogs')


@blogs.route('/', methods=['GET'])
def get_blogs():
    return {
        'blogs': []
    }
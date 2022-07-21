import time
from flask import request
from setup import session
from flask import Blueprint
from models.Post import Post
from schemas.post import PostSchema
from setup import schema_list_to_dict

posts_schema = PostSchema()
blogs = Blueprint(name='blogs', import_name=__name__, url_prefix='/blogs')


@blogs.route('/', methods=['GET'])
def all_posts():
    posts = session.query(Post).order_by(Post.id).all()
    time.sleep(2)
    blogs = schema_list_to_dict(posts_schema.dumps(posts, many=True))
    return {
        'blogs': blogs
    }


@blogs.route('/<int:id>', methods=['GET'])
def single(id):
    post = session.query(Post).filter(Post.id == id).first()
    if post is None:
        return {
            'error': {
                'message': f'no blog post matches the specified id:{id}'
            }
        }
    print(post)
    time.sleep(2)
    return {
        'success': {'post': posts_schema.dump(post)}
    }


@blogs.route('/', methods=['POST'])
def new_post():
    post_data = request.get_json()
    temp_post = Post(title=post_data['title'], content=post_data['content'], authorId=post_data['authorId'])
    print(request.get_json())
    try:
        session.add(temp_post)
        session.commit()
        time.sleep(3)
        return {
            'success': {'message': 'post created successfully'}
        }

    except Exception as e:
        print(e)
        return {
            'error': {'message': 'could\'nt create new user'}
        }

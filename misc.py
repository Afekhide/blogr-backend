import random
import requests
from setup import session
from models import Post, User


def fetch_stories():
    url = 'https://shortstories-api.herokuapp.com/stories'
    authors = [author.id for author in session.query(User).all()]
    posts = []
    print(authors)
    try:
        response = requests.get(url).json()
        for story in response:
            posts.append(Post(title=story['title'], content=story['story'], authorId=random.choice(authors)))
        print(posts)
        return posts
    except Exception as e:
        print(e)
        return []


fetch_stories()

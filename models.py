from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    movie_id = db.Column(db.String(10), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f"<Comment {self.text}>"

    def __init__(self, name, movie_id, text, rating):
        self.username = name
        self.movie_id = movie_id
        self.text = text
        self.rating = rating


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def __init__(self, name):
        self.username = name

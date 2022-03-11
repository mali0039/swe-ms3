from models import Comment


def fetch_movie_comments(movie_id):
    comments = Comment.query.filter_by(movie_id=movie_id).all()
    return comments

def fetch_user_comments(username):
    comments = Comment.query.filter_by(username=username).all()
    return comments

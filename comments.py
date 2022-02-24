from models import Comment


def fetch_comments(movie_id):
    comments = Comment.query.filter_by(movie_id=movie_id).all()
    return comments

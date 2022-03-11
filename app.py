import os
import flask
from flask_login import (
    LoginManager,
    login_required,
    current_user,
    login_user,
    logout_user,
)
from dotenv import find_dotenv, load_dotenv

from tmbd import get_random_movie
from wiki import get_wiki_url
from models import Comment, User, db

from comments import fetch_movie_comments, fetch_user_comments

load_dotenv(find_dotenv())
login_manager = LoginManager()

app = flask.Flask(__name__)
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db.init_app(app)
login_manager.login_view = "login"
login_manager.init_app(app)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# All routes contained here


@bp.route("/profile")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


@app.route("/")  # Python decorator
@login_required
def main():
    movie_details = get_random_movie()
    wiki_id = get_wiki_url(movie_details["title"] + movie_details["date"])
    # Get comments for the random movie id
    comments = fetch_movie_comments(movie_details["movie_id"])
    return flask.render_template(
        "home.html", data=movie_details, wiki_id=wiki_id, comments=comments
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        user = User.query.filter_by(username=username).first()
        # If user exists, login. If not, flash error
        if user:
            login_user(user)
            return flask.redirect(flask.url_for("main"))
        flask.flash("User does not exist!")
        return flask.redirect(flask.url_for("login"))
    # GET route
    return flask.render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        if len(username.strip()) >= 3:
            user = User(username)
            existing = User.query.filter_by(username=username).all()
            if not existing:
                # Add user if username isnt taken
                db.session.add(user)
                db.session.commit()
                user = User.query.filter_by(username=username).first()
                login_user(user)
                return flask.redirect(flask.url_for("login"))
            # If taken, flash error
            flask.flash("Username already exists!")
        else:
            # If empty username, flash error
            flask.flash("Empty usernames are not allowed!")
        # Redirect to signup if any errors
        return flask.redirect(flask.url_for("signup"))
    # GET route
    return flask.render_template("signup.html")


@app.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return flask.redirect(flask.url_for("login"))


@app.route("/comment/<movie_id>", methods=["POST"])
def post_comment(movie_id):
    comment_text, comment_rating = (
        flask.request.form["text"],
        flask.request.form["rating"],
    )
    # Ensure comment length > 3
    if len(comment_text.strip()) >= 3:
        comment = Comment(current_user.username, movie_id, comment_text, comment_rating)
        db.session.add(comment)
        db.session.commit()
    return flask.redirect(flask.url_for("main"))

@app.route("/updateComments", methods=["POST"])
def post_update_comments():
    comments = flask.request.get_json()
    for comment in comments:
        oldComment = Comment.query.filter_by(id=comment["id"]).first()
        oldComment.text = comment["text"]
        oldComment.rating = comment["rating"]
    db.session.commit()
    return {"status": "success"}

@app.route("/comments")
def get_user_comments():
    def deconstruct(comment):
        return {
            "id": comment.id,
            "rating": comment.rating,
            "username": comment.username,
            "movie_id": comment.movie_id,
            "text": comment.text,
        }

    allComments = list(map(deconstruct, fetch_user_comments(current_user.username)))
    return {"comments": allComments}


app.register_blueprint(bp)


app.run(
    debug=True, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080"))
)

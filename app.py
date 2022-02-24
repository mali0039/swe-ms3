import os
import flask
from tmbd import get_random_movie
from wiki import get_wiki_url
from models import Comment, User, db
from dotenv import find_dotenv, load_dotenv
from flask_login import (
    LoginManager,
    login_required,
    current_user,
    login_user,
    logout_user,
)
from comments import fetchComments

load_dotenv(find_dotenv())
login_manager = LoginManager()

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
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


@app.route("/")  # Python decorator
@login_required
def main():
    movie_details = get_random_movie()
    wiki_id = get_wiki_url(movie_details["title"] + movie_details["date"])
    print(movie_details["movieID"])
    comments = fetchComments(movie_details["movieID"])
    return flask.render_template(
        "index.html", data=movie_details, wiki_id=wiki_id, comments=comments
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        user = User.query.filter_by(username=username).first()
        print(user)
        if user:
            login_user(user)
            return flask.redirect(flask.url_for("main"))
        else:
            flask.flash("User does not exist!")
            return flask.redirect(flask.url_for("login"))

    return flask.render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        user = User(username)
        existing = User.query.filter_by(username=username).all()
        if not existing:
            db.session.add(user)
            db.session.commit()
            user = User.query.filter_by(username=username).first()
            login_user(user)
            return flask.redirect(flask.url_for("login"))
        else:
            flask.flash("Username already exists!")
            return flask.redirect(flask.url_for("signup"))
    else:
        return flask.render_template("signup.html")


@app.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return flask.redirect(flask.url_for("login"))


@app.route("/comment/<movieID>", methods=["POST"])
def postComment(movieID):
    commentText, commentRating = (
        flask.request.form["text"],
        flask.request.form["rating"],
    )
    comment = Comment(current_user.username, movieID, commentText, commentRating)
    db.session.add(comment)
    db.session.commit()
    return flask.redirect(flask.url_for("main"))


app.run(
    debug=True, host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080"))
)

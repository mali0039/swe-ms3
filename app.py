import os
import flask
from tmbd import get_random_movie
from wiki import get_wiki_url

app = flask.Flask(__name__)

@app.route("/")  # Python decorator
def main():
    movie_details = get_random_movie()
    wiki_id= get_wiki_url(movie_details["title"] + movie_details["date"])
    print(wiki_id)
    return flask.render_template("index.html", data=movie_details, wiki_id=wiki_id)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', '8080')),
)

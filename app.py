import flask
from tmbd import getRandomMovie
import os
app = flask.Flask(__name__)
from wiki import getWikiURL
@app.route("/")  # Python decorator
def main():
    movieDetails = getRandomMovie()
    id= getWikiURL(movieDetails["title"] + movieDetails["date"])
    print(id)
    return flask.render_template("index.html", data=movieDetails, id=id)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
)

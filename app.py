import flask
from tmbd import getRandomMovie
app = flask.Flask(__name__)
from wiki import getWikiURL
@app.route("/")  # Python decorator
def main():
    movieDetails = getRandomMovie()
    id= getWikiURL(movieDetails["title"] + movieDetails["date"])
    print(id)
    return flask.render_template("index.html", data=movieDetails, id=id)

app.run(
    debug=True
)

import flask
from tmbd import getRandomMovie
app = flask.Flask(__name__)

@app.route("/")  # Python decorator
def main():
    movieDetails = getRandomMovie()
    print(movieDetails)
    return flask.render_template("index.html", data=movieDetails)

app.run(
    debug=True
)

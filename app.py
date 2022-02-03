import flask
from tmbd import getRandomMovie
app = flask.Flask(__name__)

@app.route("/")  # Python decorator
def main():
    getRandomMovie()
    return flask.render_template("index.html")

app.run(
    debug=True
)
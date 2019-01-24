import flask
from jrReview import app

@app.route('/')
def index():
    return flask.render_template('index.html')

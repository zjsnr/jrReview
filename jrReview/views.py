import flask
from jrReview import app
from jrReview.pages import getPages

@app.route('/')
def index():
    pages = getPages()
    return flask.render_template('index.html', pages=pages)

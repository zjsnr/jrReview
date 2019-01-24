import flask
from flask_bootstrap import Bootstrap

def initApp():
    app = flask.Flask(__name__, instance_relative_config=True)
    # config
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    
    # extensions
    Bootstrap().init_app(app)
    
    return app

app = initApp()

import jrReview.views

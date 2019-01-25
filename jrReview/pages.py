import flask

class Page:
    def __init__(self, title, text, background):
        self.title = title
        self.text = text
        self.background = background

def getPages():
    items = [
        ['title1', 'text1', flask.url_for('static', filename='images/background.png')],
        ['title2', 'text2', flask.url_for('static', filename='images/background.png')]
    ]
    return [Page(*item) for item in items]
    

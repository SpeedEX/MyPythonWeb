__author__ = 'SpeedEX'

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


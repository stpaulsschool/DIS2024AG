from app import app
from flask import render_template
#@app.route('/')
#def default():
    #return "<h2> Hello this is the default route"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrew'}
    return render_template("index.html", title='Home',user=user)
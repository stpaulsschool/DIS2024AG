from app import app
from flask import render_template

from Unit1_Create_With_Code.microblog.app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'Fred'},
            'body': 'Beautiful day in Brisbane!'
        },
        {
            'author': {'username': 'Wilma'},
            'body': 'Basketball is the best sport!'
        }
    ]
    return render_template('index.html',title=user['username'], user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


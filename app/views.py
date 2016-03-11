from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():

    user = {'nickname': 'Miguel'}  # mock obj

    # we introduce some posts
    posts = [
        {
            'author': {'nickname': 'John'},
            'body':    'Beautiful day to work'
        },
        {
            'author': {'nickname': 'Susana'},
            'body':    'I like movies'

        }
    ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

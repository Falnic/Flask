from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():

    user = {'nickname': 'Falnic'}  # mock obj

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


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for openId="%s", remember_me=%s'
              %(form.openId.data, str(form.remember_me.data)))
        return redirect('/index')

    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

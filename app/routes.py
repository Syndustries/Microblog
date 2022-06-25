from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route("/")
@app.route("/index")
def index ( ) :
    user = {'username': 'Storm'}
    posts = [
    {
            'author' : {'username': 'Susan'},
            'body' : 'The Avengers movie was so cool!'
    },
    {
            'author': {'username': 'Storm'},
            'body' : 'Something or other as a test placeholder'
    }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
             form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
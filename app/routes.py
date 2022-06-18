from flask import render_template
from app import app

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

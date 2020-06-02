from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rekevin'}
    posts = [
        {
            'title': 'Article 1',
            'body': 'Hello world!'
        },
        {
            'title': 'Article 2',
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

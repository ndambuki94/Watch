from flask import render_template
from app import app


@app.route('/movie/<int:movie_id>')
def index(movie_id):
    '''
    View root page function that returns the index page and its data
    '''
    # message = 'Hello World'
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template('index.html',title = title)
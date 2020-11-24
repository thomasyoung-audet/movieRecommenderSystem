from flask import Flask

app = Flask(__name__)


@app.route('/')
def display():
    return 'This is a basic empty page'


@app.route('/content_based')
def display():
    return 'This will be the page where we demo the content based recommender'


@app.route('/user_based')
def display():
    return 'This will be the page where we demo the user based recommender'

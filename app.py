from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/item_based')
def content_based():
    return render_template('item_based.html')


@app.route('/user_based')
def user_based():
    return render_template('item_based.html')

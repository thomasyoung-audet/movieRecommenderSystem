from flask import Flask, render_template, redirect, url_for, request
from forms import MovieForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'


@app.route('/', methods=('GET', 'POST'))
def index():
    form = MovieForm()
    if form.is_submitted():
        movie1 = form.movie1.data
        movie2 = form.movie2.data
        movie3 = form.movie3.data
        movie4 = form.movie4.data
        movie5 = form.movie5.data
        movie6 = form.movie6.data
        movie7 = form.movie7.data
        movie8 = form.movie8.data
        movie9 = form.movie9.data
        movie10 = form.movie10.data
        print(movie1)
        print(movie2)
        if form.submit_item_based.data:
            return redirect(url_for('item_based'))
        if form.submit_user_based.data:
            return redirect(url_for('user_based'))

    return render_template('base.html', form=form)


@app.route('/item_based')
def content_based():
    return render_template('item_based.html')


@app.route('/user_based')
def user_based():
    return render_template('user_based.html')

from flask import Flask, render_template, redirect, url_for, request
from forms import MovieForm
import userBased
import pandas as pd
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
movies = dict()


def get_movie_names():
    movie_title_list = pd.read_csv('movies.csv')['title'].tolist()
    titles = random.sample(movie_title_list, k=10)
    return titles


@app.route('/', methods=('GET', 'POST'))
def index():
    movie_titles = get_movie_names()
    form = MovieForm(movie_titles)
    if form.validate_on_submit():
        movie1 = form.movie1.data
        movies[movie_titles[0]] = movie1
        movie2 = form.movie2.data
        movies[movie_titles[0]] = movie2
        movie3 = form.movie3.data
        movies[movie_titles[0]] = movie3
        movie4 = form.movie4.data
        movies[movie_titles[0]] = movie4
        movie5 = form.movie5.data
        movies[movie_titles[0]] = movie5
        movie6 = form.movie6.data
        movies[movie_titles[0]] = movie6
        movie7 = form.movie7.data
        movies[movie_titles[0]] = movie7
        movie8 = form.movie8.data
        movies[movie_titles[0]] = movie8
        movie9 = form.movie9.data
        movies[movie_titles[0]] = movie9
        movie10 = form.movie10.data
        movies[movie_titles[0]] = movie10
        print(movie1)
        print(movie2)
        if form.submit_item_based.data:
            return redirect(url_for('user_based', result_data=movies))  # i don't know why but I have to switch these...
        if form.submit_user_based.data:
            return redirect(url_for('item_based', result_data=movies))

    return render_template('recommender.html', form=form, titles=movie_titles)


@app.route('/item_based')
def item_based(result_data=None):
    return render_template('item_based.html')


@app.route('/user_based')
def user_based(result_data=None):
    recommended_movies = userBased.create_user_based_rating(result_data)
    print(recommended_movies)
    return render_template('user_based.html', result=recommended_movies)

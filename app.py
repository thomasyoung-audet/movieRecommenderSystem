from flask import Flask, render_template, redirect, url_for, request, flash
from forms import MovieForm
import userBased
import itemBased
import pandas as pd
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'


def get_movie_names():
    rating_data = pd.read_csv('ratings.csv')
    movie_data = pd.read_csv('movies.csv')
    user_movie_rating = pd.merge(rating_data, movie_data, on='movieId')
    common_movie_title_list = user_movie_rating['title'].value_counts()[:10].index.tolist()
    return common_movie_title_list


@app.route('/', methods=('GET', 'POST'))
def index():
    movies = dict()
    movie_titles = get_movie_names()
    form = MovieForm()
    if form.validate_on_submit():
        movie1 = form.movie1.data
        movies[movie_titles[0]] = movie1
        movie2 = form.movie2.data
        movies[movie_titles[1]] = movie2
        movie3 = form.movie3.data
        movies[movie_titles[2]] = movie3
        movie4 = form.movie4.data
        movies[movie_titles[3]] = movie4
        movie5 = form.movie5.data
        movies[movie_titles[4]] = movie5
        movie6 = form.movie6.data
        movies[movie_titles[5]] = movie6
        movie7 = form.movie7.data
        movies[movie_titles[6]] = movie7
        movie8 = form.movie8.data
        movies[movie_titles[7]] = movie8
        movie9 = form.movie9.data
        movies[movie_titles[8]] = movie9
        movie10 = form.movie10.data
        movies[movie_titles[9]] = movie10
        print(movies)
        if form.submit_item_based.data:
            print("item was true")
            return redirect(url_for('user_based', result_data=movies))
        if form.submit_user_based.data:
            print("user was true")
            return redirect(url_for('item_based', result_data=movies))

    return render_template('recommender.html', form=form, titles=movie_titles)


@app.route('/item_based')
def item_based():
    result_data = request.args.get('result_data', None)
    print("========================")
    print(result_data)
    if result_data:
        print("Result data passed")
        recommended_movies = itemBased.create_item_based_rating(result_data)
        print(recommended_movies)
    else:
        print("Result data not being passed correctly")
    return render_template('item_based.html', result=[recommended_movies.to_html(classes='data')])


@app.route('/user_based')
def user_based():
    result_data = request.args.get('result_data', None)
    movies = eval(result_data)  # this is necessary because the data gets passed as a string from the previous page
    for key, value in movies.items():
        movies[key] = int(value)  # turns the values from the dict into ints: from '3' to 3 etc
    print("========================")
    print(type(movies))
    if result_data:
        print("Result data passed")
        recommended_movies = userBased.create_user_based_rating(movies)
        top_movies = recommended_movies[0:15]
        worst_movies = recommended_movies[-10:]  # you can try doing stuff with these two, could be interesting
        total_movies = len(recommended_movies)  # number of movies in csv.
        print(recommended_movies)
    else:
        print("Result data not being passed correctly")
        top_movies = ['data was not passed correctly']
    return render_template('display_results.html', result=top_movies)

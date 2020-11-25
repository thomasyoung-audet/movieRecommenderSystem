from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd
import random


def get_movie_names():
    movie_title_list = pd.read_csv('movies.csv')['title'].tolist()
    titles = random.sample(movie_title_list, k=10)
    return titles


class MovieForm(FlaskForm):
    movie_names = get_movie_names()
    """Movie rating form."""
    movie1 = StringField(movie_names[0], [DataRequired()])
    movie2 = StringField(movie_names[1], [DataRequired()])
    movie3 = StringField(movie_names[2], [DataRequired()])
    movie4 = StringField(movie_names[3], [DataRequired()])
    movie5 = StringField(movie_names[4], [DataRequired()])
    movie6 = StringField(movie_names[5], [DataRequired()])
    movie7 = StringField(movie_names[6], [DataRequired()])
    movie8 = StringField(movie_names[7], [DataRequired()])
    movie9 = StringField(movie_names[8], [DataRequired()])
    movie10 = StringField(movie_names[9], [DataRequired()])
    submit_item_based = SubmitField('Calculate recommendations - User-based algorithm')
    submit_user_based = SubmitField('Calculate recommendations - Item-based algorithm')



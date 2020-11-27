import pandas as pd
import ast


def create_item_based_rating(movies):  # movies type dict
    movies = str(movies)
    rating_data = pd.read_csv('ratings.csv')
    movie_data = pd.read_csv('movies.csv')
    user_movie_rating = pd.merge(rating_data, movie_data, on='movieId')
    user_movie_rating_p = user_movie_rating.pivot_table('rating', index='userId', columns='title').fillna(0)

    fav_movie = []
    movies_dict = ast.literal_eval(movies)
    for item in movies_dict:
        if int(movies_dict.get(item)) >= 3:
            fav_movie.append(item)
    print("movies to search similar movies: ", fav_movie)
    recommendation = []
    for movie in fav_movie:
        result = sim_cal(user_movie_rating_p, movie)
        result_df = pd.DataFrame(data=result[movie].sort_values(ascending=False)[:10])
        recommendation.append(result_df)
    return recommendation


def sim_cal(df, movie):  # movie that we want to calculate cos_sim with other movies
    df = df[df[movie] != 0]  # delete row that contain 0 in the movie col
    return df.corr(method='pearson')
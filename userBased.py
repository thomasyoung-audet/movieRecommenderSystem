import pandas as pd
from scipy.stats.stats import pearsonr
import operator


def create_user_based_rating(sampling):
    rating_data = pd.read_csv('ratings.csv')
    movie_data = pd.read_csv('movies.csv')
    user_movie_rating = pd.merge(rating_data, movie_data, on='movieId')
    user_movie_rating_p = user_movie_rating.pivot_table('rating', index='userId', columns='title').fillna(0)

    # add user to df
    s = pd.DataFrame([sampling])
    print(s)
    user_movie_rating_p = user_movie_rating_p.append(s, ignore_index=True).fillna(0)

    # create arrays of titles where both user and input have non zero values
    common_movies_dict = dict()
    for i in range(user_movie_rating_p.shape[0] - 300):  # -1
        for j in range(user_movie_rating_p.shape[1]):
            if user_movie_rating_p.iat[i,j] != 0 and user_movie_rating_p.iat[-1,j] != 0:  # both we and a user have a movie rating in common
                if i in common_movies_dict.keys():
                    common_movies_dict[i][0].append(user_movie_rating_p.iat[i,j])
                    common_movies_dict[i][1].append(user_movie_rating_p.iat[-1,j])
                else:
                    common_movies_dict[i] = [user_movie_rating_p.iat[i,j]], [user_movie_rating_p.iat[-1,j]]
        # calculate pearson coeff between user i and our entries
        if i in common_movies_dict.keys():
            if len(common_movies_dict[i][0]) > 1:  # can't calculate if only 1 common rating
                pearson_coeff = pearsonr(common_movies_dict[i][0], common_movies_dict[i][1])
                # take subset of users that are similar (correlation > 0.3?)
                if pearson_coeff[0] >= 0.1:
                    common_movies_dict[i] = pearson_coeff[0]
                else:
                    del common_movies_dict[i]
            else:
                del common_movies_dict[i]

    # calculate relevance of all other movies to us
    relevance_dict = dict()
    for movie in list(user_movie_rating_p.columns):
        # find similar users who have rated the movie
        similar_users = dict()
        for user in common_movies_dict.keys():
            if user_movie_rating_p.at[user, movie] != 0:
                similar_users[user] = user_movie_rating_p.at[user, movie]
        # do calculation
        if similar_users:
            sim_score_sum = 0
            weighted_rating = 0
            for user, rating in similar_users.items():
                sim_score_sum += common_movies_dict[user]
                weighted_rating += common_movies_dict[user]*rating

            relevance_dict[movie] = 1/sim_score_sum*weighted_rating

    sorted_dict = sorted(relevance_dict.items(), key=operator.itemgetter(1), reverse=True)
    print("best movies:")
    print(sorted_dict[0:30])
    print("worst movies:")
    print(sorted_dict[-10:])
    print("total movies evaluated:")
    print(len(sorted_dict))
    return sorted_dict  # [0:15]


if __name__ == "__main__":
    a = {'Forrest Gump (1994)': 2, 'Pulp Fiction (1994)': 4, 'Shawshank Redemption, The (1994)': 3, 'Silence of the Lambs, The (1991)': 5,
         'Star Wars: Episode IV - A New Hope (1977)': 2, 'Jurassic Park (1993)': 3, 'Matrix, The (1999)': 1,
         'Toy Story (1995)': 5, "Schindler's List (1993)": 4, 'Terminator 2: Judgment Day (1991)': 2}
    create_user_based_rating(a)

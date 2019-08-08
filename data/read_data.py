import os
import pandas as pd

now_path = os.path.split(__file__)

# print("当前路径：", now_path[0])


def get_movies(dir_path):
    movies_ = os.path.join(dir_path, "ml-1m/movies.dat")
    df_movies = pd.read_table(movies_, header=None, sep="::", engine='python')
    df_movies.columns = "MovieID::Title::Genres".split("::")
    return df_movies


def get_ratings(dir_path):
    ratings_ = os.path.join(dir_path, "ml-1m/ratings.dat")
    df_ratings = pd.read_table(ratings_, header=None, sep="::", engine='python')
    df_ratings.columns = "UserID::MovieID::Rating::Timestamp".split("::")
    return df_ratings


def get_users(dir_path):
    users_ = os.path.join(dir_path, "ml-1m/users.dat")
    df_users = pd.read_table(users_, header=None, sep="::", engine='python')
    df_users.columns = "UserID::Gender::Age::Occupation::Zip-code".split("::")
    return df_users


movies = get_movies(dir_path=now_path[0])
users = get_users(dir_path=now_path[0])
ratings = get_ratings(dir_path=now_path[0])


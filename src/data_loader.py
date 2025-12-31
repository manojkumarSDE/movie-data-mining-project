import pandas as pd

def load_data():
    movies = pd.read_csv("data/Movies.csv")
    ratings = pd.read_csv("data/Ratings.csv")
    users = pd.read_csv("data/Users.csv")

    movies['Year'] = movies['Title'].str.extract(r'\((\d{4})\)').astype(int)
    movies['Category'] = movies['Category'].str.split('|')
    movies = movies.explode('Category')

    merged = ratings.merge(movies, on='MovieID') \
                    .merge(users, on='UserID')

    return movies, merged

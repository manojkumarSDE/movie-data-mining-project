def movies_per_year(movies):
    return movies.groupby('Year')['MovieID'].count()

def top_category_each_year(data):
    avg = data.groupby(['Year','Category'])['Rating'].mean().reset_index()
    return avg.loc[avg.groupby('Year')['Rating'].idxmax()]

def category_age_likes(data):
    likes = data.groupby(['Age','Category'])['UserID'].nunique().reset_index()
    return likes.loc[likes.groupby('Age')['UserID'].idxmax()]

def year_category_count(movies):
    return movies.groupby(['Year','Category'])['MovieID'].count()

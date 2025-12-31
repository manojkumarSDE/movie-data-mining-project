from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
import numpy as np

def cluster_age_category(data):
    df = data.groupby(['Age','Category'])['Rating'].mean().reset_index()
    enc = OneHotEncoder()
    cat_enc = enc.fit_transform(df[['Category']]).toarray()

    X = np.hstack([df[['Age']].values, cat_enc])
    df['Cluster'] = KMeans(n_clusters=4, random_state=42).fit_predict(X)
    return df

def cluster_occupation_category(data):
    df = data.groupby(['Occupation','Category'])['Rating'].mean().reset_index()
    enc = OneHotEncoder()
    cat_enc = enc.fit_transform(df[['Category']]).toarray()

    X = np.hstack([df[['Occupation']].values, cat_enc])
    df['Cluster'] = KMeans(n_clusters=5, random_state=42).fit_predict(X)
    return df

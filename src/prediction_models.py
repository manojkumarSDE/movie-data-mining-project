import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_occ_age_to_category(data):
    X = pd.get_dummies(data[['Occupation','Age']])
    y, labels = pd.factorize(data['Category'])

    model = RandomForestClassifier()
    model.fit(X, y)
    return model, X.columns, labels

def train_category_to_user(data):
    X = pd.get_dummies(data[['Category']])
    age_model = RandomForestClassifier().fit(X, data['Age'])
    occ_model = RandomForestClassifier().fit(X, data['Occupation'])
    return age_model, occ_model, X.columns

from src.analysis import *
from src.clustering import *
from src.prediction_models import *

def menu(movies, data):
    model, cols, labels = train_occ_age_to_category(data)

    while True:
        print("\n1 Movies per Year")
        print("2 Top Category per Year")
        print("3 Category & Age Liking")
        print("4 Predict Category (Occupation + Age)")
        print("5 Exit")

        ch = input("Enter choice: ")

        if ch == '1':
            print(movies_per_year(movies))
        elif ch == '2':
            print(top_category_each_year(data))
        elif ch == '3':
            print(category_age_likes(data))
        elif ch == '4':
            occ = int(input("Occupation: "))
            age = int(input("Age Group: "))
            df = pd.DataFrame({'Occupation':[occ],'Age':[age]})
            df = pd.get_dummies(df).reindex(columns=cols, fill_value=0)
            pred = model.predict(df)
            print("Predicted Category:", labels[pred][0])
        elif ch == '5':
            break

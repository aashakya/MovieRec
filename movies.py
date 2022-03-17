# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:00:06 2022

@author: ashakya
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_csv("movie_list.csv")
#adding a numerical genre column
genre_num =[]
genre = df["Genre"]
for i in range(len(genre)):
    if(genre[i] == "Action"):
        genre_num.append(0)
    elif (genre[i] == "Adventure"):
        genre_num.append(10)
    elif (genre[i] == "Thriller"):
        genre_num.append(20)  
    elif (genre[i] == "Mystery"):
        genre_num.append(30)
    elif (genre[i] == "Sci-Fi"):
        genre_num.append(40)
    elif (genre[i] == "Kids and Family"):
        genre_num.append(50)
    elif (genre[i] == "Comedy"):
        genre_num.append(60)
    elif (genre[i] == "Romance"):
        genre_num.append(70)
    elif (genre[i] == "Music"):
        genre_num.append(80)
    elif (genre[i] == "Musical"):
        genre_num.append(90)
    else:
        genre_num.append(100)
df["genreNum"] = genre_num

# genreNum dictionary

# 2D plot of the data
def coloring(C):
    if(C==1):
        color = "green"
    else:
        color ="red"
    return (color)
df["color"]=df['Class'].apply(coloring)
p = figure(x_axis_label='GenreNum', y_axis_label='Rating')
p.circle(df['genreNum'],df['Rating'],color=df['color'],size=5)
output_file('plot.html')
show(p)

# KNN decision system
X = df.drop("Class", axis = 1)
X = X.drop("Movie Name", axis = 1)
X = X.drop("Length(mins)", axis = 1)
X = X.drop("Genre", axis = 1)
X = X.drop("Genre 2", axis = 1)
X = X.drop("color", axis = 1)

Y = df["Class"]
n = 3

def KNNfunc(rating,genreNumber,movie):
    neigh = KNeighborsClassifier(n_neighbors = n)
    neigh.fit(X.values,Y)
    KNeighborsClassifier(...)
    testcase = [rating, genreNumber]
    pred_val = neigh.predict([testcase])
    if (pred_val == 0):
        print('Not recommended to watch')
    else:
        print('Recommended to watch')
    prob = neigh.predict_proba([testcase])
    print("The probabily of liking",movie,"is",round(prob[0,1],2))
    print("\n")

genreDict = {
    "Action": 0,
    "Adventure": 10,
    "Thriller": 20,
    "Mystery": 30,
    "Sci-Fi": 40,
    "Kids and Family": 50,
    "Comedy": 60,
    "Romance": 70,
    "Music": 80,
    "Musical": 90,
    "Biography": 100
    }
n = 3

KNNfunc(75, 70,"Grease")
KNNfunc(99, 40, "Finding Nemo")
KNNfunc(89, 70, "Titanic")
KNNfunc(98, 0, "Jaws")
KNNfunc(78, 50, "Rudy")
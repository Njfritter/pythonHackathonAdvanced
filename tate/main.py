import sqlite3
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import tensorflow as tf

def clean_frame(frame):
    numeric_frame = frame._get_numeric_data()
    numeric_frame[numeric_frame < 0.0] = np.nan
    for column in numeric_frame:
        numeric_frame[column][np.isnan(frame[column])] = numeric_frame[column].min()

def normalize_frame(frame):
    numeric_frame = frame._get_numeric_data()
    for index, column in enumerate(numeric_frame):
        if index < len(numeric_frame.columns.values) - 1:
            max_val = numeric_frame[column].max()
            min_val = numeric_frame[column].min()
            numeric_frame[column] = (numeric_frame[column] - min_val) / (max_val - min_val)

connection = sqlite3.connect("../wine.db")

red = connection.execute("SELECT * FROM mainTable WHERE wine_class='red'")
white = connection.execute("SELECT * FROM mainTable WHERE wine_class='white'")

red_rows = red.fetchall()
white_rows = white.fetchall()

red_dataframe = pd.DataFrame(red_rows, columns=list(zip(*red.description))[0])
white_dataframe = pd.DataFrame(white_rows, columns=list(zip(*white.description))[0])

clean_frame(red_dataframe)
clean_frame(white_dataframe)
normalize_frame(red_dataframe)
# normalize_frame(white_dataframe)

red_explanatory = red_dataframe._get_numeric_data().ix[:, 0:11]
red_response = red_dataframe._get_numeric_data().ix[12]
print(red_response)
# white_numeric = white_dataframe._get_numeric_data()

pca = PCA(n_components=4)
red_transformed = pca.fit_transform(red_explanatory)


plt.scatter(red_transformed[:,0], red_transformed[:,1])
plt.show()

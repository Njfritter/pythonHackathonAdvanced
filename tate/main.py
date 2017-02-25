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
    numeric_frame = frame._get_numeric_data()[0:10]
    for index, column in enumerate(numeric_frame):
        if index < len(numeric_frame):
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

# red_explanatory = red_dataframe._get_numeric_data().ix[:, 0:11]
# print(red_explanatory.columns)
# red_response = red_dataframe._get_numeric_data().ix[12]
# # white_numeric = white_dataframe._get_numeric_data()
# pca = PCA(n_components=4)
# pca.fit(red_explanatory)
#
#
# fig, plot = plt.subplots()
# fig.set_size_inches(50, 50)
# plt.prism()
#
# red_transformed = pca.fit_transform(red_explanatory)
# print(pca.explained_variance_ratio_)
# plot.scatter(red_transformed[:, 0], red_transformed[:, 1], c = red_response)
# plot.set_xticks(())
# plot.set_yticks(())
#
# plt.tight_layout()
# plt.show()

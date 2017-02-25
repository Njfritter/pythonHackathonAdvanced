import sqlite3
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import tensorflow as tf

def clean_frame(frame):
    numeric_frame = frame._get_numeric_data()
    numeric_frame[numeric_frame < 0.0] = np.nan
    for column in numeric_frame:
        numeric_frame[column][np.isnan(frame[column])] = numeric_frame[column].min()

def normalize_frame(frame):
    numeric_frame = frame._get_numeric_data()
    for column in numeric_frame:
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
normalize_frame(white_dataframe)

red_numeric = red_dataframe._get_numeric_data()
white_numeric = white_dataframe._get_numeric_data()
pca = PCA(n_components=4)
pca.fit(red_numeric.ix[:, 0:11])
print(red_numeric.ix[:, 0:11])
print(pca.components_)

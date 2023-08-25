import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split as tt_split

df = pd.read_csv("../data/conversion_rgb_temp_full.csv", sep=";")
X = df.loc[0:]
Y = df.loc[:0]

model = RandomForestRegressor(n_estimators= 100, n_jobs=-1)

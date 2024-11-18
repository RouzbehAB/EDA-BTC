import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

btc = yf.download("BTC-USD", start="2015-01-01", end="2022-12-31")
df = pd.DataFrame(btc)

weekday = df.index.weekday
df["weekday"] = weekday


sunday = df["weekday"] == 0
wednesday = df["weekday"] == 3


df_sunday = pd.merge(df, sunday, join="inner", on="Date")
df_wednesday = pd.merge(df, wednesday, join="inner", on="Date")
# print(df)




# print(df.describe())
# df.info()
# print(df.head())
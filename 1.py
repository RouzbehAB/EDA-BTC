import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

df = yf.download("BTC-USD", start="2014-01-01", end="2024-01-01")

# sns.heatmap(df.corr(), annot=True, fmt="0.4f", cmap="coolwarm")
plt.boxplot(df.Close,)
# plt.scatter(df["High"], df["Low"])
# plt.scatter(df["Close"], df["Volume"])
# plt.scatter(df["Open"], df["Volume"])
# plt.scatter(df["High"], df["Volume"])
# plt.scatter(df["Low"], df["Volume"])

# sns.pairplot(df,hue="clsoe")
# sns.pairplot(df)
# sns.pairplot(df)
plt.show()




# print(df.describe())
# df.info()
# print(df.head())
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

btc = yf.download("BTC-USD", start="2014-01-01", end="2024-01-01")
df = pd.DataFrame(btc)

weekday = df.index.weekday
df["weekday"] = weekday
# print(weekday)

# print(df.describe())
df.info()
print(df.head())
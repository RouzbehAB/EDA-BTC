import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import pandas as pd

first_capital = 1000
cap_counter = first_capital

df = yf.download("BTC-USD", start="2015-01-01", end="2022-12-31")
df["weekday"]= df.index.weekday

sunday = df[df["weekday"] == 0]
wednesday = df[df["weekday"] == 3]

operation = pd.merge(sunday["Open"], wednesday["Close"], left_index=True, right_index=True, suffixes=["_buy", "_sell"] )

for index, row in operation.iterrows():
    buy_btc = cap_counter / row["Open_buy"]
    cap_counter = buy_btc * row["Close_sell"]
    profit = cap_counter - first_capital
    print(f"Final capital: {cap_counter : 2f} $")

    if profit > 0:
        print("profitable")
    else:
        print("not profitable")







# print(df)




# print(df.describe())
# df.info()
# print(df.head())
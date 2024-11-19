# By copilot ******

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# دانلود داده‌های بیتکوین از یاهو فایننس
btc_data = yf.download("BTC-USD", start="2015-01-01", end="2022-12-31")

# اضافه کردن ستون‌های روز یکشنبه و چهارشنبه
btc_data['Sunday'] = btc_data.index.to_series().apply(lambda x: x.weekday() == 6)
btc_data['Wednesday'] = btc_data.index.to_series().apply(lambda x: x.weekday() == 2)

# فیلتر کردن داده‌های یکشنبه‌ها و چهارشنبه‌ها
sundays = btc_data[btc_data['Sunday']]
wednesdays = btc_data[btc_data['Wednesday']]

# متغیرهای اولیه برای حساب سود یا زیان
initial_investment = 1000
cash = initial_investment
btc_held = 0

# محاسبه سود یا زیان با خرید در یکشنبه‌ها و فروش در چهارشنبه‌ها
for sunday, wednesday in zip(sundays.iterrows(), wednesdays.iterrows()):
    buy_price = sunday[1]['Open']
    sell_price = wednesday[1]['Close']

    # خرید در یکشنبه
    btc_bought = cash / buy_price
    btc_held += btc_bought
    cash = 0

    # فروش در چهارشنبه
    cash = btc_held * sell_price
    btc_held = 0

# محاسبه سود یا زیان نهایی
final_value = cash
profit_loss = final_value - initial_investment

print(f"Initial Investment: ${initial_investment}")
print(f"Final Value: ${final_value}")
print(f"Profit/Loss: ${profit_loss}")

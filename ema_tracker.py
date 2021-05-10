import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


def calculate_ema(prices, days, smoothing=2):
    ema = [sum(prices[:days]) / days]
    for price in prices[days:]:
        ema.append((price * (smoothing / (1 + days))) +
                   ema[-1] * (1 - (smoothing / (1 + days))))
    return ema


symbol = 'PFE'
df = web.DataReader(symbol, 'yahoo', '2021-05-01', '2021-05-10')

# Add this line to save EMA values in a list
ema = calculate_ema(df['Close'], 10)
print(ema)
# Creates array [0, 1, 2, 3, ..., df.shape[0]]
price_X = np.arange(df.shape[0])
# Creates array [10, 11, 12, 13, ..., df.shape[0]+1]
ema_X = np.arange(10, df.shape[0]+1)
# We start at 10, because we use the first 10 values to calculate the SMA,
# then we calculate EMA form the 11th value

plt.xlabel('Days')
plt.ylabel('Price')
plt.plot(price_X, df['Close'], label='Closing Prices')
plt.plot(ema_X, ema, label='EMA')
plt.legend()
plt.show()

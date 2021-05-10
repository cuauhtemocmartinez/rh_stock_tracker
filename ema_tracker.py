import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


def calculate_ema(prices, days, smoothing=2):
    pass


symbol = 'MSFT'
df = web.DataReader(symbol, 'yahoo', '2021-01-01', '2016-05-10')


def calculate_ema(prices, days, smoothing=2):
    ema = [sum(prices[:days]) / days]  # First method
    ################################################
    ema = []
    ema.append(sum(prices[:days]) / days)  # Second method


def calculate_ema(prices, days, smoothing=2):
    ema = [sum(prices[:days]) / days]
    for price in prices[days:]:
        ema.append((price * (smoothing / (1 + days))) +
                   ema[-1] * (1 - (smoothing / (1 + days))))
    return ema

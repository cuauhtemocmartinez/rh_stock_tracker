import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


def calculate_ema(prices, days, smoothing=2):
    pass


symbol = 'MSFT'
df = web.DataReader(symbol, 'yahoo', '2015-01-01', '2016-01-01')

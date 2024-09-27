import pandas as pd
import numpy as np

def calculate_ema(data, span):
    return data.ewm(span=span, adjust=False).mean()

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(window=window).mean()
    avg_loss = pd.Series(loss).rolling(window=window).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calculate_bollinger_bands(data, window=20, std_dev=2):
    middle_band = data.rolling(window=window).mean()
    std = data.rolling(window=window).std()
    upper_band = middle_band + (std * std_dev)
    lower_band = middle_band - (std * std_dev)
    return upper_band, middle_band, lower_band

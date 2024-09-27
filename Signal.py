def generate_otc_signals(data):
    data['Signal'] = 0
    data.loc[data['EMA_9'] > data['EMA_21'], 'Signal'] = 1  # Buy signal
    data.loc[data['EMA_9'] < data['EMA_21'], 'Signal'] = 0  # Sell signal
    data.loc[data['RSI'] > 70, 'Signal'] = 0  # Overbought signal
    data.loc[data['RSI'] < 30, 'Signal'] = 1  # Oversold signal
    return data

def generate_live_signals(data):
    data['Signal'] = 0
    data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  # Golden Cross Buy signal
    data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = 0  # Death Cross Sell signal
    data.loc[data['MACD'] > data['MACD_signal'], 'Signal'] = 1  # MACD Buy signal
    data.loc[data['MACD'] < data['MACD_signal'], 'Signal'] = 0  # MACD Sell signal
    return data

def generate_commodities_signals(data):
    data['Signal'] = 0
    data.loc[data['Close'] < data['Bollinger_Lower'], 'Signal'] = 1  # Buy signal
    data.loc[data['Close'] > data['Bollinger_Upper'], 'Signal'] = 0  # Sell signal
    return data

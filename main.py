from binary_bot import MarketSignalGenerator
from indicators import calculate_ema, calculate_sma, calculate_rsi, calculate_bollinger_bands
from Signal import generate_otc_signals, generate_live_signals, generate_commodities_signals

# Example data (Randomly generated for demonstration purposes)
import pandas as pd
import numpy as np

dates = pd.date_range('2023-01-01', periods=100, freq='H')  # Hourly data
close_prices = np.random.normal(loc=100, scale=5, size=(100,))
data = pd.DataFrame({'Close': close_prices}, index=dates)

# Specify the market type: 'OTC', 'Live', or 'Commodities'
market_type = 'Live'

# Initialize and run the signal generator
generator = MarketSignalGenerator(data, market_type)
generator.calculate_indicators()
generator.generate_signals()
accuracy = generator.backtest_strategy()

print(f"Strategy Accuracy for {market_type} market: {accuracy:.2f}%")
generator.visualize_signals()

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load data
df = pd.read_csv("stock_prices.csv", index_col=0, parse_dates=True)

# Use only closing prices
prices = df["close"].values.reshape(-1, 1)

# Normalize prices
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_prices = scaler.fit_transform(prices)

# Split into train & test
train_size = int(len(scaled_prices) * 0.8)
train_data, test_data = scaled_prices[:train_size], scaled_prices[train_size:]

# Save preprocessed data
np.save("train_data.npy", train_data)
np.save("test_data.npy", test_data)
np.save("scaler.npy", scaler)  # Save scaler to reverse transformation later

print("Preprocessed data saved successfully!")

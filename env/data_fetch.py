import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "IC9UV19SE7O91WHY"
STOCK_SYMBOL = "AAPL"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&apikey={API_KEY}&outputsize=compact&datatype=json"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["Time Series (Daily)"]).T
df.columns = ["open", "high", "low", "close", "volume"]
df = df.astype(float)
df.index = pd.to_datetime(df.index)

# Save data to CSV
df.to_csv("stock_prices.csv")
print("Stock data saved to stock_prices.csv")

# Plot closing prices
df["close"].plot(figsize=(10, 5), title=f"{STOCK_SYMBOL} Closing Prices", grid=True)
plt.show()
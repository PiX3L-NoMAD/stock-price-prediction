import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# ✅ Force TensorFlow to use CPU only (fix GPU error)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Load preprocessed test data and scaler
test_data = np.load("test_data.npy")
scaler = np.load("scaler.npy", allow_pickle=True).item()

# Load the trained model (without compilation)
model = tf.keras.models.load_model("stock_price_model.keras", compile=False)

# Prepare test inputs and true values
X_test, y_test = test_data[:-1], test_data[1:]

# Make predictions
predictions = model.predict(X_test)

# Reverse normalization
predicted_prices = scaler.inverse_transform(predictions)
actual_prices = scaler.inverse_transform(y_test)

# Plot actual vs predicted prices
plt.figure(figsize=(12, 6))
sns.lineplot(x=range(len(actual_prices)), y=actual_prices.flatten(), label="Actual Prices")
sns.lineplot(x=range(len(predicted_prices)), y=predicted_prices.flatten(), label="Predicted Prices", linestyle="dashed")
plt.title("Stock Price Prediction")
plt.legend()

# ✅ Fix: Save plot instead of showing it
plt.savefig("prediction_plot.png")  
print("Plot saved as prediction_plot.png ✅")

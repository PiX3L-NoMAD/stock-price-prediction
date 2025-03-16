import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load preprocessed data
train_data = np.load("train_data.npy")
test_data = np.load("test_data.npy")

# Prepare data for supervised learning
X_train, y_train = train_data[:-1], train_data[1:]
X_test, y_test = test_data[:-1], test_data[1:]

# Build a simple neural network
model = keras.Sequential([
    keras.layers.Dense(32, activation="relu", input_shape=(1,)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1)  # Output layer for price prediction
])

# Compile the model (explicitly define loss function)
model.compile(optimizer="adam", loss=keras.losses.MeanSquaredError())

# Train the model
history = model.fit(X_train, y_train, epochs=500, batch_size=8, validation_data=(X_test, y_test), verbose=1)

# Save the trained model in the new Keras format
model.save("stock_price_model.keras")  
print("Model saved as stock_price_model.keras ✅")

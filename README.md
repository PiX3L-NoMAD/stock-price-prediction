# Setting Up the Virtual Environment

Follow these steps to create a virtual environment and install dependencies.

## 1. Create a Virtual Environment

Run the following command in your project directory:

- **For macOS/Linux:**
  ```sh
  python3 -m venv env
  ```
- **For Windows:**
  ```sh
  python -m venv env
  ```

## 2. Activate the Virtual Environment

- **On macOS/Linux:**
  ```sh
  source env/bin/activate
  ```
- **On Windows:**
  ```sh
  env\Scripts\activate
  ```

Once activated, your terminal prompt should change, indicating that the environment is active.

## 3. Install Dependencies

With the virtual environment activated, install the required dependencies:

```sh
pip install -r requirements.txt
```

## 4. Deactivate the Virtual Environment

When you're done, deactivate the environment by running:

```sh
deactivate
```

This setup ensures your project runs in an isolated environment, preventing conflicts with system-wide packages.

# Running the Project

Follow these steps to fetch data, preprocess it, train the model, and make predictions.

## 1. Fetch Data
Run the following command to fetch the required data:
```sh
python fetch_data.py
```

## 2. Preprocess Data
Prepare the data for training by running:
```sh
python preprocess.py
```

## 3. Train the Model
Train the model using 500 epochs (or modify the number as needed):
```sh
python train_model.py
```

## 4. Make Predictions
Run the following command to generate predictions:
```sh
python predict.py
```
This will create a `prediction_plot.png` file, displaying a graph comparing how well the model predicted the last 20% of the data it was given.


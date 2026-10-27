# stock_price_case_study.py
# Case study: predict the next day's closing price from the previous 5 days.
# We generate a made-up price series so the file runs offline.
# NOTE: real stock markets are very hard to predict. This is a learning exercise only.
# Command:  python stock_price_case_study.py

import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error

# 1) Create 300 days of fake prices: slow upward trend + wave + small noise
rng = np.random.default_rng(7)
days = np.arange(300)
prices = 100 + 0.2 * days + 5 * np.sin(days / 10) + rng.normal(0, 0.3, 300)
data = pd.DataFrame({"close": prices})

# 2) Work with daily CHANGES (today - yesterday). Changes stay in a similar range
#    even when the price itself keeps rising, which makes learning much easier.
data["change"] = data["close"].diff()

# 3) Build features: the last 5 daily changes ("lags")
window = 5
for lag in range(1, window + 1):
    data[f"change_lag_{lag}"] = data["change"].shift(lag)
data = data.dropna()                       # first rows have no full history

feature_columns = [f"change_lag_{i}" for i in range(1, window + 1)]
X = data[feature_columns].values
y = data["change"].values                  # target: tomorrow's change

# 4) Time-series split: train on the past, test on the most recent 60 days (no shuffling!)
X_train, X_test = X[:-60], X[-60:]
y_train, y_test = y[:-60], y[-60:]

# 5) Train a small neural network
model = MLPRegressor(hidden_layer_sizes=(16, 8), max_iter=3000, random_state=7)
model.fit(X_train, y_train)

# 6) Turn predicted changes back into prices: price = yesterday's price + change
yesterday = data["close"].shift(1).values[-60:]
real_prices = data["close"].values[-60:]
predicted_prices = yesterday + model.predict(X_test)
print(f"Network error on last 60 days : {mean_absolute_error(real_prices, predicted_prices):.2f} rupees")

# 7) Compare with the simplest baseline: "tomorrow = today"
print(f"Baseline error (tomorrow=today): {mean_absolute_error(real_prices, yesterday):.2f} rupees")

for real, guess in list(zip(real_prices, predicted_prices))[:5]:
    print(f"  real {real:7.2f}  predicted {guess:7.2f}")

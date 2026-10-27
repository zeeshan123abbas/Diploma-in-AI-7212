# linear_vs_nonlinear.py
# Why a straight line is not always enough.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Data: speed of a car (km/h) and fuel used per 100 km.
# Fuel is high at very low AND very high speeds -> a curve (U-shape).
speed = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
fuel = np.array([9.5, 8.1, 7.0, 6.3, 5.9, 5.8, 6.0, 6.5, 7.2, 8.1, 9.3])

# 1) Fit a straight line
X = speed.reshape(-1, 1)          # sklearn wants a 2-D table: 11 rows x 1 column
line_model = LinearRegression()
line_model.fit(X, fuel)
line_pred = line_model.predict(X)
print("Straight line R2:", round(r2_score(fuel, line_pred), 3))   # close to 0 = bad fit

# 2) Plot the data and the line
plt.figure(figsize=(6, 4))
plt.scatter(speed, fuel, color="black", label="Real data")
plt.plot(speed, line_pred, color="red", label="Straight line")
plt.title("A straight line cannot follow a curve")
plt.xlabel("Speed (km/h)")
plt.ylabel("Fuel (L / 100 km)")
plt.legend()
plt.tight_layout()
plt.savefig("linear_vs_nonlinear.png")
print("Saved linear_vs_nonlinear.png")

# polynomial_regression.py
# Polynomial regression = linear regression on x, x^2, x^3 ... so the line can bend.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

speed = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
fuel = np.array([9.5, 8.1, 7.0, 6.3, 5.9, 5.8, 6.0, 6.5, 7.2, 8.1, 9.3])
X = speed.reshape(-1, 1)

# Step 1: create the extra columns x and x^2 (degree 2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
print("First row before:", X[0], " after:", X_poly[0])   # [20] -> [20, 400]

# Step 2: fit a normal linear regression on the new columns
model = LinearRegression()
model.fit(X_poly, fuel)
print("Intercept:", round(model.intercept_, 3))
print("Coefficients (x, x^2):", model.coef_.round(5))

# Step 3: check how well it fits
pred = model.predict(X_poly)
print("Polynomial R2:", round(r2_score(fuel, pred), 3))   # close to 1 = good fit

# Step 4: predict for a new speed
new_speed = np.array([[65]])
print("Predicted fuel at 65 km/h:", round(model.predict(poly.transform(new_speed))[0], 2))

# Step 5: draw a smooth curve using many x values
smooth_x = np.linspace(20, 120, 200).reshape(-1, 1)
smooth_y = model.predict(poly.transform(smooth_x))
plt.figure(figsize=(6, 4))
plt.scatter(speed, fuel, color="black", label="Real data")
plt.plot(smooth_x, smooth_y, color="green", label="Degree 2 curve")
plt.title("Polynomial regression")
plt.xlabel("Speed (km/h)")
plt.ylabel("Fuel (L / 100 km)")
plt.legend()
plt.tight_layout()
plt.savefig("polynomial_regression.png")
print("Saved polynomial_regression.png")

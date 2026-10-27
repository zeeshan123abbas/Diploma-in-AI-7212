# simple_linear_regression.py
# Fit a straight line  y = a + b*x  and use it to predict
import numpy as np
from scipy import stats

# Step 1: advertising spend (Rs. lakh) and sales (Rs. lakh)
ad_spend = np.array([1, 2, 3, 4, 5, 6])
sales    = np.array([12, 15, 21, 24, 29, 33])

# Step 2: least squares line with scipy
result = stats.linregress(ad_spend, sales)
print("Slope (b)     =", round(result.slope, 3))
print("Intercept (a) =", round(result.intercept, 3))
print("R-squared     =", round(result.rvalue ** 2, 4))

# Step 3: predict sales for a spend of 8 lakh
new_spend = 8
predicted = result.intercept + result.slope * new_spend
print("Predicted sales for 8 lakh spend:", round(predicted, 2))

# Step 4: residual = actual - predicted (should be small and random)
predicted_all = result.intercept + result.slope * ad_spend
residuals = sales - predicted_all
print("Residuals:", np.round(residuals, 2))

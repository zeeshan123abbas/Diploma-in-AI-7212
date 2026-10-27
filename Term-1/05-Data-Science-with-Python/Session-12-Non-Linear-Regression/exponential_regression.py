# exponential_regression.py
# Exponential growth: y = a * e^(b * x). Example: users of a new app each month.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

month = np.array([1, 2, 3, 4, 5, 6, 7, 8])
users = np.array([1200, 1650, 2300, 3100, 4300, 5900, 8200, 11200])

# Step 1: write the formula as a Python function
def exponential(x, a, b):
    return a * np.exp(b * x)

# Step 2: curve_fit finds the best a and b (p0 = starting guess)
params, _ = curve_fit(exponential, month, users, p0=[1000, 0.3])
a, b = params
print(f"Best formula: users = {a:.1f} * e^({b:.3f} * month)")
print("Monthly growth rate:", round((np.exp(b) - 1) * 100, 1), "%")

# Step 3: goodness of fit
pred = exponential(month, a, b)
print("R2:", round(r2_score(users, pred), 4))

# Step 4: forecast the next 2 months
for m in [9, 10]:
    print(f"Forecast month {m}: {exponential(m, a, b):,.0f} users")

# Step 5: plot
smooth = np.linspace(1, 10, 100)
plt.figure(figsize=(6, 4))
plt.scatter(month, users, color="black", label="Real users")
plt.plot(smooth, exponential(smooth, a, b), color="orange", label="Exponential fit")
plt.title("Exponential growth of app users")
plt.xlabel("Month")
plt.ylabel("Users")
plt.legend()
plt.tight_layout()
plt.savefig("exponential_regression.png")
print("Saved exponential_regression.png")

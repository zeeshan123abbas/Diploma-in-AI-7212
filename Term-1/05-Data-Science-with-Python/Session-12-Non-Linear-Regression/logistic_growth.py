# logistic_growth.py
# Logistic (S-shaped) curve: slow start, fast middle, then a ceiling.
# y = L / (1 + e^(-k * (x - x0)))   L = ceiling, k = steepness, x0 = middle point
# Example: % of households in a town with a new internet service over the years.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

year = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
percent = np.array([2, 4, 7, 13, 24, 39, 55, 68, 77, 82, 85])

def logistic(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

params, _ = curve_fit(logistic, year, percent, p0=[90, 1, 5])
L, k, x0 = params
print(f"Ceiling L = {L:.1f}%  steepness k = {k:.2f}  middle year x0 = {x0:.1f}")
print("Predicted % in year 12:", round(logistic(12, L, k, x0), 1))

smooth = np.linspace(0, 14, 200)
plt.figure(figsize=(6, 4))
plt.scatter(year, percent, color="black", label="Real data")
plt.plot(smooth, logistic(smooth, L, k, x0), color="purple", label="Logistic fit")
plt.axhline(L, color="gray", linestyle="--", label="Ceiling")
plt.title("S-shaped adoption curve")
plt.xlabel("Year")
plt.ylabel("Households (%)")
plt.legend()
plt.tight_layout()
plt.savefig("logistic_growth.png")
print("Saved logistic_growth.png")

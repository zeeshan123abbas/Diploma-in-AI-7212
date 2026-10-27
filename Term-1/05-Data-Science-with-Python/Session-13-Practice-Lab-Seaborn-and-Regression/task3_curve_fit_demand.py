# task3_curve_fit_demand.py  (Practice for Session 12)
# Task: electricity demand of a growing housing society. Fit exponential AND logistic, compare.

import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

year = np.arange(0, 12)
demand_mw = np.array([5, 6.5, 8.6, 11.2, 14.5, 18.3, 22.4, 26.0, 28.9, 30.8, 32.0, 32.7])

def exponential(x, a, b):
    return a * np.exp(b * x)

def logistic(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

exp_params, _ = curve_fit(exponential, year, demand_mw, p0=[5, 0.2])
log_params, _ = curve_fit(logistic, year, demand_mw, p0=[35, 0.5, 5])

exp_r2 = r2_score(demand_mw, exponential(year, *exp_params))   # *params unpacks the list
log_r2 = r2_score(demand_mw, logistic(year, *log_params))
print("Exponential R2:", round(exp_r2, 3))
print("Logistic    R2:", round(log_r2, 3))

print("\nForecast for year 15:")
print("  Exponential:", round(exponential(15, *exp_params), 1), "MW")
print("  Logistic:   ", round(logistic(15, *log_params), 1), "MW")
print("\nThe demand is levelling off, so the logistic model is more realistic.")

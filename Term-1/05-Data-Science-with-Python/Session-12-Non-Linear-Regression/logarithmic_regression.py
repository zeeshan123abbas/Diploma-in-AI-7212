# logarithmic_regression.py
# Logarithmic curve: y = a + b * ln(x). Fast rise first, then slows down.
# Example: marks improve quickly with the first hours of practice, then level off.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

practice_hours = np.array([1, 2, 4, 6, 8, 12, 16, 20, 25, 30])
score = np.array([35, 47, 58, 64, 68, 73, 77, 79, 81, 83])

def logarithmic(x, a, b):
    return a + b * np.log(x)        # np.log = natural log (ln)

params, _ = curve_fit(logarithmic, practice_hours, score)
a, b = params
print(f"Best formula: score = {a:.2f} + {b:.2f} * ln(hours)")
print("R2:", round(r2_score(score, logarithmic(practice_hours, a, b)), 4))
print("Predicted score after 40 hours:", round(logarithmic(40, a, b), 1))

smooth = np.linspace(1, 40, 200)
plt.figure(figsize=(6, 4))
plt.scatter(practice_hours, score, color="black", label="Real scores")
plt.plot(smooth, logarithmic(smooth, a, b), color="blue", label="Log fit")
plt.title("Diminishing returns of practice")
plt.xlabel("Practice hours")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("logarithmic_regression.png")
print("Saved logarithmic_regression.png")

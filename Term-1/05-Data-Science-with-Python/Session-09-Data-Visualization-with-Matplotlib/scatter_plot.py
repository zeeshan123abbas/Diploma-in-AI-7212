# scatter_plot.py
# Scatter plot = is there a relationship between two numeric columns?

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=3)
study_hours = rng.uniform(0, 8, size=50)                         # 50 students
marks = 35 + study_hours * 7 + rng.normal(0, 6, size=50)         # more hours -> more marks

plt.figure(figsize=(6, 4))
plt.scatter(study_hours, marks, color="purple", alpha=0.7)       # alpha = transparency
plt.title("Study Hours vs Marks")
plt.xlabel("Study hours per day")
plt.ylabel("Marks")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scatter_plot.png")

# The correlation number tells us how strong the straight-line relationship is
correlation = np.corrcoef(study_hours, marks)[0, 1]
print("Saved scatter_plot.png | correlation =", round(correlation, 2))

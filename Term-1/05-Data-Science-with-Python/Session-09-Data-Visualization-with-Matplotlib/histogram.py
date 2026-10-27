# histogram.py
# Histogram = how values are spread out (the distribution).

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=1)
marks = rng.normal(loc=65, scale=12, size=300)   # 300 marks around 65
marks = np.clip(marks, 0, 100)                    # keep them between 0 and 100

plt.figure(figsize=(7, 4))
plt.hist(marks, bins=15, color="skyblue", edgecolor="black")   # bins = number of bars
plt.axvline(marks.mean(), color="red", linestyle="--", label=f"Mean = {marks.mean():.1f}")
plt.title("Distribution of Final Marks (300 students)")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.legend()
plt.tight_layout()
plt.savefig("histogram.png")
print("Saved histogram.png")

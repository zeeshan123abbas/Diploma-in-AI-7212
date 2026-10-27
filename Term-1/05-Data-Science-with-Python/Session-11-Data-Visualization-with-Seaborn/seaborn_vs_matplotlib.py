# seaborn_vs_matplotlib.py
# The same question drawn with Matplotlib and with Seaborn.
# Question: average marks per section, split by gender.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("students_performance.csv")

# ---- Matplotlib: we must calculate and position everything ourselves ----
table = df.groupby(["section", "gender"])["marks"].mean().unstack()   # sections x genders
x = np.arange(len(table.index))       # bar positions 0, 1, 2
width = 0.35
plt.figure(figsize=(6, 4))
plt.bar(x - width / 2, table["Female"], width, label="Female")
plt.bar(x + width / 2, table["Male"], width, label="Male")
plt.xticks(x, table.index)
plt.title("Matplotlib: average marks")
plt.legend()
plt.tight_layout()
plt.savefig("compare_matplotlib.png")

# ---- Seaborn: one line, works directly on the DataFrame ----
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="section", y="marks", hue="gender")   # calculates the mean for us
plt.title("Seaborn: average marks (with error bars)")
plt.tight_layout()
plt.savefig("compare_seaborn.png")
print("Saved compare_matplotlib.png and compare_seaborn.png")

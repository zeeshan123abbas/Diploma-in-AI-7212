# seaborn_distributions.py
# Looking at the shape of a numeric column: histplot, kdeplot, boxplot, violinplot.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("students_performance.csv")
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(11, 8))

# 1) Histogram with a smooth density curve on top
sns.histplot(data=df, x="marks", bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Histogram + KDE of marks")

# 2) KDE (smooth curve) for each gender, to compare shapes
sns.kdeplot(data=df, x="marks", hue="gender", fill=True, ax=axes[0, 1])
axes[0, 1].set_title("Marks density by gender")

# 3) Box plot per section
sns.boxplot(data=df, x="section", y="marks", ax=axes[1, 0])
axes[1, 0].set_title("Box plot of marks by section")

# 4) Violin plot = box plot + density shape
sns.violinplot(data=df, x="internet", y="marks", ax=axes[1, 1])
axes[1, 1].set_title("Marks with / without internet")

fig.tight_layout()
fig.savefig("distributions.png")
print("Saved distributions.png")

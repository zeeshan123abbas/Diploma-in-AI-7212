# seaborn_relationships.py
# Relationships between variables: regplot, heatmap and pairplot.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("students_performance.csv")
sns.set_theme(style="whitegrid")

# 1) Scatter plot with a fitted trend line
plt.figure(figsize=(6, 4))
sns.regplot(data=df, x="attendance", y="marks", scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title("Attendance vs Marks with trend line")
plt.tight_layout()
plt.savefig("regplot.png")

# 2) Correlation heatmap of the numeric columns
numbers = df[["study_hours", "attendance", "marks"]]
correlation = numbers.corr()                       # values from -1 to +1
plt.figure(figsize=(5, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")

# 3) Pair plot: every numeric column against every other, coloured by result
grid = sns.pairplot(df, vars=["study_hours", "attendance", "marks"], hue="result", height=2.5)
grid.savefig("pairplot.png")

# 4) Count plot: how many students in each category
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="section", hue="result")
plt.title("Pass / Fail count per section")
plt.tight_layout()
plt.savefig("countplot.png")
print("Saved regplot.png, heatmap.png, pairplot.png, countplot.png")

# plot_formatting.py
# Formatting features of 2-D plots: themes, palettes, titles, labels, limits, annotations.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("students_performance.csv")

# 1) Theme and context control the overall look
sns.set_theme(style="whitegrid", context="talk")   # styles: white, dark, whitegrid, darkgrid, ticks

plt.figure(figsize=(9, 6))
ax = sns.scatterplot(
    data=df, x="study_hours", y="marks",
    hue="result",                                  # colour by Pass/Fail
    palette={"Pass": "seagreen", "Fail": "crimson"},
    s=60, alpha=0.8,                               # dot size and transparency
)

# 2) Titles, labels and axis limits
ax.set_title("Study Hours vs Marks", fontsize=18, fontweight="bold")
ax.set_xlabel("Study hours per day")
ax.set_ylabel("Final marks")
ax.set_ylim(0, 105)

# 3) A reference line and an annotation (arrow + text)
ax.axhline(50, color="gray", linestyle="--", linewidth=1)
ax.annotate("Pass mark = 50", xy=(6, 50), xytext=(4.5, 20),
            arrowprops={"arrowstyle": "->", "color": "black"}, fontsize=12)

# 4) Move the legend and remove the top/right borders
ax.legend(title="Result", loc="lower right")
sns.despine()

plt.tight_layout()
plt.savefig("formatted_scatter.png", dpi=100)
print("Saved formatted_scatter.png")

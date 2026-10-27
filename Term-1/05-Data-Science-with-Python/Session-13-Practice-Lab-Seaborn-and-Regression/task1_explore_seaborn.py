# task1_explore_seaborn.py  (Practice for Session 11)
# Task: explore house_prices.csv with four Seaborn charts in one figure.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("house_prices.csv")
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Step 1: distribution of price
sns.histplot(data=df, x="price_lakh", kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Price distribution (lakh Rs)")

# Step 2: price by area
sns.boxplot(data=df, x="area", y="price_lakh", ax=axes[0, 1])
axes[0, 1].set_title("Price by area")

# Step 3: size vs price coloured by area -> does it curve?
sns.scatterplot(data=df, x="size_sqft", y="price_lakh", hue="area", ax=axes[1, 0])
axes[1, 0].set_title("Size vs price")

# Step 4: correlation heatmap
sns.heatmap(df[["size_sqft", "age_years", "price_lakh"]].corr(), annot=True, cmap="coolwarm", ax=axes[1, 1])
axes[1, 1].set_title("Correlation")

fig.tight_layout()
fig.savefig("house_explore.png")
print("Saved house_explore.png")
print("Average price per area:\n", df.groupby("area")["price_lakh"].mean().round(1).sort_values())

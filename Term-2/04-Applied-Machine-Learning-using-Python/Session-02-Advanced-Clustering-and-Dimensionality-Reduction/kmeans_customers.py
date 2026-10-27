# kmeans_customers.py
# Group shoppers into segments with K-Means and save a chart.

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")                 # save charts to files (no window needed)
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1) A tiny customer table: yearly income (thousand Rs) and spending score (1-100)
data = pd.DataFrame({
    "income":   [150, 160, 170, 180, 600, 620, 650, 700, 1200, 1250, 1300, 1350],
    "spending": [80, 85, 75, 90, 50, 45, 55, 52, 20, 15, 85, 90],
})

# 2) Put both columns on the same scale (income numbers are much bigger)
scaled = StandardScaler().fit_transform(data)

# 3) Ask K-Means for 4 groups
kmeans = KMeans(n_clusters=4, n_init=10, random_state=0)
data["segment"] = kmeans.fit_predict(scaled)
print(data)

# 4) Average values per segment help us name each group
print("\nAverage per segment:")
print(data.groupby("segment").mean().round(1))

# 5) Plot and save
plt.scatter(data["income"], data["spending"], c=data["segment"], cmap="viridis", s=80)
plt.xlabel("Income (thousand Rs)")
plt.ylabel("Spending score")
plt.title("Customer segments (K-Means)")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kmeans_segments.png")
plt.savefig(out)
print("Chart saved to", out)

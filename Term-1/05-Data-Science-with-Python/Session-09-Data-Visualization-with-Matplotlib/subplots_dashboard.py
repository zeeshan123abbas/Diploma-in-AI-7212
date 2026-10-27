# subplots_dashboard.py
# Several charts in ONE image = a small dashboard. Answers a problem statement:
# "The manager wants to understand last year's sales at a glance."

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "revenue": [210, 190, 240, 260, 300, 280, 250, 270, 310, 330, 400, 420],
    "orders": [70, 65, 80, 85, 95, 90, 82, 88, 99, 105, 130, 140],
})
category = pd.Series({"Electronics": 45, "Clothing": 30, "Grocery": 25})

# 2 rows x 2 columns of charts
fig, axes = plt.subplots(2, 2, figsize=(11, 7))

axes[0, 0].plot(sales["month"], sales["revenue"], marker="o")       # trend
axes[0, 0].set_title("Revenue trend (thousand Rs)")

axes[0, 1].bar(category.index, category.values, color="orange")     # comparison
axes[0, 1].set_title("Revenue share by category (%)")

axes[1, 0].scatter(sales["orders"], sales["revenue"], color="green") # relationship
axes[1, 0].set_title("Orders vs revenue")
axes[1, 0].set_xlabel("Orders")

axes[1, 1].hist(sales["revenue"], bins=5, color="gray", edgecolor="black")  # distribution
axes[1, 1].set_title("How monthly revenue is spread")

fig.suptitle("Sales Dashboard 2025", fontsize=16)
fig.tight_layout()
fig.savefig("dashboard.png")

# Insights we can read from the charts
best = sales.loc[sales["revenue"].idxmax(), "month"]
print("Saved dashboard.png")
print("Insight 1: best month is", best)
print("Insight 2: revenue grows strongly in the last quarter")
print("Insight 3: more orders -> more revenue (points rise left to right)")

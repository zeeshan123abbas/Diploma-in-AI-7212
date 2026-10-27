# task3_charts.py  (Practice for Session 09)
# Task: answer 3 questions with charts. Run task2_clean_orders.py first.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

orders = pd.read_csv("orders_clean.csv", parse_dates=["order_date"])

# Q1: Which city spends the most? -> bar chart
city_total = orders.groupby("city")["total"].sum().sort_values(ascending=False)

# Q2: How do sales change by month? -> line chart
orders["month"] = orders["order_date"].dt.strftime("%Y-%m")
monthly = orders.groupby("month")["total"].sum()

# Q3: Which products sell the most units? -> horizontal bar chart
units = orders.groupby("product")["qty"].sum().sort_values()

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].bar(city_total.index, city_total.values, color="steelblue")
axes[0].set_title("Q1: Revenue by city (Rs)")
axes[1].plot(monthly.index, monthly.values, marker="o", color="green")
axes[1].set_title("Q2: Revenue by month (Rs)")
axes[2].barh(units.index, units.values, color="orange")
axes[2].set_title("Q3: Units sold by product")
fig.tight_layout()
fig.savefig("orders_dashboard.png")

print("Saved orders_dashboard.png")
print("Top city:", city_total.index[0])
print("Best month:", monthly.idxmax())
print("Most units:", units.idxmax())

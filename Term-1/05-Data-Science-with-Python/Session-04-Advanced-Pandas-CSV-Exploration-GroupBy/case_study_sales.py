# case_study_sales.py
# Mini case study: a manager asks 4 questions about the shop's sales.

import pandas as pd

sales = pd.read_csv("sales.csv", parse_dates=["date"])
sales["total"] = sales["quantity"] * sales["unit_price"]

# Q1: Which city brings the most money?
city_totals = sales.groupby("city")["total"].sum().sort_values(ascending=False)
print("Q1 Best city:", city_totals.index[0], "-> Rs", city_totals.iloc[0])

# Q2: Which category sells the most items?
items = sales.groupby("category")["quantity"].sum()
print("Q2 Most items sold in:", items.idxmax(), "->", items.max(), "items")

# Q3: How did sales change month by month?
sales["month"] = sales["date"].dt.month_name()      # e.g. "January"
monthly = sales.groupby("month", sort=False)["total"].sum()
print("\nQ3 Monthly sales:\n", monthly)

# Q4: What are the 5 biggest orders?
print("\nQ4 Top 5 orders:\n", sales.nlargest(5, "total")[["order_id", "city", "category", "total"]])

# Save the city report for the manager
city_totals.to_csv("city_report.csv", header=["total_sales"])
print("\nSaved city_report.csv")

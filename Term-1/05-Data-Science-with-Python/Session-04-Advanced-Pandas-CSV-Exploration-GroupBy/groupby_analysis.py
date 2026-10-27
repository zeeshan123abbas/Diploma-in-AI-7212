# groupby_analysis.py
# groupby = split the rows into groups, calculate something, combine the answers.

import pandas as pd

sales = pd.read_csv("sales.csv")
sales["total"] = sales["quantity"] * sales["unit_price"]

# 1) Total sales per city
print("Total sales per city:\n", sales.groupby("city")["total"].sum(), "\n")

# 2) Average quantity per category
print("Average quantity per category:\n",
      sales.groupby("category")["quantity"].mean().round(2), "\n")

# 3) Several calculations at once with agg()
summary = sales.groupby("city")["total"].agg(["count", "sum", "mean", "max"])
print("City summary:\n", summary.round(0), "\n")

# 4) Group by two columns
city_cat = sales.groupby(["city", "category"])["total"].sum()
print("City + category:\n", city_cat, "\n")

# 5) Same result as a neat table (cities as rows, categories as columns)
table = sales.pivot_table(values="total", index="city", columns="category", aggfunc="sum")
print("Pivot table:\n", table)

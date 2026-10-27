# explore_data.py
# The first commands to run on ANY new dataset.

import pandas as pd

sales = pd.read_csv("sales.csv")

print("1) First rows:\n", sales.head(), "\n")
print("2) Last rows:\n", sales.tail(3), "\n")
print("3) Shape:", sales.shape, "\n")

print("4) Info (columns, types, non-null counts):")
sales.info()

print("\n5) Statistics of number columns:\n", sales.describe().round(1), "\n")
print("6) Missing values per column:\n", sales.isnull().sum(), "\n")
print("7) Unique cities:", sales["city"].unique())
print("8) How many orders per city:\n", sales["city"].value_counts(), "\n")
print("9) Largest 3 quantities:\n", sales.nlargest(3, "quantity"))

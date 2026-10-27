# read_write_csv.py
# Reading a CSV file into a DataFrame and writing results back to CSV.

import pandas as pd

# 1) Read the CSV file (it must be in the same folder)
sales = pd.read_csv("sales.csv")
print("Loaded", len(sales), "rows")
print(sales.head())          # first 5 rows

# 2) Read only some columns
small = pd.read_csv("sales.csv", usecols=["city", "quantity"])
print("\nOnly two columns:\n", small.head(3))

# 3) Tell pandas which column holds dates
sales = pd.read_csv("sales.csv", parse_dates=["date"])
print("\nDate column type:", sales["date"].dtype)

# 4) Add a column and save a new CSV
sales["total"] = sales["quantity"] * sales["unit_price"]
karachi = sales[sales["city"] == "Karachi"]
karachi.to_csv("karachi_sales.csv", index=False)
print("\nSaved karachi_sales.csv with", len(karachi), "rows")

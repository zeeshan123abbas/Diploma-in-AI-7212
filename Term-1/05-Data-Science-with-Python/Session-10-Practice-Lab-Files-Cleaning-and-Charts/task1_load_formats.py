# task1_load_formats.py  (Practice for Session 07)
# Task: read the raw JSON file, then save the same data as CSV, Excel and pickle.

import json
import pandas as pd

# Step 1: read JSON with the json module and look at the first record
with open("orders_raw.json", "r", encoding="utf-8") as file:
    records = json.load(file)
print("Number of records:", len(records))
print("First record:", records[0])

# Step 2: turn the list of dictionaries into a DataFrame
orders = pd.DataFrame(records)
print("\n", orders.head())

# Step 3: save in three other formats
orders.to_csv("orders_raw.csv", index=False)
orders.to_excel("orders_raw.xlsx", index=False)      # needs openpyxl
orders.to_pickle("orders_raw.pkl")
print("\nSaved CSV, Excel and pickle copies")

# Step 4: prove all copies hold the same number of rows
print("CSV rows:", len(pd.read_csv("orders_raw.csv")))
print("Excel rows:", len(pd.read_excel("orders_raw.xlsx")))
print("Pickle rows:", len(pd.read_pickle("orders_raw.pkl")))

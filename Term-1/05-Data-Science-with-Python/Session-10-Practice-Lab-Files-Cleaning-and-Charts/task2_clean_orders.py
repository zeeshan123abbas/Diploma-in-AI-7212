# task2_clean_orders.py  (Practice for Session 08)
# Task: clean the raw orders and save orders_clean.csv

import numpy as np
import pandas as pd

orders = pd.read_json("orders_raw.json")
print("Before cleaning:", orders.shape)
print(orders.isnull().sum(), "\n")

# Step 1: remove the duplicate order
orders = orders.drop_duplicates()

# Step 2: tidy text columns
orders["customer"] = orders["customer"].str.strip().str.title()
orders["city"] = orders["city"].str.strip().str.title()

# Step 3: impossible quantity (negative) -> missing
orders.loc[orders["qty"] < 0, "qty"] = np.nan

# Step 4: fill missing values
orders["qty"] = orders["qty"].fillna(1)                             # assume 1 item
orders["city"] = orders["city"].fillna(orders["city"].mode()[0])    # most common city
# missing price -> median price of the SAME product
orders["price"] = orders["price"].fillna(orders.groupby("product")["price"].transform("median"))
# if a product had no other price, fall back to the overall median
orders["price"] = orders["price"].fillna(orders["price"].median())

# Step 5: correct types and a new column
orders["qty"] = orders["qty"].astype(int)
orders["order_date"] = pd.to_datetime(orders["order_date"], format="%Y-%m-%d")
orders["total"] = orders["price"] * orders["qty"]

print("After cleaning:", orders.shape, "| missing values:", orders.isnull().sum().sum())
print(orders[["customer", "city", "product", "price", "qty", "total"]])
orders.to_csv("orders_clean.csv", index=False)
print("\nSaved orders_clean.csv")

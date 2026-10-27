# text_processing.py
# Cleaning text columns with the .str accessor
import pandas as pd

sales = pd.read_csv("sales.csv")

# Step 1: messy names (extra spaces, mixed case)
print("Before:", sales["customer"].tolist())

# Step 2: strip spaces and use Title Case
sales["customer"] = sales["customer"].str.strip().str.title()
print("After :", sales["customer"].tolist())

# Step 3: split full name into first and last name
sales[["first_name", "last_name"]] = sales["customer"].str.split(" ", n=1, expand=True)
print(sales[["customer", "first_name", "last_name"]].head())

# Step 4: search text
print("\nProducts containing 'board':", sales[sales["product"].str.contains("board", case=False)]["product"].unique())

# Step 5: replace and length
sales["category_short"] = sales["category"].str.replace("Accessories", "Acc")
sales["name_length"] = sales["customer"].str.len()
print(sales[["category", "category_short", "name_length"]].head(3))

# Step 6: count repeat customers
print("\nOrders per customer:")
print(sales["customer"].value_counts().head(3))

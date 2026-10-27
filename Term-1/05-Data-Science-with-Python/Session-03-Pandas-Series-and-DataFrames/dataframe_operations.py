# dataframe_operations.py
# Common everyday operations on a DataFrame.

import pandas as pd

sales = pd.DataFrame({
    "product":  ["Tea", "Sugar", "Milk", "Rice", "Oil"],
    "price":    [450, 160, 220, 380, 600],
    "quantity": [30, 50, 80, 25, 15],
})

# 1) New column from two columns
sales["revenue"] = sales["price"] * sales["quantity"]
print(sales, "\n")

# 2) Column statistics
print("Total revenue:", sales["revenue"].sum())
print("Average price:", sales["price"].mean())

# 3) Rename a column
sales = sales.rename(columns={"quantity": "qty"})
print("\nRenamed columns:", list(sales.columns))

# 4) Drop (remove) a column
smaller = sales.drop(columns=["price"])
print("\nWithout price:\n", smaller)

# 5) Add a new row with pd.concat
new_row = pd.DataFrame({"product": ["Flour"], "price": [140], "qty": [60], "revenue": [8400]})
sales = pd.concat([sales, new_row], ignore_index=True)
print("\nAfter adding Flour:\n", sales)

# 6) Apply a simple function to each value of a column
def price_band(price):
    # returns a label depending on the price
    if price >= 400:
        return "High"
    return "Normal"

sales["band"] = sales["price"].apply(price_band)
print("\nWith price band:\n", sales)

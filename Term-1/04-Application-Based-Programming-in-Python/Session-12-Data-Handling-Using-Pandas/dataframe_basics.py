# dataframe_basics.py
# A DataFrame is a TABLE: rows and columns (many Series side by side)
import pandas as pd

# Step 1: create a DataFrame from a dictionary of lists
students = pd.DataFrame({
    "name": ["Ali", "Sara", "Bilal", "Hina"],
    "city": ["Karachi", "Lahore", "Karachi", "Multan"],
    "marks": [78, 91, 64, 85],
})
print(students)

# Step 2: read a CSV file into a DataFrame
sales = pd.read_csv("sales.csv")

# Step 3: explore the data
print("\nShape (rows, columns):", sales.shape)
print("\nFirst 3 rows:")
print(sales.head(3))
print("\nColumn types:")
print(sales.dtypes)
print("\nSummary of numbers:")
print(sales.describe())

# Step 4: select columns and rows
print("\nOne column:")
print(sales["product"].head(3))
print("\nTwo columns:")
print(sales[["city", "unit_price"]].head(3))
print("\nRow by position (iloc):")
print(sales.iloc[0])
print("\nRows by label + columns (loc):")
print(sales.loc[0:2, ["order_id", "product"]])

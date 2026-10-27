# data_manipulation.py
# Cleaning, filtering, new columns, sorting, grouping and merging
import pandas as pd

sales = pd.read_csv("sales.csv", parse_dates=["date"])

# 1) Missing values
print("Missing per column:")
print(sales.isna().sum())
sales["quantity"] = sales["quantity"].fillna(1)     # assume 1 if missing
sales["quantity"] = sales["quantity"].astype(int)

# 2) New calculated column
sales["total"] = sales["quantity"] * sales["unit_price"]

# 3) Filtering rows
karachi = sales[sales["city"] == "Karachi"]
print("\nKarachi orders:", len(karachi))
big = sales[(sales["category"] == "Electronics") & (sales["total"] > 100000)]
print("Big electronics orders:")
print(big[["order_id", "product", "total"]])

# 4) Sorting
print("\nTop 3 orders by total:")
print(sales.sort_values("total", ascending=False).head(3)[["order_id", "city", "total"]])

# 5) Grouping and aggregation
print("\nRevenue by city:")
print(sales.groupby("city")["total"].sum().sort_values(ascending=False))
print("\nOrders and revenue by category:")
print(sales.groupby("category").agg(orders=("order_id", "count"), revenue=("total", "sum")))

# 6) Merging with another table (like a SQL JOIN)
regions = pd.DataFrame({"city": ["Karachi", "Lahore", "Islamabad", "Multan"],
                        "province": ["Sindh", "Punjab", "ICT", "Punjab"]})
merged = sales.merge(regions, on="city", how="left")
print("\nRevenue by province:")
print(merged.groupby("province")["total"].sum())

# 7) Drop a column and save the clean data
clean = merged.drop(columns=["customer"])
clean.to_csv("sales_clean.csv", index=False)
print("\nSaved sales_clean.csv with", clean.shape[0], "rows")

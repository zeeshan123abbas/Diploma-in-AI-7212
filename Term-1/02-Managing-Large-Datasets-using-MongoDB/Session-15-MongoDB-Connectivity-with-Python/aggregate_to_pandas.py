# Session 15 - aggregate_to_pandas.py
# Run: python aggregate_to_pandas.py
# Uses MONGODB_URI if set (e.g. your Atlas string), otherwise the local server.

# Needs shopdb (Session 02) and pandas (pip install -r requirements.txt).
import os
import pandas as pd
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))
db = client["shopdb"]

# Step 1: let MongoDB do the heavy work (same pipeline as Session 05)
pipeline = [
    {"$match": {"status": {"$ne": "cancelled"}}},
    {"$group": {"_id": "$city", "revenue": {"$sum": "$total"}, "orders": {"$sum": 1}}},
    {"$sort": {"revenue": -1}},
]
rows = list(db.orders.aggregate(pipeline))     # a small list of dictionaries

# Step 2: build a DataFrame and tidy the column names
df = pd.DataFrame(rows).rename(columns={"_id": "city"})
df["avg_order"] = (df["revenue"] / df["orders"]).round(0)

# Step 3: show and save
print(df)
df.to_csv("revenue_by_city.csv", index=False)
print("saved revenue_by_city.csv")

client.close()

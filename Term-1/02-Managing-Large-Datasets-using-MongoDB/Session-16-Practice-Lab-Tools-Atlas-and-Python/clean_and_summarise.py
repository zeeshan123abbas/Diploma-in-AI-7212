# Session 16 - clean_and_summarise.py  (TRANSFORM + LOAD steps)
# Run load-branch-sales.bat first, then: python clean_and_summarise.py
# Uses MONGODB_URI if set (Atlas), otherwise the local server.
import os
import pandas as pd
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))
db = client["salesdb"]
raw = db["raw_sales"]

# Rule 1: one standard spelling for each city
CITY_FIX = {
    "karachi": "Karachi", "khi": "Karachi",
    "lahore": "Lahore", "lhr": "Lahore",
    "islamabad": "Islamabad", "isb": "Islamabad",
    "quetta": "Quetta",
}

clean_rows = []
seen_receipts = set()
skipped = 0

# Step 1: read every raw document and clean it
for row in raw.find():
    receipt = row.get("receiptNo")
    amount = row.get("amount")

    # Rule 2: skip duplicates
    if receipt in seen_receipts:
        skipped += 1
        continue
    seen_receipts.add(receipt)

    # Rule 3: skip rows without a numeric amount (empty or text like "six thousand")
    if not isinstance(amount, (int, float)):
        skipped += 1
        continue

    city_key = str(row.get("city", "")).strip().lower()
    clean_rows.append({
        "date": row["date"],
        "city": CITY_FIX.get(city_key, "Unknown"),
        "amount": amount,
    })

print("raw rows    :", raw.count_documents({}))
print("clean rows  :", len(clean_rows))
print("skipped rows:", skipped)

# Step 2: summarise with pandas (revenue and receipts per date and city)
df = pd.DataFrame(clean_rows)
summary = (df.groupby(["date", "city"], as_index=False)
             .agg(revenue=("amount", "sum"), receipts=("amount", "count")))
print(summary)

# Step 3: LOAD - replace the summary collection so re-runs do not duplicate
db.daily_summary.delete_many({})
# PyMongo cannot store numpy numbers, so convert each value to plain Python types
records = [
    {"date": r.date, "city": r.city, "revenue": float(r.revenue), "receipts": int(r.receipts)}
    for r in summary.itertuples()
]
db.daily_summary.insert_many(records)
print("daily_summary documents:", db.daily_summary.count_documents({}))

# Step 4: hand-off file for Excel
summary.to_csv("summary.csv", index=False)
print("saved summary.csv")
client.close()

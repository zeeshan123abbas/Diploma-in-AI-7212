# Session 15 - query_documents.py
# Run: python query_documents.py
# Uses MONGODB_URI if set (e.g. your Atlas string), otherwise the local server.

# Needs shopdb (run shopdb-setup.js from Session 02 first).
import os
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))
db = client["shopdb"]

# 1. find_one: a single document (or None)
product = db.products.find_one({"_id": "P004"})
print("1)", product["name"], product["price"])

# 2. find with a filter, projection, sort and limit
print("2) products under 3000, most expensive first:")
cursor = db.products.find(
    {"price": {"$lt": 3000}},                 # filter: $lt must be in quotes
    {"_id": 0, "name": 1, "price": 1}         # projection
).sort("price", -1).limit(5)
for p in cursor:                              # a cursor is read with a for loop
    print("   ", p["name"], "-", p["price"])

# 3. logical operator: customers from Karachi OR premium customers
print("3) Karachi or premium customers:")
for c in db.customers.find({"$or": [{"city": "Karachi"}, {"isPremium": True}]}):
    print("   ", c["name"], c["city"], c["isPremium"])

# 4. count and distinct
print("4) pending orders:", db.orders.count_documents({"status": "pending"}))
print("   categories:", db.products.distinct("category"))

client.close()

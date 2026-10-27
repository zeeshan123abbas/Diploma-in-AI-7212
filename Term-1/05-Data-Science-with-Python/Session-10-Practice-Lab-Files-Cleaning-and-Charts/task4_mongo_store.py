# task4_mongo_store.py  (Practice for Session 06)
# Task: store the clean orders in MongoDB and query them back.
# Needs a running MongoDB on localhost:27017 and orders_clean.csv from task 2.

import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

orders = pd.read_csv("orders_clean.csv")

client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=3000)
try:
    client.admin.command("ping")
    collection = client["aptech_ds"]["orders"]
    collection.delete_many({})                                 # fresh start

    # Step 1: DataFrame -> list of dictionaries -> MongoDB
    collection.insert_many(orders.to_dict(orient="records"))
    print("Inserted:", collection.count_documents({}))

    # Step 2: query - Karachi orders above Rs 10,000
    query = {"city": "Karachi", "total": {"$gt": 10000}}
    for doc in collection.find(query, {"_id": 0, "customer": 1, "product": 1, "total": 1}):
        print("  ", doc)

    # Step 3: back to pandas
    back = pd.DataFrame(list(collection.find({}, {"_id": 0})))
    print("Rows read back into pandas:", len(back))
except ServerSelectionTimeoutError:
    print("MongoDB is not running - start it and try again.")
finally:
    client.close()

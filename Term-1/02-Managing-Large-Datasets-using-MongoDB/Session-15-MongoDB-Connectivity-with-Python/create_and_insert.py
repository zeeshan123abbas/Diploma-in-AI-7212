# Session 15 - create_and_insert.py
# Run: python create_and_insert.py
# Uses MONGODB_URI if set (e.g. your Atlas string), otherwise the local server.

import os
from datetime import datetime
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))

# Step 1: choose a database and a collection (created on first insert)
db = client["schooldb"]
students = db["students"]

# Step 2: insert ONE document (a Python dictionary)
result = students.insert_one({
    "name": "Ayesha",
    "age": 21,
    "city": "Karachi",
    "skills": ["python", "sql"],          # a list becomes an array
    "joined": datetime(2026, 1, 10),      # datetime becomes a BSON date
    "isActive": True                      # Python True -> true
})
print("inserted one, _id =", result.inserted_id)

# Step 3: insert MANY documents at once
result = students.insert_many([
    {"name": "Bilal", "age": 23, "city": "Lahore",    "skills": ["excel"]},
    {"name": "Sara",  "age": 19, "city": "Karachi",   "skills": ["python"]},
    {"name": "Usman", "age": 25, "city": "Islamabad", "skills": ["sql", "powerbi"]},
])
print("inserted many, count =", len(result.inserted_ids))

# Step 4: confirm
print("total students:", students.count_documents({}))
client.close()

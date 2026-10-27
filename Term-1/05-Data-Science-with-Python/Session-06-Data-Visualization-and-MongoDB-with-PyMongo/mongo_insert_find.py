# mongo_insert_find.py
# Insert documents and read them back with filters.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=3000)

db = client["aptech_ds"]          # database (created automatically on first insert)
students = db["students"]          # collection (like a table)

students.delete_many({})           # start fresh every time we run the demo

# 1) Insert one document (a Python dictionary)
students.insert_one({"name": "Ayesha", "city": "Karachi", "marks": 88})

# 2) Insert many documents at once
students.insert_many([
    {"name": "Bilal", "city": "Lahore",    "marks": 72},
    {"name": "Sana",  "city": "Karachi",   "marks": 95},
    {"name": "Umar",  "city": "Islamabad", "marks": 64},
    {"name": "Hira",  "city": "Lahore",    "marks": 81},
])
print("Documents in collection:", students.count_documents({}))

# 3) Find all students from Karachi
print("\nKarachi students:")
for doc in students.find({"city": "Karachi"}):
    print("  ", doc["name"], doc["marks"])

# 4) Find students with marks greater than 80, show only name and marks, sorted
print("\nMarks above 80 (highest first):")
query = {"marks": {"$gt": 80}}            # $gt = greater than
fields = {"_id": 0, "name": 1, "marks": 1}  # 1 = show, 0 = hide
for doc in students.find(query, fields).sort("marks", -1):
    print("  ", doc)

# 5) Update and delete
students.update_one({"name": "Umar"}, {"$set": {"marks": 70}})
students.delete_one({"name": "Bilal"})
print("\nAfter update/delete:", list(students.find({}, {"_id": 0, "name": 1, "marks": 1})))

client.close()

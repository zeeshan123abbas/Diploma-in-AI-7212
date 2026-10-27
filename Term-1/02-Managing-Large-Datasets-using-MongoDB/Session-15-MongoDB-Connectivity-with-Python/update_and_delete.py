# Session 15 - update_and_delete.py
# Run: python update_and_delete.py
# Uses MONGODB_URI if set (e.g. your Atlas string), otherwise the local server.

# Needs shopdb (Session 02) and schooldb (create_and_insert.py).
import os
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))
shop = client["shopdb"]
school = client["schooldb"]

# 1. update_one: change one field
result = shop.products.update_one({"_id": "P009"}, {"$set": {"stock": 75}})
print("update_one -> matched:", result.matched_count, "modified:", result.modified_count)

# 2. update_many: raise all Book prices by 5%
result = shop.products.update_many({"category": "Books"}, {"$mul": {"price": 1.05}})
print("update_many -> modified:", result.modified_count)

# 3. push a value into an array
school.students.update_one({"name": "Bilal"}, {"$push": {"skills": "python"}})

# 4. delete_many: remove students younger than 20
result = school.students.delete_many({"age": {"$lt": 20}})
print("delete_many -> deleted:", result.deleted_count)

client.close()

# Session 15 - connect.py
# Run: python connect.py
# Uses MONGODB_URI if set (e.g. your Atlas string), otherwise the local server.

import os
from pymongo import MongoClient

# Step 1: read the connection string (Atlas) or use the local default
uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")

# Step 2: create ONE client for the whole program (wait max 5 seconds for a server)
client = MongoClient(uri, serverSelectionTimeoutMS=5000)

# Step 3: test the connection
try:
    client.admin.command("ping")
    print("Connected to MongoDB!")
    print("Databases:", client.list_database_names())
except Exception as error:
    print("Could not connect:", error)
finally:
    client.close()   # close when the program ends

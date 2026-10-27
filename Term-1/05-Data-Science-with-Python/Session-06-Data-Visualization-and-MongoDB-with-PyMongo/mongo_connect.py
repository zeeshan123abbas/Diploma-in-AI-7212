# mongo_connect.py
# Connect Python to a local MongoDB server using the PyMongo driver.
# Install first:  pip install pymongo   (and start MongoDB on your PC)

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# 1) The connection string: where is the server?
#    Local default: mongodb://localhost:27017
#    For MongoDB Atlas, paste the string from the Atlas "Connect" button instead.
connection_string = "mongodb://localhost:27017"

# 2) Create the client (wait max 3 seconds for the server)
client = MongoClient(connection_string, serverSelectionTimeoutMS=3000)

try:
    # 3) "ping" checks that the server really answers
    client.admin.command("ping")
    print("Connected to MongoDB!")

    # 4) List the databases on the server
    print("Databases:", client.list_database_names())
except ServerSelectionTimeoutError:
    print("Could not reach MongoDB. Is the server running on localhost:27017?")
finally:
    client.close()   # always close the connection when done

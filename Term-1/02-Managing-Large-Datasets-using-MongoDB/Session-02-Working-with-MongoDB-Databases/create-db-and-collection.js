// create-db-and-collection.js
// Run: mongosh --file create-db-and-collection.js
// Purpose: create a collection in two ways - automatically and explicitly.

// Step 1: switch to a new database "schooldb"
db = db.getSiblingDB("schooldb");

// Step 2: remove old copies so the file can be run many times
db.students.drop();
db.activityLog.drop();

// Step 3 (implicit): inserting a document creates the collection "students"
db.students.insertOne({ name: "Sara Ali", term: 1 });

// Step 4 (explicit): create a capped collection for logs
//   capped: true -> fixed size; oldest documents are removed when full
//   size        -> maximum size in bytes, max -> maximum number of documents
db.createCollection("activityLog", { capped: true, size: 100000, max: 100 });

// Step 5: list the collections in this database
print("Collections in schooldb: " + db.getCollectionNames().join(", "));

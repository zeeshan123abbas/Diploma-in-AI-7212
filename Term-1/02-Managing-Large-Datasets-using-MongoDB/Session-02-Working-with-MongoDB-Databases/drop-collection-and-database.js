// drop-collection-and-database.js
// Run: mongosh --file drop-collection-and-database.js
// Purpose: remove a whole collection and a whole database.
// WARNING: dropping cannot be undone. We only drop demo data here, never shopdb itself.

// Step 1: drop the demo collection "typesDemo" from shopdb
db = db.getSiblingDB("shopdb");
const dropped = db.typesDemo.drop();          // true if it existed, false if not
print("typesDemo dropped: " + dropped);

// Step 2: drop the whole "hello" database created in Session 01
db = db.getSiblingDB("hello");
printjson(db.dropDatabase());                 // { ok: 1, dropped: 'hello' }

// Step 3: confirm - "hello" should no longer be listed
print("Databases now: " + db.getMongo().getDBNames().join(", "));

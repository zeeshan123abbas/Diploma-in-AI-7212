// diagnostic-commands.js
// Run: mongosh --file diagnostic-commands.js
// Purpose: check the server and database with diagnostic commands.

db = db.getSiblingDB("shopdb");

// 1. Is the server alive?
print("--- ping ---");
printjson(db.adminCommand({ ping: 1 }));

// 2. Which version am I running?
print("--- buildInfo ---");
print("version: " + db.adminCommand({ buildInfo: 1 }).version);

// 3. Is this server a primary? (hello replaced the old isMaster command)
print("--- hello ---");
printjson(db.adminCommand({ hello: 1 }).isWritablePrimary);

// 4. Size of this database (scale 1024 = numbers in KB)
print("--- dbStats ---");
const stats = db.runCommand({ dbStats: 1, scale: 1024 });
print("collections: " + stats.collections + ", objects: " + stats.objects + ", dataSize KB: " + stats.dataSize);

// 5. Names of the collections
print("--- listCollections ---");
const list = db.runCommand({ listCollections: 1, nameOnly: true });
list.cursor.firstBatch.forEach(c => print(" - " + c.name));

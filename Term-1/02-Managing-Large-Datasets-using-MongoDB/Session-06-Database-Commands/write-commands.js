// write-commands.js
// Run shopdb-setup.js first, then: mongosh --file write-commands.js
// Purpose: insert, update, find and delete using commands instead of shell methods.

db = db.getSiblingDB("shopdb");

// 1. insert command
let reply = db.runCommand({
  insert: "products",
  documents: [{ _id: "P011", name: "Webcam HD", category: "Electronics", price: 5200 }]
});
print("inserted: " + reply.n);          // n = documents inserted

// 2. update command: q = filter, u = update
reply = db.runCommand({
  update: "products",
  updates: [{ q: { _id: "P011" }, u: { $set: { stock: 10 } } }]
});
print("matched: " + reply.n + ", modified: " + reply.nModified);

// 3. find command (results are inside cursor.firstBatch)
reply = db.runCommand({ find: "products", filter: { _id: "P011" } });
printjson(reply.cursor.firstBatch);

// 4. delete command: limit 1 = delete one match, 0 = all matches
reply = db.runCommand({
  delete: "products",
  deletes: [{ q: { _id: "P011" }, limit: 1 }]
});
print("deleted: " + reply.n);

// atlas-first-steps.js
// Connect to Atlas first, then inside mongosh:  load("atlas-first-steps.js")
// Or: mongosh "<your Atlas URI>" --file atlas-first-steps.js
// Purpose: prove that normal commands work in the cloud.

db = db.getSiblingDB("shopdb");

// 1. Insert and read back a document
db.products.insertOne({ _id: "A001", name: "Cloud Notebook", category: "Books", price: 999, stock: 10 });
printjson(db.products.findOne({ _id: "A001" }));

// 2. Atlas runs a replica set: see the members
const info = db.hello();
print("set name : " + info.setName);
print("primary  : " + info.primary);
print("members  : " + info.hosts.join(", "));

// 3. List databases you can see with this user
db.adminCommand({ listDatabases: 1, nameOnly: true }).databases.forEach(d => print(" - " + d.name));

// 4. Clean up the test document
db.products.deleteOne({ _id: "A001" });

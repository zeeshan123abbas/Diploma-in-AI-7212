// part-b-commands-and-methods-solutions.js  (tasks 6-10)
// Run shopdb-setup.js first, then: mongosh --file part-b-commands-and-methods-solutions.js

db = db.getSiblingDB("shopdb");

// Task 6: dbStats command
const s = db.runCommand({ dbStats: 1 });
print("collections: " + s.collections + ", objects: " + s.objects);

// Task 7: distinct command
print("payment methods: " + db.runCommand({ distinct: "orders", key: "payment" }).values.join(", "));

// Task 8: update and return the new document
printjson(db.orders.findOneAndUpdate(
  { _id: "O010" },
  { $set: { status: "shipped" } },
  { returnDocument: "after" }
));

// Task 9: two stock changes in one bulkWrite
const r = db.products.bulkWrite([
  { updateOne: { filter: { _id: "P003" }, update: { $inc: { stock: 20 } } } },
  { updateOne: { filter: { _id: "P006" }, update: { $inc: { stock: -5 } } } }
]);
print("modified: " + r.modifiedCount);

// Task 10: create, show and drop a read-only user
db.createUser({ user: "manager", pwd: "Manager#2026", roles: [{ role: "read", db: "shopdb" }] });
printjson(db.getUsers());
db.dropUser("manager");

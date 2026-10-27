// other-index-types.js
// Run shopdb-setup.js and make-big-collection.js first.
// Purpose: compound, multikey, unique and hashed indexes.

db = db.getSiblingDB("shopdb");

// 1. Compound index (ESR: equality on city, then range on total)
db.bigorders.createIndex({ city: 1, total: 1 });
const plan = db.bigorders.find({ city: "Quetta", total: { $gt: 15000 } }).explain("executionStats");
print("compound -> examined: " + plan.executionStats.totalDocsExamined + ", returned: " + plan.executionStats.nReturned);

// 2. Multikey index: tags is an array, MongoDB indexes every element
db.products.createIndex({ tags: 1 });
printjson(db.products.find({ tags: "python" }, { name: 1 }).toArray());

// 3. Unique index: no two customers with the same email
db.customers.createIndex({ email: 1 }, { unique: true });
try {
  db.customers.insertOne({ _id: "C099", name: "Copy", email: "ayesha@example.com" });
} catch (err) {
  print("duplicate blocked: " + err.code);              // 11000 = duplicate key
}

// 4. Hashed index (used mainly as a shard key, Session 10)
db.bigorders.createIndex({ orderNo: "hashed" });
print("indexes on bigorders: " + db.bigorders.getIndexes().map(i => i.name).join(", "));

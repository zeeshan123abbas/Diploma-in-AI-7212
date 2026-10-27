// aggregation-commands.js
// Run shopdb-setup.js first, then: mongosh --file aggregation-commands.js
// Purpose: count, distinct and aggregate as commands.

db = db.getSiblingDB("shopdb");

// 1. count: how many pending orders?
const c = db.runCommand({ count: "orders", query: { status: "pending" } });
print("pending orders: " + c.n);

// 2. distinct: list of different cities
const d = db.runCommand({ distinct: "customers", key: "city" });
print("cities: " + d.values.join(", "));

// 3. aggregate: orders per payment method (cursor: {} is required)
const a = db.runCommand({
  aggregate: "orders",
  pipeline: [ { $group: { _id: "$payment", orders: { $sum: 1 } } } ],
  cursor: {}
});
printjson(a.cursor.firstBatch);

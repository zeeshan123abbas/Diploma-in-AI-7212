// array-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file array-operators.js
// Purpose: query arrays with a plain value, $all, $size and $elemMatch.

db = db.getSiblingDB("shopdb");

// 1. Plain value: tags array CONTAINS "python"
print("--- tagged python ---");
printjson(db.products.find({ tags: "python" }, { name: 1, tags: 1 }).toArray());

// 2. $all: tags contain BOTH "python" AND "data"
print("--- tagged python AND data ---");
printjson(db.products.find({ tags: { $all: ["python", "data"] } }, { name: 1 }).toArray());

// 3. $size: products with no ratings yet (empty array)
print("--- no ratings yet ---");
printjson(db.products.find({ ratings: { $size: 0 } }, { name: 1 }).toArray());

// 4. $elemMatch: orders with ONE item that is P001 AND has qty of 2 or more
print("--- bought 2+ Wireless Mice in one line ---");
printjson(db.orders.find(
  { items: { $elemMatch: { productId: "P001", qty: { $gte: 2 } } } },
  { customerId: 1, items: 1 }
).toArray());

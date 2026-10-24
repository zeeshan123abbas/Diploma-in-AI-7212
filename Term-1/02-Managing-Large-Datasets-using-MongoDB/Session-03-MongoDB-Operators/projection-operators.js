// projection-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file projection-operators.js
// Purpose: control which part of an array is returned.

db = db.getSiblingDB("shopdb");

// 1. $slice: show only the FIRST rating of each product
print("--- first rating only ---");
printjson(db.products.find({}, { name: 1, ratings: { $slice: 1 } }).toArray());

// 2. $slice with a negative number: the LAST tag
print("--- last tag only ---");
printjson(db.products.find({}, { name: 1, tags: { $slice: -1 } }).toArray());

// 3. $elemMatch in a projection: show only the item for product P008
print("--- only the P008 line of each order ---");
printjson(db.orders.find(
  { "items.productId": "P008" },
  { items: { $elemMatch: { productId: "P008" } } }
).toArray());

// 4. Positional $: show the item that matched the filter
print("--- matched item for P001 ---");
printjson(db.orders.find({ "items.productId": "P001" }, { "items.$": 1 }).toArray());

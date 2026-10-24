// logical-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file logical-operators.js
// Purpose: combine conditions with $or, $and, $nor and $not.

db = db.getSiblingDB("shopdb");

// 1. $or: customers from Islamabad OR younger than 25
print("--- Islamabad OR age < 25 ---");
printjson(db.customers.find(
  { $or: [{ city: "Islamabad" }, { age: { $lt: 25 } }] },
  { name: 1, city: 1, age: 1 }
).toArray());

// 2. $and: Electronics that are in stock
//    (writing { category: "Electronics", stock: { $gt: 0 } } gives the same result)
print("--- Electronics AND stock > 0 ---");
printjson(db.products.find(
  { $and: [{ category: "Electronics" }, { stock: { $gt: 0 } }] },
  { name: 1, stock: 1 }
).toArray());

// 3. $nor: orders that are NEITHER delivered NOR cancelled
print("--- not delivered and not cancelled ---");
printjson(db.orders.find(
  { $nor: [{ status: "delivered" }, { status: "cancelled" }] },
  { status: 1 }
).toArray());

// 4. $not: products whose price is NOT greater than 3000
print("--- price NOT > 3000 ---");
printjson(db.products.find({ price: { $not: { $gt: 3000 } } }, { name: 1, price: 1 }).toArray());

// element-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file element-operators.js
// Purpose: check whether a field exists ($exists) and what type it is ($type).

db = db.getSiblingDB("shopdb");

// 1. Products that HAVE a specs field
print("--- products with specs ---");
printjson(db.products.find({ specs: { $exists: true } }, { name: 1 }).toArray());

// 2. Products that do NOT have a specs field (books, clothing, grocery)
print("--- products without specs ---");
printjson(db.products.find({ specs: { $exists: false } }, { name: 1 }).toArray());

// 3. Products that have a warranty value inside specs (dot notation)
print("--- products with a warranty ---");
printjson(db.products.find({ "specs.warrantyMonths": { $exists: true } }, { name: 1, specs: 1 }).toArray());

// 4. Customers whose "joined" field is stored as a real date
print("Customers with a date in 'joined': " +
  db.customers.countDocuments({ joined: { $type: "date" } }));

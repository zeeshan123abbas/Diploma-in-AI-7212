// misc-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file misc-operators.js
// Purpose: text patterns ($regex), field-to-field logic ($expr) and $mod.

db = db.getSiblingDB("shopdb");

// 1. $regex: product names starting with "b" (the "i" option ignores upper/lower case)
print("--- names starting with B ---");
printjson(db.products.find({ name: { $regex: "^b", $options: "i" } }, { name: 1 }).toArray());

// 2. $regex: emails ending with example.com
print("Customers with example.com email: " +
  db.customers.countDocuments({ email: { $regex: "example\\.com$" } }));

// 3. $expr: products where stock is lower than 10 (uses "$stock" = value of the stock field)
print("--- low stock ---");
printjson(db.products.find({ $expr: { $lt: ["$stock", 10] } }, { name: 1, stock: 1 }).toArray());

// 4. $expr comparing two numbers made from fields: price x stock > 200000 (stock value)
print("--- stock worth more than 200,000 PKR ---");
printjson(db.products.find(
  { $expr: { $gt: [{ $multiply: ["$price", "$stock"] }, 200000] } },
  { name: 1, price: 1, stock: 1 }
).toArray());

// 5. $mod: customers with an even age (age divided by 2 leaves 0)
print("--- even ages ---");
printjson(db.customers.find({ age: { $mod: [2, 0] } }, { name: 1, age: 1 }).toArray());

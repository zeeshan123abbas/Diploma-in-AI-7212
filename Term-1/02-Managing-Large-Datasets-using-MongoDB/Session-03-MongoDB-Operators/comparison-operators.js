// comparison-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file comparison-operators.js
// Purpose: filter with $gt, $gte, $lte, $in and $ne.

db = db.getSiblingDB("shopdb");

// 1. Products costing MORE than 3000 PKR
print("--- price > 3000 ---");
printjson(db.products.find({ price: { $gt: 3000 } }, { name: 1, price: 1 }).toArray());

// 2. Products in a price RANGE: 2000 to 4000 (both conditions on the same field)
print("--- 2000 <= price <= 4000 ---");
printjson(db.products.find({ price: { $gte: 2000, $lte: 4000 } }, { name: 1, price: 1 }).toArray());

// 3. Customers whose city is IN a list
print("--- customers from Karachi or Lahore ---");
printjson(db.customers.find({ city: { $in: ["Karachi", "Lahore"] } }, { name: 1, city: 1 }).toArray());

// 4. Orders whose status is NOT EQUAL to cancelled
print("--- orders that are not cancelled ---");
printjson(db.orders.find({ status: { $ne: "cancelled" } }, { status: 1, total: 1 }).toArray());

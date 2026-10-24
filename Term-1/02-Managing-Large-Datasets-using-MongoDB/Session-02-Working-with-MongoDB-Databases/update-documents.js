// update-documents.js
// Run shopdb-setup.js first, then: mongosh --file update-documents.js
// Purpose: change documents with updateOne(), updateMany() and replaceOne().

db = db.getSiblingDB("shopdb");

// Update 1: restock the earbuds (stock was 0)
const r1 = db.products.updateOne({ _id: "P003" }, { $set: { stock: 25 } });
print("updateOne matched " + r1.matchedCount + ", modified " + r1.modifiedCount);

// Update 2: increase the price of every Grocery product by 50 PKR
const r2 = db.products.updateMany({ category: "Grocery" }, { $inc: { price: 50 } });
print("updateMany modified " + r2.modifiedCount + " grocery products");

// Update 3: add a new field to all customers in Lahore
db.customers.updateMany({ city: "Lahore" }, { $set: { region: "Punjab" } });

// Update 4: replace a whole document (only _id stays the same)
db.customers.replaceOne(
  { _id: "C006" },
  { name: "Faraz Hussain", city: "Hyderabad", age: 36 }
);

// Step 5: check the results
printjson(db.products.find({ category: "Grocery" }, { name: 1, price: 1 }).toArray());
printjson(db.customers.findOne({ _id: "C006" }));   // email and isPremium are gone

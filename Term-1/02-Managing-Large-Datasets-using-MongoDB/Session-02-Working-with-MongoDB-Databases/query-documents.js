// query-documents.js
// Run shopdb-setup.js first, then: mongosh --file query-documents.js
// Purpose: read documents with find(), findOne(), projection, sort() and limit().

db = db.getSiblingDB("shopdb");

// Query 1: one document by its _id
print("--- Product P001 ---");
printjson(db.products.findOne({ _id: "P001" }));

// Query 2: all products in the Books category (filter)
print("--- Books ---");
printjson(db.products.find({ category: "Books" }).toArray());

// Query 3: only name and price of every product (projection: 1 = show, 0 = hide)
print("--- Name and price only ---");
printjson(db.products.find({}, { name: 1, price: 1, _id: 0 }).toArray());

// Query 4: a field inside an embedded document uses "dot notation" in quotes
print("--- Products made by Anker ---");
printjson(db.products.find({ "specs.brand": "Anker" }, { name: 1 }).toArray());

// Query 5: the 3 most expensive products (sort -1 = high to low)
print("--- Top 3 by price ---");
printjson(db.products.find({}, { name: 1, price: 1 }).sort({ price: -1 }).limit(3).toArray());

// Query 6: how many customers live in Karachi?
print("Customers in Karachi: " + db.customers.countDocuments({ city: "Karachi" }));

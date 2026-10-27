// collection-methods.js
// Run shopdb-setup.js first, then: mongosh --file collection-methods.js
// Purpose: useful collection methods beyond basic CRUD.

db = db.getSiblingDB("shopdb");

// 1. Fast count vs exact count with a filter
print("all products (estimated): " + db.products.estimatedDocumentCount());
print("electronics (exact): " + db.products.countDocuments({ category: "Electronics" }));

// 2. distinct: different categories
print("categories: " + db.products.distinct("category").join(", "));

// 3. findOneAndUpdate: sell one mouse and get the NEW stock back
const updated = db.products.findOneAndUpdate(
  { _id: "P001" },
  { $inc: { stock: -1 } },
  { returnDocument: "after" }          // "before" would return the old version
);
print("mouse stock now: " + updated.stock);

// 4. bulkWrite: several writes in one trip to the server
const bulk = db.products.bulkWrite([
  { insertOne: { document: { _id: "P012", name: "Desk Lamp", category: "Electronics", price: 2200, stock: 30 } } },
  { updateOne: { filter: { _id: "P009" }, update: { $set: { price: 700 } } } },
  { deleteOne: { filter: { _id: "P012" } } }
]);
print("inserted: " + bulk.insertedCount + ", modified: " + bulk.modifiedCount + ", deleted: " + bulk.deletedCount);

// 5. renameCollection (and rename it back)
db.customers.renameCollection("clients");
print("collections: " + db.getCollectionNames().join(", "));
db.clients.renameCollection("customers");

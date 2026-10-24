// delete-documents.js
// Run shopdb-setup.js first, then: mongosh --file delete-documents.js
// Purpose: remove documents with deleteOne() and deleteMany().

db = db.getSiblingDB("shopdb");

print("Orders before: " + db.orders.countDocuments());

// Delete 1: remove ONE order (the first one that matches)
const r1 = db.orders.deleteOne({ _id: "O003" });
print("deleteOne removed " + r1.deletedCount);

// Delete 2: remove ALL pending orders
const r2 = db.orders.deleteMany({ status: "pending" });
print("deleteMany removed " + r2.deletedCount);

print("Orders after: " + db.orders.countDocuments());

// Tip: db.orders.deleteMany({}) would delete EVERY order but keep the empty collection.
// Run shopdb-setup.js again to get all 12 orders back.

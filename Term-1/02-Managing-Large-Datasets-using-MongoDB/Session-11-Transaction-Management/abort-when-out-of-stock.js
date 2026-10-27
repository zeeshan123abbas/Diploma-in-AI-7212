// abort-when-out-of-stock.js
// Needs a replica set. Run shopdb-setup.js first, then: mongosh --file abort-when-out-of-stock.js
// Purpose: abort a transaction because of a business rule (not enough stock).

const session  = db.getMongo().startSession();
const shop     = session.getDatabase("shopdb");
const wanted   = 5;                                    // customer wants 5 units

session.startTransaction();
try {
  // Step 1: insert the order
  shop.orders.insertOne({ _id: "O101", customerId: "C003", items: [{ productId: "P003", qty: wanted }], status: "pending" });

  // Step 2: check stock INSIDE the transaction
  const product = shop.products.findOne({ _id: "P003" });
  if (product.stock < wanted) {
    throw new Error("Only " + product.stock + " in stock");   // jump to catch
  }

  // Step 3: reduce stock and commit (not reached for P003)
  shop.products.updateOne({ _id: "P003" }, { $inc: { stock: -wanted } });
  session.commitTransaction();
} catch (err) {
  session.abortTransaction();                          // the order insert is undone too
  print("Aborted: " + err.message);
} finally {
  session.endSession();
}

// The order O101 must NOT exist
print("O101 exists? " + (db.getSiblingDB("shopdb").orders.countDocuments({ _id: "O101" }) === 1));

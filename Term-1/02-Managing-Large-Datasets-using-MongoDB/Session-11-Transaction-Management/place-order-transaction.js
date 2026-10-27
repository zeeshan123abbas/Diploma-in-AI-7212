// place-order-transaction.js
// Needs a replica set (see README). Run shopdb-setup.js on it first, then:
//   mongosh --file place-order-transaction.js
// Purpose: create an order AND reduce stock in one transaction.

// Step 1: start a session and get collections FROM the session
const session  = db.getMongo().startSession();
const shop     = session.getDatabase("shopdb");
const orders   = shop.orders;
const products = shop.products;

// Step 2: start the transaction
session.startTransaction({
  readConcern:  { level: "snapshot" },        // consistent view of the data
  writeConcern: { w: "majority" }             // commit survives a failover
});

try {
  // Step 3: write 1 - the new order
  orders.insertOne({
    _id: "O100", customerId: "C002", city: "Lahore", orderDate: new Date(),
    items: [{ productId: "P004", qty: 2, price: 3200 }],
    total: 6400, status: "pending", payment: "COD"
  });

  // Step 4: write 2 - reduce stock
  products.updateOne({ _id: "P004" }, { $inc: { stock: -2 } });

  // Step 5: save both together
  session.commitTransaction();
  print("Order saved and stock updated.");
} catch (err) {
  // Something failed: undo BOTH writes
  session.abortTransaction();
  print("Transaction aborted: " + err.message);
} finally {
  session.endSession();
}

// Check the result (outside the transaction)
printjson(db.getSiblingDB("shopdb").products.findOne({ _id: "P004" }, { name: 1, stock: 1 }));

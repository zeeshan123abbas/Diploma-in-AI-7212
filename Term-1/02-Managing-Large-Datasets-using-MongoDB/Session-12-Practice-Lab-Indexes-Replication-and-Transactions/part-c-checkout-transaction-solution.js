// part-c-checkout-transaction-solution.js  (tasks 8-10)
// Needs a replica set with shopdb-setup.js loaded. Run: mongosh --file part-c-checkout-transaction-solution.js

// A reusable checkout function: returns true if the order was saved
function checkout(orderId, customerId, items) {
  const session = db.getMongo().startSession();
  const shop = session.getDatabase("shopdb");
  session.startTransaction({ readConcern: { level: "snapshot" }, writeConcern: { w: "majority" } });
  try {
    let total = 0;
    // Step 1: check and reduce stock for every item
    for (const item of items) {
      const p = shop.products.findOne({ _id: item.productId });
      if (!p || p.stock < item.qty) {
        throw new Error("not enough stock for " + item.productId);
      }
      shop.products.updateOne({ _id: item.productId }, { $inc: { stock: -item.qty } });
      item.price = p.price;
      total += p.price * item.qty;
    }
    // Step 2: save the order
    shop.orders.insertOne({ _id: orderId, customerId: customerId, items: items, total: total, status: "pending", orderDate: new Date() });
    session.commitTransaction();
    print(orderId + " saved, total " + total);
    return true;
  } catch (err) {
    session.abortTransaction();
    print(orderId + " aborted: " + err.message);
    return false;
  } finally {
    session.endSession();
  }
}

// Task 10a: enough stock -> saved
checkout("O200", "C001", [{ productId: "P001", qty: 1 }, { productId: "P008", qty: 2 }]);

// Task 10b: P003 has 0 stock -> whole order aborted (P001 stock is NOT reduced)
checkout("O201", "C002", [{ productId: "P001", qty: 1 }, { productId: "P003", qty: 1 }]);

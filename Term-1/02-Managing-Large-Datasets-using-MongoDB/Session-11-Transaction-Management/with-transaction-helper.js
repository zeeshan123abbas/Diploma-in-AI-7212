// with-transaction-helper.js
// Needs a replica set. Run: mongosh --file with-transaction-helper.js
// Purpose: a money transfer using withTransaction (auto commit + retry).

// Step 1: practice data - two wallets
const plain = db.getSiblingDB("walletdb");
plain.wallets.drop();
plain.wallets.insertMany([
  { _id: "Ali",  balance: 2000 },
  { _id: "Sara", balance: 1000 }
]);

// Step 2: session and collection from the session
const session = db.getMongo().startSession();
const wallets = session.getDatabase("walletdb").wallets;

// Step 3: the helper starts, commits and retries the transaction for us
session.withTransaction(() => {
  wallets.updateOne({ _id: "Ali" },  { $inc: { balance: -500 } });   // take from Ali
  wallets.updateOne({ _id: "Sara" }, { $inc: { balance:  500 } });   // give to Sara
});
session.endSession();

// Step 4: totals must still be 3000
printjson(plain.wallets.find().toArray());
const total = plain.wallets.aggregate([{ $group: { _id: null, sum: { $sum: "$balance" } } }]).toArray()[0].sum;
print("total balance: " + total);

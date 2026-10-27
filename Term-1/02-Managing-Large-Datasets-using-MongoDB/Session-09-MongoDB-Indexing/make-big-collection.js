// make-big-collection.js
// Run: mongosh --file make-big-collection.js   (takes a few seconds)
// Purpose: create 100,000 practice orders so index speed-ups are visible.

db = db.getSiblingDB("shopdb");
db.bigorders.drop();                                   // start fresh

const cities   = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"];
const payments = ["COD", "Card"];
const batch = [];

// Step 1: build the documents in memory
for (let i = 1; i <= 100000; i++) {
  batch.push({
    orderNo: i,                                        // 1, 2, 3 ...
    city: cities[i % 5],                               // cycles through the 5 cities
    payment: payments[i % 2],
    total: Math.floor(Math.random() * 20000),          // random 0 - 19999
    orderDate: new Date(2026, i % 12, (i % 28) + 1)    // spread over the year
  });
}

// Step 2: insert them all at once
db.bigorders.insertMany(batch);
print("bigorders: " + db.bigorders.countDocuments() + " documents");

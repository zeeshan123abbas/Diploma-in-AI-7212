// field-update-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file field-update-operators.js
// Purpose: change fields with $set, $inc, $mul, $unset, $rename, $min, $max,
//          $currentDate and $setOnInsert (upsert).

db = db.getSiblingDB("shopdb");

// 1. $inc (subtract 5 from stock) + $currentDate (record when we changed it)
db.products.updateOne({ _id: "P009" }, { $inc: { stock: -5 }, $currentDate: { updatedAt: true } });

// 2. $mul: 10% price increase for all Books (1.1 x price)
db.products.updateMany({ category: "Books" }, { $mul: { price: 1.1 } });

// 3. $rename: rename the field "tags" to "labels" for one product
db.products.updateOne({ _id: "P006" }, { $rename: { tags: "labels" } });

// 4. $unset: remove the specs field from the laptop stand
db.products.updateOne({ _id: "P010" }, { $unset: { specs: "" } });

// 5. $min: only lower the price if the new value is SMALLER (sale price)
db.products.updateOne({ _id: "P007" }, { $min: { price: 4999 } });

// 6. $max: only raise stock if the new value is LARGER
db.products.updateOne({ _id: "P008" }, { $max: { stock: 50 } });   // 100 > 50, so no change

// 7. Upsert: update P020 if it exists, otherwise INSERT it
db.products.updateOne(
  { _id: "P020" },
  { $set: { price: 1200 }, $setOnInsert: { name: "Desk Lamp", category: "Home", stock: 5 } },
  { upsert: true }
);

// Show the changed products
printjson(db.products.find({ _id: { $in: ["P004", "P006", "P007", "P008", "P009", "P010", "P020"] } }).toArray());

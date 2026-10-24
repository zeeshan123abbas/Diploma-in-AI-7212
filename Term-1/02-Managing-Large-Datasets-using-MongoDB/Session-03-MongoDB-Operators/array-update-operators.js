// array-update-operators.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file array-update-operators.js
// Purpose: change arrays with $push, $each, $addToSet, $pull, $pop and positional $.

db = db.getSiblingDB("shopdb");

// 1. $push: add one rating to the Python book
db.products.updateOne({ _id: "P004" }, { $push: { ratings: 5 } });

// 2. $push + $each: add several ratings at once
db.products.updateOne({ _id: "P009" }, { $push: { ratings: { $each: [4, 5, 3] } } });

// 3. $addToSet: add a tag only if it is not already there (run twice - still one copy)
db.products.updateOne({ _id: "P001" }, { $addToSet: { tags: "wireless" } });
db.products.updateOne({ _id: "P001" }, { $addToSet: { tags: "wireless" } });

// 4. $pull: remove the tag "eid" from the lawn suit
db.products.updateOne({ _id: "P007" }, { $pull: { tags: "eid" } });

// 5. $pop: remove the LAST tag (1) of the charger; use -1 for the first one
db.products.updateOne({ _id: "P002" }, { $pop: { tags: 1 } });

// 6. Positional $: change qty of the P001 line inside order O001 to 3
db.orders.updateOne(
  { _id: "O001", "items.productId": "P001" },
  { $set: { "items.$.qty": 3 } }
);

// Show the results
printjson(db.products.find({ _id: { $in: ["P001", "P002", "P004", "P007", "P009"] } },
  { name: 1, tags: 1, ratings: 1 }).toArray());
printjson(db.orders.findOne({ _id: "O001" }, { items: 1 }));

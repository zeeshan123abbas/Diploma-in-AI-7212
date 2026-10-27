// unwind-items.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file unwind-items.js
// Purpose: $unwind an array, then group (top 3 best-selling products)

db = db.getSiblingDB("shopdb");

const result = db.orders.aggregate([
  // ignore cancelled orders
  { $match: { status: { $ne: "cancelled" } } },

  // one document per item in the items array
  { $unwind: "$items" },

  // add up the quantity sold for each product
  { $group: { _id: "$items.productId", unitsSold: { $sum: "$items.qty" } } },

  // best sellers first, keep 3
  { $sort: { unitsSold: -1 } },
  { $limit: 3 }
]).toArray();

printjson(result);

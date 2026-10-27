// sales-by-city.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file sales-by-city.js
// Purpose: $match -> $group -> $sort (revenue per city)

db = db.getSiblingDB("shopdb");

const result = db.orders.aggregate([
  // Stage 1: keep only delivered orders
  { $match: { status: "delivered" } },

  // Stage 2: one group per city; add totals and count orders
  { $group: {
      _id: "$city",                    // grouping key = the city field
      revenue: { $sum: "$total" },     // add up the totals
      orders:  { $sum: 1 }             // +1 for every order = count
  } },

  // Stage 3: highest revenue first
  { $sort: { revenue: -1 } }
]).toArray();

printjson(result);

// Bonus: grand total of ALL delivered orders (one group with _id: null)
printjson(db.orders.aggregate([
  { $match: { status: "delivered" } },
  { $group: { _id: null, grandTotal: { $sum: "$total" } } }
]).toArray());

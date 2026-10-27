// monthly-report.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file monthly-report.js
// Purpose: revenue per month using a date expression

db = db.getSiblingDB("shopdb");

const result = db.orders.aggregate([
  { $match: { status: { $ne: "cancelled" } } },

  // add a "month" field like "2026-03"
  { $addFields: { month: { $dateToString: { format: "%Y-%m", date: "$orderDate" } } } },

  // group by that month
  { $group: {
      _id: "$month",
      revenue:  { $sum: "$total" },
      orders:   { $sum: 1 },
      avgOrder: { $avg: "$total" }
  } },

  // round the average and rename _id
  { $project: { _id: 0, month: "$_id", revenue: 1, orders: 1, avgOrder: { $round: ["$avgOrder", 0] } } },

  // oldest month first
  { $sort: { month: 1 } }
]).toArray();

printjson(result);

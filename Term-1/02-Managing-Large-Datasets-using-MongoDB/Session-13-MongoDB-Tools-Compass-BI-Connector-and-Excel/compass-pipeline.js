// compass-pipeline.js
// Paste the array below into Compass: shopdb > orders > Aggregations > "</> Text" mode.
// Or run it in mongosh:  mongosh --file compass-pipeline.js
// Purpose: revenue per city (excluding cancelled orders).

const pipeline = [
  { $match: { status: { $ne: "cancelled" } } },                          // 1. filter
  { $group: { _id: "$city", revenue: { $sum: "$total" }, orders: { $sum: 1 } } }, // 2. group
  { $sort: { revenue: -1 } }                                            // 3. order
];

db = db.getSiblingDB("shopdb");
printjson(db.orders.aggregate(pipeline).toArray());

// Tip: in Compass, click "Export to Language" to see this pipeline as Python, Java or C# code.

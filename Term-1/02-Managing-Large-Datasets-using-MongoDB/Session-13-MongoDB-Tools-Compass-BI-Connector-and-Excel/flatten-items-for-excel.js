// flatten-items-for-excel.js
// Run shopdb-setup.js first, then: mongosh --file flatten-items-for-excel.js
// Purpose: turn the items array into flat rows so the CSV export is clean.

db = db.getSiblingDB("shopdb");

db.orders.aggregate([
  // 1. one document per item
  { $unwind: "$items" },

  // 2. keep simple, flat fields only
  { $project: {
      _id: 0,
      orderId:   "$_id",
      city:      1,
      productId: "$items.productId",
      qty:       "$items.qty",
      lineTotal: { $multiply: ["$items.qty", "$items.price"] }
  } },

  // 3. save the result into a new collection (replaced each run)
  { $out: "order_lines" }
]);

print("order_lines rows: " + db.order_lines.countDocuments());
print("Now export it:");
print("mongoexport --db shopdb --collection order_lines --type=csv --fields orderId,city,productId,qty,lineTotal --out order-lines.csv");

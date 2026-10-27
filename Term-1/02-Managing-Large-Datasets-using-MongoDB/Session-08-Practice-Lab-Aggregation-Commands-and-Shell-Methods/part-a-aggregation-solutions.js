// part-a-aggregation-solutions.js  (tasks 1-5)
// Run shopdb-setup.js first, then: mongosh --file part-a-aggregation-solutions.js

db = db.getSiblingDB("shopdb");

// Task 1: revenue per payment method (delivered only)
print("--- Task 1 ---");
printjson(db.orders.aggregate([
  { $match: { status: "delivered" } },
  { $group: { _id: "$payment", revenue: { $sum: "$total" } } },
  { $sort: { revenue: -1 } }
]).toArray());

// Task 2: orders and spending per customer, with names
print("--- Task 2 ---");
printjson(db.orders.aggregate([
  { $group: { _id: "$customerId", orders: { $sum: 1 }, spent: { $sum: "$total" } } },
  { $lookup: { from: "customers", localField: "_id", foreignField: "_id", as: "c" } },
  { $project: { _id: 0, name: { $first: "$c.name" }, orders: 1, spent: 1 } },
  { $sort: { spent: -1 } }
]).toArray());

// Task 3: top 3 products by average rating (skip empty ratings)
print("--- Task 3 ---");
printjson(db.products.aggregate([
  { $match: { "ratings.0": { $exists: true } } },          // at least one rating
  { $project: { _id: 0, name: 1, avgRating: { $round: [{ $avg: "$ratings" }, 2] } } },
  { $sort: { avgRating: -1 } },
  { $limit: 3 }
]).toArray());

// Task 4: Electronics spend per city
print("--- Task 4 ---");
printjson(db.orders.aggregate([
  { $match: { status: { $ne: "cancelled" } } },
  { $unwind: "$items" },
  { $lookup: { from: "products", localField: "items.productId", foreignField: "_id", as: "product" } },
  { $unwind: "$product" },
  { $match: { "product.category": "Electronics" } },       // change to "Books" for part 2
  { $group: { _id: "$city", spent: { $sum: { $multiply: ["$items.qty", "$items.price"] } } } },
  { $sort: { spent: -1 } }
]).toArray());

// Task 5: orders per weekday name
print("--- Task 5 ---");
printjson(db.orders.aggregate([
  { $group: { _id: { $dayOfWeek: "$orderDate" }, orders: { $sum: 1 } } },
  { $project: {
      _id: 0,
      orders: 1,
      day: { $arrayElemAt: [["", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], "$_id"] }
  } },
  { $sort: { orders: -1 } }
]).toArray());

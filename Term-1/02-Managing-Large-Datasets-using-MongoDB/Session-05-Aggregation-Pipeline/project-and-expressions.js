// project-and-expressions.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file project-and-expressions.js
// Purpose: compute new fields with $project and expressions

db = db.getSiblingDB("shopdb");

const result = db.products.aggregate([
  { $project: {
      _id: 0,
      name: 1,
      price: 1,
      // arithmetic: price + 18% tax, rounded to 0 decimals
      priceWithTax: { $round: [{ $multiply: ["$price", 1.18] }, 0] },
      // conditional: label depending on stock
      stockStatus: { $cond: { if: { $gt: ["$stock", 0] }, then: "In stock", else: "Sold out" } },
      // array: number of ratings and their average
      ratingCount: { $size: "$ratings" },
      avgRating:   { $avg: "$ratings" },
      // string: category in capitals
      categoryUpper: { $toUpper: "$category" }
  } },
  { $sort: { price: -1 } }
]).toArray();

printjson(result);

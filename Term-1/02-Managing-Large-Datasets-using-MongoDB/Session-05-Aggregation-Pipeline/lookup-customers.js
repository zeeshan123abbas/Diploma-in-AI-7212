// lookup-customers.js
// Run shopdb-setup.js (Session 02) first, then: mongosh --file lookup-customers.js
// Purpose: join orders with customers using $lookup

db = db.getSiblingDB("shopdb");

const result = db.orders.aggregate([
  // Stage 1: find the matching customer for each order
  { $lookup: {
      from: "customers",          // the other collection
      localField: "customerId",   // field in orders
      foreignField: "_id",        // field in customers
      as: "customer"              // name of the new array field
  } },

  // Stage 2: turn the 1-element array into a plain object
  { $unwind: "$customer" },

  // Stage 3: keep only what we want to show
  { $project: { total: 1, status: 1, customerName: "$customer.name", customerCity: "$customer.city" } }
]).toArray();

printjson(result);

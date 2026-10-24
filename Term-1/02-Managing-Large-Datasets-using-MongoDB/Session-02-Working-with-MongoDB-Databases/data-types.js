// data-types.js
// Run: mongosh --file data-types.js
// Purpose: see the most common MongoDB (BSON) data types in one document.

// Step 1: use the practice database
db = db.getSiblingDB("shopdb");

// Step 2: start with an empty demo collection
db.typesDemo.drop();

// Step 3: insert one document that uses many different types
db.typesDemo.insertOne({
  name: "Sample Product",                 // String
  qty: NumberInt(5),                      // Int32 (whole number)
  views: NumberLong(1500000),             // Int64 (big whole number)
  rating: 4.5,                            // Double (decimal number)
  price: NumberDecimal("1999.99"),        // Decimal128 (exact, good for money)
  inStock: true,                          // Boolean
  addedOn: new Date(),                    // Date (current date and time, stored in UTC)
  tags: ["new", "sale"],                  // Array
  supplier: { name: "ABC Traders", city: "Lahore" }, // Embedded document
  discount: null                          // Null (no value)
});

// Step 4: read it back - look at how each type is displayed
printjson(db.typesDemo.findOne());

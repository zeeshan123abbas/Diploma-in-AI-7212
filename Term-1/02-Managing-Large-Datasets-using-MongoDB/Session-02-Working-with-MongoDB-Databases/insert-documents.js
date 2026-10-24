// insert-documents.js
// Run shopdb-setup.js first, then: mongosh --file insert-documents.js
// Purpose: add new products with insertOne() and insertMany().

db = db.getSiblingDB("shopdb");

// Step 1: remove these ids if they exist from an earlier run (avoids duplicate key errors)
db.products.deleteMany({ _id: { $in: ["P011", "P012", "P013"] } });

// Step 2: insert ONE document
const one = db.products.insertOne({
  _id: "P011", name: "Webcam HD", category: "Electronics",
  price: 5200, stock: 10, tags: ["computer"]
});
print("insertOne added id: " + one.insertedId);

// Step 3: insert MANY documents (an array of documents)
const many = db.products.insertMany([
  { _id: "P012", name: "Urdu Novel", category: "Books", price: 900, stock: 30, tags: ["urdu"] },
  { _id: "P013", name: "Prayer Mat", category: "Home", price: 1500, stock: 40, tags: ["gift"] }
]);
print("insertMany added ids: " + Object.values(many.insertedIds).join(", "));

// Step 4: insert WITHOUT an _id - MongoDB creates an ObjectId for us
db.feedback.insertOne({ text: "Fast delivery!", stars: 5 });
printjson(db.feedback.findOne());

// Step 5: confirm the new total
print("Products now: " + db.products.countDocuments());

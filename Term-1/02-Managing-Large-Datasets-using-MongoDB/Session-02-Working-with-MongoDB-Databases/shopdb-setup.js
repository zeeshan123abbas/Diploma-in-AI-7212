// shopdb-setup.js
// Creates (or re-creates) the practice database "shopdb" used in every session.
// Run it from a terminal:   mongosh --file shopdb-setup.js
// or inside mongosh:         load("shopdb-setup.js")

// Step 1: switch to the shopdb database (it is created on the first insert)
db = db.getSiblingDB("shopdb");

// Step 2: remove old data so we always start fresh
db.products.drop();
db.customers.drop();
db.orders.drop();

// Step 3: insert 10 products
db.products.insertMany([
  {"_id": "P001", "name": "Wireless Mouse", "category": "Electronics", "price": 1800, "stock": 45, "tags": ["computer", "accessory"], "ratings": [5, 4, 4], "specs": {"brand": "Logitech", "warrantyMonths": 12}},
  {"_id": "P002", "name": "USB-C Charger 65W", "category": "Electronics", "price": 4500, "stock": 20, "tags": ["mobile", "laptop", "charger"], "ratings": [5, 5, 4], "specs": {"brand": "Anker", "warrantyMonths": 18}},
  {"_id": "P003", "name": "Bluetooth Earbuds", "category": "Electronics", "price": 6999, "stock": 0, "tags": ["audio", "mobile"], "ratings": [3, 4], "specs": {"brand": "Audionic", "warrantyMonths": 6}},
  {"_id": "P004", "name": "Python Crash Course", "category": "Books", "price": 3200, "stock": 12, "tags": ["programming", "python"], "ratings": [5, 5, 5, 4]},
  {"_id": "P005", "name": "Data Science Handbook", "category": "Books", "price": 4100, "stock": 8, "tags": ["data", "python", "statistics"], "ratings": [4, 5]},
  {"_id": "P006", "name": "Cotton Kurta", "category": "Clothing", "price": 2800, "stock": 60, "tags": ["men", "summer"], "ratings": [4, 3, 4]},
  {"_id": "P007", "name": "Lawn Suit 3-Piece", "category": "Clothing", "price": 5500, "stock": 25, "tags": ["women", "summer", "eid"], "ratings": [5, 4]},
  {"_id": "P008", "name": "Basmati Rice 5kg", "category": "Grocery", "price": 2400, "stock": 100, "tags": ["rice", "staple"], "ratings": [4, 4, 5]},
  {"_id": "P009", "name": "Green Tea 50 Bags", "category": "Grocery", "price": 650, "stock": 80, "tags": ["tea", "healthy"], "ratings": []},
  {"_id": "P010", "name": "Laptop Stand", "category": "Electronics", "price": 3500, "stock": 15, "tags": ["computer", "office"], "ratings": [4], "specs": {"brand": "Generic"}}
]);

// Step 4: insert 6 customers
db.customers.insertMany([
  {"_id": "C001", "name": "Ayesha Khan", "email": "ayesha@example.com", "city": "Karachi", "age": 24, "isPremium": true, "joined": ISODate("2025-03-10T00:00:00Z")},
  {"_id": "C002", "name": "Bilal Ahmed", "email": "bilal@example.com", "city": "Lahore", "age": 31, "isPremium": false, "joined": ISODate("2025-06-22T00:00:00Z")},
  {"_id": "C003", "name": "Sara Ali", "email": "sara@example.com", "city": "Karachi", "age": 19, "isPremium": false, "joined": ISODate("2025-11-05T00:00:00Z")},
  {"_id": "C004", "name": "Usman Tariq", "email": "usman@example.com", "city": "Islamabad", "age": 42, "isPremium": true, "joined": ISODate("2024-12-01T00:00:00Z")},
  {"_id": "C005", "name": "Hina Raza", "email": "hina@example.com", "city": "Lahore", "age": 27, "isPremium": true, "joined": ISODate("2026-01-15T00:00:00Z")},
  {"_id": "C006", "name": "Faraz Hussain", "email": "faraz@example.com", "city": "Karachi", "age": 35, "isPremium": false, "joined": ISODate("2026-02-20T00:00:00Z")}
]);

// Step 5: insert 12 orders
db.orders.insertMany([
  {"_id": "O001", "customerId": "C001", "city": "Karachi", "orderDate": ISODate("2026-01-05T00:00:00Z"), "items": [{"productId": "P001", "qty": 2, "price": 1800}, {"productId": "P004", "qty": 1, "price": 3200}], "total": 6800, "status": "delivered", "payment": "Card"},
  {"_id": "O002", "customerId": "C002", "city": "Lahore", "orderDate": ISODate("2026-01-12T00:00:00Z"), "items": [{"productId": "P008", "qty": 3, "price": 2400}], "total": 7200, "status": "delivered", "payment": "COD"},
  {"_id": "O003", "customerId": "C003", "city": "Karachi", "orderDate": ISODate("2026-01-20T00:00:00Z"), "items": [{"productId": "P003", "qty": 1, "price": 6999}], "total": 6999, "status": "cancelled", "payment": "Card"},
  {"_id": "O004", "customerId": "C001", "city": "Karachi", "orderDate": ISODate("2026-02-02T00:00:00Z"), "items": [{"productId": "P005", "qty": 1, "price": 4100}, {"productId": "P009", "qty": 4, "price": 650}], "total": 6700, "status": "delivered", "payment": "COD"},
  {"_id": "O005", "customerId": "C004", "city": "Islamabad", "orderDate": ISODate("2026-02-14T00:00:00Z"), "items": [{"productId": "P002", "qty": 1, "price": 4500}, {"productId": "P010", "qty": 1, "price": 3500}], "total": 8000, "status": "delivered", "payment": "Card"},
  {"_id": "O006", "customerId": "C005", "city": "Lahore", "orderDate": ISODate("2026-02-25T00:00:00Z"), "items": [{"productId": "P007", "qty": 2, "price": 5500}], "total": 11000, "status": "delivered", "payment": "Card"},
  {"_id": "O007", "customerId": "C006", "city": "Karachi", "orderDate": ISODate("2026-03-03T00:00:00Z"), "items": [{"productId": "P006", "qty": 1, "price": 2800}, {"productId": "P008", "qty": 1, "price": 2400}], "total": 5200, "status": "shipped", "payment": "COD"},
  {"_id": "O008", "customerId": "C002", "city": "Lahore", "orderDate": ISODate("2026-03-09T00:00:00Z"), "items": [{"productId": "P001", "qty": 1, "price": 1800}], "total": 1800, "status": "pending", "payment": "COD"},
  {"_id": "O009", "customerId": "C004", "city": "Islamabad", "orderDate": ISODate("2026-03-15T00:00:00Z"), "items": [{"productId": "P004", "qty": 2, "price": 3200}, {"productId": "P005", "qty": 1, "price": 4100}], "total": 10500, "status": "delivered", "payment": "Card"},
  {"_id": "O010", "customerId": "C003", "city": "Karachi", "orderDate": ISODate("2026-03-21T00:00:00Z"), "items": [{"productId": "P009", "qty": 2, "price": 650}], "total": 1300, "status": "pending", "payment": "COD"},
  {"_id": "O011", "customerId": "C005", "city": "Lahore", "orderDate": ISODate("2026-03-28T00:00:00Z"), "items": [{"productId": "P002", "qty": 1, "price": 4500}], "total": 4500, "status": "shipped", "payment": "Card"},
  {"_id": "O012", "customerId": "C001", "city": "Karachi", "orderDate": ISODate("2026-04-02T00:00:00Z"), "items": [{"productId": "P010", "qty": 1, "price": 3500}, {"productId": "P001", "qty": 1, "price": 1800}], "total": 5300, "status": "pending", "payment": "Card"}
]);

// Step 6: show what we created
print("shopdb is ready:");
print("  products : " + db.products.countDocuments());
print("  customers: " + db.customers.countDocuments());
print("  orders   : " + db.orders.countDocuments());

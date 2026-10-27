// role-methods.js
// Run: mongosh --file role-methods.js
// Purpose: create a custom role with exactly the rights a clerk needs.

db = db.getSiblingDB("shopdb");

// 1. Custom role: read products, insert/update orders, NO delete
db.createRole({
  role: "orderClerk",
  privileges: [
    { resource: { db: "shopdb", collection: "products" }, actions: ["find"] },
    { resource: { db: "shopdb", collection: "orders" },   actions: ["find", "insert", "update"] }
  ],
  roles: []                                   // inherits no other roles
});

// 2. Give the role to a new user
db.createUser({ user: "clerk1", pwd: "Clerk#2026", roles: ["orderClerk"] });

// 3. Show the role and its privileges
printjson(db.getRole("orderClerk", { showPrivileges: true }));

// 4. Clean up
db.dropUser("clerk1");
db.dropRole("orderClerk");
print("demo user and role removed");

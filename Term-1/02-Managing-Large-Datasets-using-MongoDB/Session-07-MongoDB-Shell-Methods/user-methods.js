// user-methods.js
// Run: mongosh --file user-methods.js
// Purpose: create, update and remove a user with shell methods.

db = db.getSiblingDB("shopdb");

// 1. Create a read-only user (demo password; in real life use passwordPrompt())
db.createUser({
  user: "analyst",
  pwd: "Analyst#2026",
  roles: [{ role: "read", db: "shopdb" }]
});

// 2. Give the user more rights later
db.grantRolesToUser("analyst", [{ role: "readWrite", db: "shopdb" }]);

// 3. Take a right away again
db.revokeRolesFromUser("analyst", [{ role: "readWrite", db: "shopdb" }]);

// 4. Change the password
db.changeUserPassword("analyst", "NewPass#2026");

// 5. See all users of this database
printjson(db.getUsers());

// 6. Remove the user
db.dropUser("analyst");
print("analyst removed");

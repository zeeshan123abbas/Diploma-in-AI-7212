// auth-commands.js
// Run: mongosh --file auth-commands.js
// Purpose: create, view and remove a user with commands.
// Works on a local server without access control. With access control on,
// log in first as a user who has the userAdmin role.

db = db.getSiblingDB("shopdb");

// 1. Create a read-only user for shopdb
db.runCommand({
  createUser: "reporter",
  pwd: "Rep0rt#2026",                       // demo password only - never hard-code real ones
  roles: [{ role: "read", db: "shopdb" }]
});

// 2. View the user
printjson(db.runCommand({ usersInfo: "reporter" }).users);

// 3. How the user would log in:
//    mongosh "mongodb://localhost:27017/shopdb" -u reporter -p
//    or inside mongosh:  db.auth("reporter", passwordPrompt())

// 4. Remove the user (clean up)
db.runCommand({ dropUser: "reporter" });
print("reporter removed");

// first-commands.js
// Run from a terminal:  mongosh --file first-commands.js
// Purpose: check that mongosh can talk to the MongoDB server.

// Step 1: ask the server for its version
print("Server version: " + db.version());

// Step 2: show the database we are connected to (default is "test")
print("Current database: " + db.getName());

// Step 3: list all databases (same as typing "show dbs" in the shell)
const names = db.getMongo().getDBNames();
print("Databases on this server: " + names.join(", "));

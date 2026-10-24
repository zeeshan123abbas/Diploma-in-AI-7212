// first-document.js
// Run from a terminal:  mongosh --file first-document.js
// Purpose: create a database, a collection and one document, then read it back.

// Step 1: switch to a database called "hello" (it does not exist yet - that is fine)
db = db.getSiblingDB("hello");

// Step 2: insert one document into the "greetings" collection
//         MongoDB creates the database and the collection automatically
db.greetings.insertOne({ text: "Assalam o Alaikum, MongoDB!", lang: "en" });

// Step 3: read one document back and print it nicely
printjson(db.greetings.findOne());

// Step 4: count how many greetings we have (it grows each time you run this file)
print("Total greetings: " + db.greetings.countDocuments());

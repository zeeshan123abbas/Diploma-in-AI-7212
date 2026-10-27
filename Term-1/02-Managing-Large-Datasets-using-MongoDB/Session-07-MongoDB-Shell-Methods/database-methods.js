// database-methods.js
// Run: mongosh --file database-methods.js
// Purpose: database methods and a collection with a schema validator.

db = db.getSiblingDB("schooldb");

// 1. Basic information
print("database: " + db.getName());

// 2. Create a collection with rules (drop first so the script can re-run)
db.students.drop();
db.createCollection("students", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "age"],                        // these fields must exist
      properties: {
        name: { bsonType: "string" },
        age:  { bsonType: "int", minimum: 16, maximum: 60 }
      }
    }
  }
});

// 3. A valid insert (NumberInt makes the number a 32-bit int)
db.students.insertOne({ name: "Ayesha", age: NumberInt(21) });
print("valid student inserted");

// 4. An invalid insert: age too small -> error is caught
try {
  db.students.insertOne({ name: "Tiny", age: NumberInt(10) });
} catch (err) {
  print("rejected: " + err.message);
}

// 5. Collections and size
print("collections: " + db.getCollectionNames().join(", "));
print("objects: " + db.stats().objects);

// 6. Clean up the demo database
db.dropDatabase();

// lab-write-solutions.js  (Part C)
// Run library-setup.js first, then: mongosh --file lab-write-solutions.js

db = db.getSiblingDB("librarydb");

// Task 8: insert a new book and find it
const added = db.books.insertOne({ _id: 9, title: "MongoDB Made Easy", author: "Zeeshan Abbas", year: 2026, copies: 6, genres: ["data", "nosql"], available: true });
print("inserted _id: " + added.insertedId);
printjson(db.books.findOne({ title: "MongoDB Made Easy" }));

// Task 9: add 2 copies to book 2, add a genre to book 1 (no duplicates)
db.books.updateOne({ _id: 2 }, { $inc: { copies: 2 } });
db.books.updateOne({ _id: 1 }, { $addToSet: { genres: "beginner" } });

// Task 10: mark books with 0 copies as not available
const upd = db.books.updateMany({ copies: 0 }, { $set: { available: false } });
print("matched: " + upd.matchedCount + ", modified: " + upd.modifiedCount);

// Task 11: delete books before 2015 - count first, then delete
print("will delete: " + db.books.countDocuments({ year: { $lt: 2015 } }));
const del = db.books.deleteMany({ year: { $lt: 2015 } });
print("deleted: " + del.deletedCount);

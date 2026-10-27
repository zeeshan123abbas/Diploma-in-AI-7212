// lab-read-solutions.js  (Parts A and B)
// Run library-setup.js first, then: mongosh --file lab-read-solutions.js

db = db.getSiblingDB("librarydb");

// Task 1: all books, then only title and author
printjson(db.books.find().toArray());
printjson(db.books.find({}, { _id: 0, title: 1, author: 1 }).toArray());

// Task 2: how many books are available
print("available: " + db.books.countDocuments({ available: true }));

// Task 3: 3 newest books, then page 2 of the same list
printjson(db.books.find({}, { title: 1, year: 1 }).sort({ year: -1 }).limit(3).toArray());
printjson(db.books.find({}, { title: 1, year: 1 }).sort({ year: -1 }).skip(3).limit(3).toArray());

// Task 4: 1 to 3 copies
printjson(db.books.find({ copies: { $gte: 1, $lte: 3 } }, { title: 1, copies: 1 }).toArray());

// Task 5: genre "data" or "ai"
printjson(db.books.find({ genres: { $in: ["data", "ai"] } }, { title: 1, genres: 1 }).toArray());

// Task 6a: books that HAVE a rating field
printjson(db.books.find({ rating: { $exists: true } }, { title: 1, rating: 1 }).toArray());
// Task 6b: books with exactly 2 genres
printjson(db.books.find({ genres: { $size: 2 } }, { title: 1, genres: 1 }).toArray());

// Task 7: title starts with "Data"
printjson(db.books.find({ title: { $regex: /^Data/ } }, { title: 1 }).toArray());

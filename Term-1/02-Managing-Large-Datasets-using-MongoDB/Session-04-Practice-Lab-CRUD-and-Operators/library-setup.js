// library-setup.js
// Builds the small "librarydb" database used in this practice lab.
// Run: mongosh --file library-setup.js

// Step 1: switch to librarydb (same as "use librarydb")
db = db.getSiblingDB("librarydb");

// Step 2: start fresh
db.books.drop();

// Step 3: insert 8 books
db.books.insertMany([
  { _id: 1, title: "Python Basics",          author: "Ali Raza",     year: 2021, copies: 4, genres: ["programming"],             available: true,  rating: 4.5 },
  { _id: 2, title: "Data Stories",           author: "Sana Mir",     year: 2019, copies: 0, genres: ["data", "statistics"],      available: false },
  { _id: 3, title: "Intro to AI",            author: "Kamran Shah",  year: 2023, copies: 2, genres: ["ai", "programming"],       available: true,  rating: 4.8 },
  { _id: 4, title: "SQL for Everyone",       author: "Nadia Iqbal",  year: 2016, copies: 5, genres: ["data"],                    available: true },
  { _id: 5, title: "Old Computing Classics", author: "Tariq Jamil",  year: 2012, copies: 1, genres: ["history"],                 available: true },
  { _id: 6, title: "Data Cleaning Handbook", author: "Sana Mir",     year: 2022, copies: 3, genres: ["data", "python"],          available: true,  rating: 4.1 },
  { _id: 7, title: "Machine Learning Notes", author: "Rabia Noor",   year: 2024, copies: 0, genres: ["ai", "data", "math"],      available: true },
  { _id: 8, title: "Networking 101",         author: "Usman Tariq",  year: 2014, copies: 2, genres: ["networks"],                available: true }
]);

// Step 4: confirm
print("librarydb ready, books: " + db.books.countDocuments());

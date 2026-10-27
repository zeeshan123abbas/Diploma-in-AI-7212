// part-a-index-tuning-solutions.js  (tasks 1-4)
// Run make-big-collection.js (Session 09) first, then: mongosh --file part-a-index-tuning-solutions.js

db = db.getSiblingDB("shopdb");
db.bigorders.dropIndexes();                        // start without extra indexes

// Helper: print the key numbers from explain()
function measure(label, cursor) {
  const s = cursor.explain("executionStats").executionStats;
  print(label + ": examined " + s.totalDocsExamined + ", returned " + s.nReturned + ", " + s.executionTimeMillis + " ms");
}

// Task 1: measure before
const q = { payment: "COD", city: "Quetta" };
measure("before", db.bigorders.find(q).sort({ orderDate: -1 }));

// Task 2: ESR index = Equality (payment, city) then Sort (orderDate)
db.bigorders.createIndex({ payment: 1, city: 1, orderDate: -1 });
measure("after ", db.bigorders.find(q).sort({ orderDate: -1 }));

// Task 3: covered query (filter + projection only use indexed fields, _id hidden)
db.bigorders.createIndex({ city: 1, total: 1 });
measure("covered", db.bigorders.find({ city: "Lahore", total: { $gt: 19000 } }, { _id: 0, city: 1, total: 1 }));

// Task 4: find indexes never used and drop them (_id_ is kept)
db.bigorders.createIndex({ payment: 1 });          // an index nobody uses
db.bigorders.aggregate([{ $indexStats: {} }]).forEach(stat => {
  if (stat.name !== "_id_" && stat.accesses.ops == 0) {
    print("dropping unused index: " + stat.name);
    db.bigorders.dropIndex(stat.name);
  }
});

// single-field-index.js
// Run make-big-collection.js first, then: mongosh --file single-field-index.js
// Purpose: measure a query before and after creating an index.

db = db.getSiblingDB("shopdb");
db.bigorders.dropIndexes();                            // remove old indexes (keeps _id)

// Small helper that prints the useful parts of explain()
function show(label, cursor) {
  const stats = cursor.explain("executionStats").executionStats;
  print(label + " -> examined: " + stats.totalDocsExamined +
        ", returned: " + stats.nReturned +
        ", ms: " + stats.executionTimeMillis);
}

// 1. BEFORE: no index on orderNo -> collection scan
show("before index", db.bigorders.find({ orderNo: 77777 }));

// 2. Create the index
db.bigorders.createIndex({ orderNo: 1 });

// 3. AFTER: index scan, only 1 document examined
show("after index ", db.bigorders.find({ orderNo: 77777 }));

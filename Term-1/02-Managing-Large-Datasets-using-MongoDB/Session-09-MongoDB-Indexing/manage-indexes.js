// manage-indexes.js
// Run other-index-types.js first, then: mongosh --file manage-indexes.js
// Purpose: list, hide, unhide and drop indexes.

db = db.getSiblingDB("shopdb");

// 1. List indexes (name + keys)
db.bigorders.getIndexes().forEach(i => print(i.name + "  " + JSON.stringify(i.key)));

// 2. Hide an index: still updated, but queries ignore it (safe test before dropping)
db.bigorders.hideIndex("city_1_total_1");
db.bigorders.unhideIndex("city_1_total_1");

// 3. How often has each index been used?
db.bigorders.aggregate([{ $indexStats: {} }]).forEach(s => print(s.name + " used " + s.accesses.ops + " times"));

// 4. Drop one index by name, then all the rest (the _id index always stays)
db.bigorders.dropIndex("city_1_total_1");
db.bigorders.dropIndexes();
db.products.dropIndex("tags_1");
db.customers.dropIndex("email_1");
print("left on bigorders: " + db.bigorders.getIndexes().map(i => i.name).join(", "));

// sharding-setup.js
// Run against the mongos router:  mongosh --port 27040 --file sharding-setup.js
// Purpose: add shards, shard a collection and see how data is spread.

// Step 1: tell the cluster about the two shards
sh.addShard("shardA/localhost:27031");
sh.addShard("shardB/localhost:27032");

// Step 2: allow sharding for the database (optional in MongoDB 6+, but clear for learning)
sh.enableSharding("shopdb");

// Step 3: shard the collection on a HASHED key so inserts spread evenly
sh.shardCollection("shopdb.bigorders", { orderNo: "hashed" });

// Step 4: insert 20,000 documents through mongos
db = db.getSiblingDB("shopdb");
const docs = [];
for (let i = 1; i <= 20000; i++) {
  docs.push({ orderNo: i, city: ["Karachi", "Lahore", "Quetta"][i % 3], total: i % 9000 });
}
db.bigorders.insertMany(docs);

// Step 5: how many documents live on each shard?
db.bigorders.getShardDistribution();

// Step 6: overview of the whole cluster
sh.status();

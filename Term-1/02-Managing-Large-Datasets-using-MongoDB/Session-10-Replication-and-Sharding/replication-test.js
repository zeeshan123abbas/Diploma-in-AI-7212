// replication-test.js
// Run:  mongosh "mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=rs0" --file replication-test.js
// Purpose: write on the primary, read from a secondary, then force an election.

db = db.getSiblingDB("rstest");

// 1. Write on the primary and wait until most members have it
db.notes.insertOne(
  { text: "Hello replica set", at: new Date() },
  { writeConcern: { w: "majority" } }
);
print("written on primary: " + db.hello().primary);

// 2. Read from a secondary
db.getMongo().setReadPref("secondary");
printjson(db.notes.find().toArray());
db.getMongo().setReadPref("primary");        // back to the default

// 3. Ask the primary to step down for 60 seconds -> an election happens
try {
  rs.stepDown(60);
} catch (err) {
  print("connection reset during election (this is normal)");
}

sleep(12000);                                 // give the election time
print("new primary: " + db.hello().primary);

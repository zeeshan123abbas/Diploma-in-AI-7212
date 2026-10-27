// part-b-replica-set-solutions.js  (tasks 5-7)
// Start the replica set from Session 10, then:
//   mongosh "mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=rs0" --file part-b-replica-set-solutions.js

// Task 5: state of every member
rs.status().members.forEach(m => print(m.name + " -> " + m.stateStr));

// Task 6: majority write, then read from a secondary
const lab = db.getSiblingDB("labdb");
lab.events.insertOne({ msg: "lab 12 test", at: new Date() }, { writeConcern: { w: "majority" } });
db.getMongo().setReadPref("secondary");
printjson(lab.events.find().sort({ at: -1 }).limit(1).toArray());
db.getMongo().setReadPref("primary");

// Task 7: step down and time the election
const oldPrimary = db.hello().primary;
const start = new Date();
try { rs.stepDown(30); } catch (e) { print("stepDown sent"); }

let newPrimary = undefined;
while (!newPrimary || newPrimary === oldPrimary) {    // poll every second
  sleep(1000);
  try { newPrimary = db.hello().primary; } catch (e) { /* reconnecting */ }
}
print("old primary: " + oldPrimary + ", new primary: " + newPrimary);
print("election took about " + Math.round((new Date() - start) / 1000) + " seconds");

// replica-set-init.js
// Run after the start script:  mongosh --port 27017 --file replica-set-init.js
// Purpose: join the 3 servers into replica set rs0 and show their roles.

// Step 1: initiate the set with its 3 members
rs.initiate({
  _id: "rs0",                                  // must match --replSet
  members: [
    { _id: 0, host: "localhost:27017" },
    { _id: 1, host: "localhost:27018" },
    { _id: 2, host: "localhost:27019" }
  ]
});

// Step 2: wait a few seconds for the first election
sleep(8000);

// Step 3: show each member and its state (PRIMARY / SECONDARY)
rs.status().members.forEach(m => print(m.name + "  ->  " + m.stateStr));

// Other useful helpers:
//   rs.conf()                     current configuration
//   rs.add("localhost:27020")     add a member
//   rs.remove("localhost:27020")  remove a member
//   rs.printSecondaryReplicationInfo()   how far behind secondaries are

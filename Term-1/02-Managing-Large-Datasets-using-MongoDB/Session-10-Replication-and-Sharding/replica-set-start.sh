#!/usr/bin/env bash
# replica-set-start.sh  (macOS / Linux)
# Starts 3 mongod servers in the background that form the replica set "rs0".

# Step 1: one data folder per member
mkdir -p ~/data/rs1 ~/data/rs2 ~/data/rs3

# Step 2: start the members (--fork runs in background, logs go to a file)
mongod --replSet rs0 --port 27017 --dbpath ~/data/rs1 --bind_ip localhost --fork --logpath ~/data/rs1.log
mongod --replSet rs0 --port 27018 --dbpath ~/data/rs2 --bind_ip localhost --fork --logpath ~/data/rs2.log
mongod --replSet rs0 --port 27019 --dbpath ~/data/rs3 --bind_ip localhost --fork --logpath ~/data/rs3.log

echo "Members started. Now run:  mongosh --port 27017 --file replica-set-init.js"

@echo off
REM sharding-start.bat  (Windows) - a tiny practice sharded cluster on one PC
REM 1 config server, 2 shards (each a 1-member replica set), 1 mongos router.

mkdir C:\data\cfg C:\data\shA C:\data\shB 2>nul

REM Config server replica set "cfgRS" on port 27030
start "config" mongod --configsvr --replSet cfgRS --port 27030 --dbpath C:\data\cfg --bind_ip localhost

REM Two shard replica sets
start "shardA" mongod --shardsvr --replSet shardA --port 27031 --dbpath C:\data\shA --bind_ip localhost
start "shardB" mongod --shardsvr --replSet shardB --port 27032 --dbpath C:\data\shB --bind_ip localhost

echo Wait 10 seconds, then initiate each replica set once:
echo   mongosh --port 27030 --eval "rs.initiate({_id:'cfgRS',configsvr:true,members:[{_id:0,host:'localhost:27030'}]})"
echo   mongosh --port 27031 --eval "rs.initiate({_id:'shardA',members:[{_id:0,host:'localhost:27031'}]})"
echo   mongosh --port 27032 --eval "rs.initiate({_id:'shardB',members:[{_id:0,host:'localhost:27032'}]})"
echo Then start the router:
echo   start "mongos" mongos --configdb cfgRS/localhost:27030 --port 27040 --bind_ip localhost
echo Finally:  mongosh --port 27040 --file sharding-setup.js

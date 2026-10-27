@echo off
REM replica-set-start.bat  (Windows)
REM Starts 3 mongod servers that form the replica set "rs0".
REM Each opens in its own window. Close a window to "crash" that member.

REM Step 1: one data folder per member
mkdir C:\data\rs1 C:\data\rs2 C:\data\rs3 2>nul

REM Step 2: start the members (same --replSet name, different port and folder)
start "rs0-27017" mongod --replSet rs0 --port 27017 --dbpath C:\data\rs1 --bind_ip localhost
start "rs0-27018" mongod --replSet rs0 --port 27018 --dbpath C:\data\rs2 --bind_ip localhost
start "rs0-27019" mongod --replSet rs0 --port 27019 --dbpath C:\data\rs3 --bind_ip localhost

echo Members started. Now run:  mongosh --port 27017 --file replica-set-init.js

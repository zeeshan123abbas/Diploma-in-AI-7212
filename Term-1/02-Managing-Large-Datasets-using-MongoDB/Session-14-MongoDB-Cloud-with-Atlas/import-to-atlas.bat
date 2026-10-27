@echo off
REM import-to-atlas.bat
REM Copies data from your local MongoDB to Atlas.
REM Replace <username>, <password> and cluster0.xxxxx with your values.
set ATLAS=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net

REM Option A: copy the WHOLE shopdb database (exact BSON copy)
mongodump --db shopdb --out dump
mongorestore --uri "%ATLAS%" --nsInclude "shopdb.*" dump

REM Option B: import ONE JSON file (e.g. products.json from Session 02)
mongoimport --uri "%ATLAS%/shopdb" --collection products_copy --jsonArray --file ..\Session-02-Working-with-MongoDB-Databases\products.json

echo Done. Check the collections in Atlas > Browse Collections or in Compass.

@echo off
REM export-from-atlas.bat
REM Takes data OUT of Atlas. Load the sample dataset in Atlas first for step 1.
set ATLAS=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net

REM 1. CSV of 2015 movies (for Excel or pandas)
mongoexport --uri "%ATLAS%/sample_mflix" --collection movies ^
  --query "{\"year\": 2015}" --fields title,year,imdb.rating ^
  --type=csv --out movies-2015.csv

REM 2. JSON array of all shopdb orders
mongoexport --uri "%ATLAS%/shopdb" --collection orders --jsonArray --out orders-from-atlas.json

REM 3. Full backup of shopdb (restore later with mongorestore)
mongodump --uri "%ATLAS%/shopdb" --out atlas-backup

echo Export finished.

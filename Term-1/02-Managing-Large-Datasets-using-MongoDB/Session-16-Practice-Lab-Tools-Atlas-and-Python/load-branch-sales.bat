@echo off
REM load-branch-sales.bat - EXTRACT step: load the CSV into salesdb.raw_sales
REM For Atlas, set the variable first:  set MONGODB_URI=mongodb+srv://<user>:<password>@cluster0.xxxxx.mongodb.net
REM If MONGODB_URI is not set, the local server is used.

if "%MONGODB_URI%"=="" set MONGODB_URI=mongodb://localhost:27017

REM --drop replaces the collection each time so the lab can be repeated
mongoimport --uri "%MONGODB_URI%" --db salesdb --collection raw_sales ^
  --type=csv --headerline --columnsHaveTypes --drop ^
  --file branch-sales.csv

echo Loaded. Open salesdb.raw_sales in Compass and look at the Schema tab.

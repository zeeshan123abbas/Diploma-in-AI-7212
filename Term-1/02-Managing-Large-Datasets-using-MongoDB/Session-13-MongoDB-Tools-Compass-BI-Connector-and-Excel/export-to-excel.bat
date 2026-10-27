@echo off
REM export-to-excel.bat  (Windows; on macOS/Linux replace ^ with \)
REM Needs MongoDB Database Tools and shopdb (Session 02).
REM Exports collections as CSV files that open directly in Excel.

REM 1. Orders: CSV needs an explicit list of fields
mongoexport --db shopdb --collection orders --type=csv ^
  --fields _id,customerId,city,total,status,payment ^
  --out orders.csv

REM 2. Products with a nested field (specs.brand becomes its own column)
mongoexport --db shopdb --collection products --type=csv ^
  --fields _id,name,category,price,stock,specs.brand ^
  --out products.csv

REM 3. Only delivered orders (a query filter in JSON)
mongoexport --db shopdb --collection orders --type=csv ^
  --fields _id,city,total --query "{\"status\": \"delivered\"}" ^
  --out delivered-orders.csv

echo Done. Open the .csv files in Excel.

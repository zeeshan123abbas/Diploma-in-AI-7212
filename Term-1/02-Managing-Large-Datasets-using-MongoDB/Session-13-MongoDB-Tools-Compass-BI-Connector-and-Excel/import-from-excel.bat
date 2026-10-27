@echo off
REM import-from-excel.bat  (Windows)
REM In Excel: File > Save As > "CSV UTF-8 (Comma delimited)". Then run this file.
REM The header row of new-products.csv contains types, e.g. price.int32()

mongoimport --db shopdb --collection products --type=csv ^
  --columnsHaveTypes --headerline ^
  --file new-products.csv

REM Without types every value would be imported as a string. Check the result:
mongosh shopdb --quiet --eval "printjson(db.products.find({ _id: /^P1/ }).toArray())"

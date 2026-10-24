-- Session 05: load a CSV file into a table with BULK INSERT
-- 1) Copy new-students.csv to a folder the SQL Server service can read, e.g. C:\SQLData\
-- 2) Change the path below if you used a different folder.
USE CampusDB;
GO

BULK INSERT Students
FROM 'C:\SQLData\new-students.csv'
WITH (
    FORMAT = 'CSV',          -- understands quoted values (SQL Server 2017+)
    FIRSTROW = 2,            -- skip the header line
    FIELDTERMINATOR = ',',   -- columns are separated by commas
    ROWTERMINATOR = '0x0a'   -- each row ends with a line feed
);

-- Check the new rows
SELECT * FROM Students WHERE StudentID >= 201;
GO

-- No access to the server's disk? Use SSMS instead:
-- right-click CampusDB > Tasks > Import Flat File... and pick the CSV.

-- Session 01: your first queries in SSMS
-- Run campusdb-setup.sql first.

-- Step 1: tell SQL Server which database to use
USE CampusDB;
GO

-- Step 2: show every row and column of the Students table
SELECT * FROM Students;

-- Step 3: show only two columns
SELECT FirstName, City FROM Students;

-- Step 4: show only students from Karachi
SELECT FirstName, LastName
FROM Students
WHERE City = 'Karachi';

-- Step 5: ask the server some questions about itself
SELECT @@VERSION     AS ServerVersion;   -- which SQL Server you are using
SELECT DB_NAME()     AS CurrentDatabase; -- which database is active
SELECT GETDATE()     AS ServerDateTime;  -- current date and time

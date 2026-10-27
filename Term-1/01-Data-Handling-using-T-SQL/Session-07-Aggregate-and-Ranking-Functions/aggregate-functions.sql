-- Session 07: aggregate functions on the whole table
USE CampusDB;
GO

-- 1. Basic summary of all marks
SELECT COUNT(*)          AS TotalRows,      -- every row (14)
       COUNT(Marks)      AS RowsWithMarks,  -- NULL marks are skipped (12)
       SUM(Marks)        AS TotalMarks,
       AVG(Marks * 1.0)  AS AverageMarks,   -- * 1.0 keeps the decimals
       MIN(Marks)        AS LowestMarks,
       MAX(Marks)        AS HighestMarks
FROM Enrollments;

-- 2. Total and average course fee
SELECT SUM(Fee) AS TotalFees,
       AVG(Fee) AS AverageFee
FROM Courses;

-- 3. COUNT(DISTINCT ...) counts different values only
SELECT COUNT(DISTINCT City) AS NumberOfCities
FROM Students;
GO

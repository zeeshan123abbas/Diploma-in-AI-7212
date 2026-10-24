-- Session 03: sorting with ORDER BY and limiting with TOP
USE CampusDB;
GO

-- Step 1: sort A to Z (ASC is the default)
SELECT FirstName, City FROM Students ORDER BY FirstName;

-- Step 2: sort highest fee first
SELECT CourseName, Fee FROM Courses ORDER BY Fee DESC;

-- Step 3: sort by two columns: city first, then name inside each city
SELECT City, FirstName FROM Students ORDER BY City ASC, FirstName ASC;

-- Step 4: TOP n gives the first n rows (use ORDER BY so "first" has meaning)
SELECT TOP (3) StudentID, Marks
FROM Enrollments
ORDER BY Marks DESC;           -- the three highest marks

-- Step 5: TOP with PERCENT
SELECT TOP (50) PERCENT CourseName, Fee
FROM Courses
ORDER BY Fee;

-- Step 6: WITH TIES also returns rows equal to the last one
SELECT TOP (1) WITH TIES CourseName, Fee
FROM Courses
ORDER BY Fee;                  -- two courses cost 15000, both returned

-- Step 7: OFFSET-FETCH for paging (skip 2 rows, then take 3)
SELECT StudentID, FirstName
FROM Students
ORDER BY StudentID
OFFSET 2 ROWS FETCH NEXT 3 ROWS ONLY;
GO

-- Session 03: filtering rows with WHERE
USE CampusDB;
GO

-- 1) Simple comparison
SELECT CourseName, Fee FROM Courses WHERE Fee > 15000;

-- 2) AND / OR / NOT
SELECT FirstName, City, DeptID
FROM Students
WHERE City = 'Karachi' OR City = 'Lahore';

SELECT FirstName, City
FROM Students
WHERE NOT City = 'Karachi';

-- 3) BETWEEN (both ends included)
SELECT StudentID, Marks FROM Enrollments WHERE Marks BETWEEN 70 AND 90;

-- 4) IN (a list of allowed values)
SELECT FirstName, City FROM Students WHERE City IN ('Lahore', 'Islamabad');

-- 5) LIKE with wildcards: % = any characters, _ = exactly one character
SELECT FirstName FROM Students WHERE FirstName LIKE 'A%';    -- starts with A
SELECT FirstName FROM Students WHERE FirstName LIKE '%a';    -- ends with a
SELECT FirstName FROM Students WHERE FirstName LIKE '_a%';   -- second letter is a

-- 6) IS NULL / IS NOT NULL (never use = NULL)
SELECT FirstName FROM Students WHERE Email IS NULL;
SELECT StudentID, CourseID FROM Enrollments WHERE Marks IS NOT NULL;

-- 7) IS [NOT] DISTINCT FROM (SQL Server 2022+) treats two NULLs as equal
DECLARE @WantedDept INT = NULL;
SELECT FirstName, DeptID
FROM Students
WHERE DeptID IS NOT DISTINCT FROM @WantedDept;   -- finds Fahad (DeptID is NULL)
GO

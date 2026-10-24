-- Session 04: combining query results with set operators
-- Rule: both queries must return the same number of columns with matching types.
USE CampusDB;
GO

-- Students who took course 1 (T-SQL)
SELECT StudentID FROM Enrollments WHERE CourseID = 1;   -- 101,102,103,105,108

-- Students who took course 4 (Python)
SELECT StudentID FROM Enrollments WHERE CourseID = 4;   -- 101,103,104,107

-- 1) UNION: in either list, duplicates removed
SELECT StudentID FROM Enrollments WHERE CourseID = 1
UNION
SELECT StudentID FROM Enrollments WHERE CourseID = 4;

-- 2) UNION ALL: in either list, duplicates kept (faster)
SELECT StudentID FROM Enrollments WHERE CourseID = 1
UNION ALL
SELECT StudentID FROM Enrollments WHERE CourseID = 4;

-- 3) INTERSECT: in BOTH lists (took T-SQL and Python)
SELECT StudentID FROM Enrollments WHERE CourseID = 1
INTERSECT
SELECT StudentID FROM Enrollments WHERE CourseID = 4;   -- 101, 103

-- 4) EXCEPT: in the first list but NOT the second
SELECT StudentID FROM Enrollments WHERE CourseID = 1
EXCEPT
SELECT StudentID FROM Enrollments WHERE CourseID = 4;   -- 102, 105, 108

-- ORDER BY goes once, at the very end
SELECT City FROM Students
UNION
SELECT DeptName FROM Departments
ORDER BY City;
GO

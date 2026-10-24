-- Session 04: the four kinds of joins
USE CampusDB;
GO

-- 1) INNER JOIN: only rows that match in BOTH tables
SELECT s.FirstName, c.CourseName, e.Marks
FROM Enrollments AS e
INNER JOIN Students AS s ON e.StudentID = s.StudentID
INNER JOIN Courses  AS c ON e.CourseID  = c.CourseID;

-- 2a) LEFT OUTER JOIN: every student, even with no enrollment
SELECT s.FirstName, e.CourseID
FROM Students AS s
LEFT JOIN Enrollments AS e ON s.StudentID = e.StudentID;   -- Fahad shows NULL

-- 2b) Use LEFT JOIN + IS NULL to find students with NO enrollment
SELECT s.FirstName
FROM Students AS s
LEFT JOIN Enrollments AS e ON s.StudentID = e.StudentID
WHERE e.EnrollmentID IS NULL;

-- 2c) RIGHT OUTER JOIN: every course, even with no students
SELECT c.CourseName, e.StudentID
FROM Enrollments AS e
RIGHT JOIN Courses AS c ON e.CourseID = c.CourseID;        -- Machine Learning shows NULL

-- 2d) FULL OUTER JOIN: every student AND every department
SELECT s.FirstName, d.DeptName
FROM Students AS s
FULL JOIN Departments AS d ON s.DeptID = d.DeptID;

-- 3) CROSS JOIN: every combination (3 departments x 5 courses = 15 rows)
SELECT d.DeptName, c.CourseName
FROM Departments AS d
CROSS JOIN Courses AS c;

-- 4) SELF JOIN: join a table to itself (faculty and their manager)
SELECT f.FullName  AS Teacher,
       m.FullName  AS Manager
FROM Faculty AS f
LEFT JOIN Faculty AS m ON f.ManagerID = m.FacultyID;
GO

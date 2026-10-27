-- Session 07: GROUP BY and HAVING
USE CampusDB;
GO

-- 1. Students per city
SELECT City, COUNT(*) AS TotalStudents
FROM Students
GROUP BY City                 -- one group per city
ORDER BY TotalStudents DESC;

-- 2. Only cities with at least 2 students
SELECT City, COUNT(*) AS TotalStudents
FROM Students
GROUP BY City
HAVING COUNT(*) >= 2;         -- HAVING filters groups

-- 3. Average marks per course, with the course name
SELECT c.CourseName,
       COUNT(e.Marks)                       AS StudentsWithMarks,
       ROUND(AVG(e.Marks * 1.0), 2)         AS AverageMarks
FROM Enrollments AS e
JOIN Courses     AS c ON c.CourseID = e.CourseID
WHERE e.Marks IS NOT NULL     -- WHERE filters rows BEFORE grouping
GROUP BY c.CourseName
ORDER BY AverageMarks DESC;
GO

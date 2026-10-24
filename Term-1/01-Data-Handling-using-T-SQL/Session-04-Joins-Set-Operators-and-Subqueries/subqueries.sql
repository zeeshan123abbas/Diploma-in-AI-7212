-- Session 04: subqueries (a query inside another query)
USE CampusDB;
GO

-- 1) Scalar subquery: returns ONE value
--    Courses that cost more than the average fee
SELECT CourseName, Fee
FROM Courses
WHERE Fee > (SELECT AVG(Fee) FROM Courses);

-- 2) Multi-value subquery with IN
--    Students who are enrolled in at least one course
SELECT FirstName
FROM Students
WHERE StudentID IN (SELECT StudentID FROM Enrollments);

-- 3) NOT IN: students who are NOT enrolled anywhere
SELECT FirstName
FROM Students
WHERE StudentID NOT IN (SELECT StudentID FROM Enrollments);

-- 4) Correlated subquery: the inner query uses a column of the outer query
--    For each enrollment, show the best mark in that same course
SELECT e.StudentID,
       e.CourseID,
       e.Marks,
       (SELECT MAX(e2.Marks)
        FROM Enrollments AS e2
        WHERE e2.CourseID = e.CourseID) AS BestInCourse
FROM Enrollments AS e;

-- 5) EXISTS: true if the subquery returns at least one row
--    Courses that have at least one student
SELECT c.CourseName
FROM Courses AS c
WHERE EXISTS (SELECT 1 FROM Enrollments AS e WHERE e.CourseID = c.CourseID);

-- 6) Subquery in FROM (derived table) - must have an alias
SELECT t.StudentID, t.AverageMarks
FROM (
    SELECT StudentID, AVG(Marks) AS AverageMarks
    FROM Enrollments
    GROUP BY StudentID
) AS t
WHERE t.AverageMarks > 75;
GO

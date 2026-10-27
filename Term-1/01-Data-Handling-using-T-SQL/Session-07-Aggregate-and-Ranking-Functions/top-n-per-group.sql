-- Session 07: the top student of each course (classic interview question)
USE CampusDB;
GO

-- Step 1: number the students inside each course, best first
WITH Ranked AS (
    SELECT CourseID,
           StudentID,
           Marks,
           ROW_NUMBER() OVER (PARTITION BY CourseID ORDER BY Marks DESC) AS Position
    FROM Enrollments
    WHERE Marks IS NOT NULL
)
-- Step 2: keep only position 1
SELECT r.CourseID, c.CourseName, r.StudentID, r.Marks
FROM Ranked  AS r
JOIN Courses AS c ON c.CourseID = r.CourseID
WHERE r.Position = 1;
GO

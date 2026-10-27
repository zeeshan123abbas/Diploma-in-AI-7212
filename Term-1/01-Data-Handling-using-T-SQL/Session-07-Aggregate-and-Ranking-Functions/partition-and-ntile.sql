-- Session 07: PARTITION BY and NTILE
USE CampusDB;
GO

-- 1. Rank students inside each course (numbering restarts per course)
SELECT CourseID,
       StudentID,
       Marks,
       RANK() OVER (PARTITION BY CourseID ORDER BY Marks DESC) AS RankInCourse
FROM Enrollments
WHERE Marks IS NOT NULL
ORDER BY CourseID, RankInCourse;

-- 2. Split all marks into 3 bands: 1 = top, 2 = middle, 3 = bottom
SELECT StudentID,
       Marks,
       NTILE(3) OVER (ORDER BY Marks DESC) AS Band
FROM Enrollments
WHERE Marks IS NOT NULL;
GO

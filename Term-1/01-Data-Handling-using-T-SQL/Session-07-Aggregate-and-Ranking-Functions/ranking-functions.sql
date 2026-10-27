-- Session 07: ROW_NUMBER, RANK and DENSE_RANK side by side
USE CampusDB;
GO

SELECT StudentID,
       CourseID,
       Marks,
       ROW_NUMBER() OVER (ORDER BY Marks DESC) AS RowNum,      -- always unique
       RANK()       OVER (ORDER BY Marks DESC) AS RankNo,      -- ties share, then gap
       DENSE_RANK() OVER (ORDER BY Marks DESC) AS DenseRankNo  -- ties share, no gap
FROM Enrollments
WHERE Marks IS NOT NULL       -- leave out exams not taken
ORDER BY Marks DESC;
GO

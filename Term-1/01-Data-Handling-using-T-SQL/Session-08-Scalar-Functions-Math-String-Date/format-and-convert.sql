-- Session 08: FORMAT, CAST, CONVERT, ISNULL and COALESCE
USE CampusDB;
GO

SELECT CourseName,
       FORMAT(Fee, 'N0') + ' PKR'                AS FeeText,        -- 15,000 PKR
       CONVERT(VARCHAR(10), GETDATE(), 103)      AS TodayDDMMYYYY,  -- style 103 = dd/mm/yyyy
       FORMAT(GETDATE(), 'dd-MMM-yyyy')          AS TodayNice,      -- 02-May-2026
       CAST(Credits AS VARCHAR(2)) + ' credits'  AS CreditText      -- number -> text
FROM Courses;

-- COALESCE returns the first value that is not NULL
SELECT FirstName,
       COALESCE(Email, City, 'unknown') AS ContactInfo
FROM Students;
GO

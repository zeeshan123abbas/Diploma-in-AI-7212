-- Session 08: date and time functions
USE CampusDB;
GO

-- 1. Today
SELECT GETDATE()                    AS NowDateTime,
       CAST(GETDATE() AS DATE)      AS TodayOnly;

-- 2. Break a date into parts and calculate with it
SELECT FirstName,
       EnrollDate,
       YEAR(EnrollDate)                         AS JoinYear,
       DATENAME(month, EnrollDate)              AS JoinMonth,        -- 'March'
       DATENAME(weekday, EnrollDate)            AS JoinWeekday,      -- 'Friday'
       DATEPART(quarter, EnrollDate)            AS JoinQuarter,      -- 1 to 4
       DATEDIFF(day, EnrollDate, GETDATE())     AS DaysSinceJoining,
       DATEADD(month, 6, EnrollDate)            AS ReviewDate,       -- 6 months later
       EOMONTH(EnrollDate)                      AS MonthEnd          -- last day of month
FROM Students;

-- 3. Students who joined in the last 120 days
SELECT FirstName, EnrollDate
FROM Students
WHERE EnrollDate >= DATEADD(day, -120, CAST(GETDATE() AS DATE));
GO

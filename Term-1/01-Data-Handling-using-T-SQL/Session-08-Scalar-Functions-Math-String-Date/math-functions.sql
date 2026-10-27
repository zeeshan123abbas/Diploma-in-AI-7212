-- Session 08: mathematical functions
USE CampusDB;
GO

-- 1. Try the functions on plain numbers first
SELECT ROUND(15499.567, 1) AS Rounded,     -- 15499.600
       CEILING(4.1)        AS RoundedUp,   -- 5
       FLOOR(4.9)          AS RoundedDown, -- 4
       ABS(-12)            AS Absolute,    -- 12
       POWER(2, 10)        AS TwoPower10,  -- 1024
       SQRT(81)            AS SquareRoot,  -- 9
       17 % 5              AS Remainder;   -- 2

-- 2. Use them on real data
SELECT CourseName,
       Fee,
       ROUND(Fee * 1.075, 0) AS FeeWithTax,     -- add 7.5% tax, no decimals
       CEILING(Fee / 3)      AS InstalmentOf3,  -- round up so 3 payments cover the fee
       FLOOR(Fee / 1000)     AS ThousandsOnly
FROM Courses;

-- 3. How many 3-seat lab groups do we need for 8 students?
SELECT CEILING(COUNT(*) / 3.0) AS GroupsNeeded  -- 3.0 avoids integer division
FROM Students;
GO

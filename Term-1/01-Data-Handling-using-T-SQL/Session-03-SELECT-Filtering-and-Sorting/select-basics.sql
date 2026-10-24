-- Session 03: the SELECT statement step by step
USE CampusDB;
GO

-- Step 1: all columns
SELECT * FROM Courses;

-- Step 2: specific columns (better practice than *)
SELECT CourseName, Fee FROM Courses;

-- Step 3: a calculated column (expression) with an alias
SELECT CourseName,
       Fee,
       Fee * 0.10 AS Discount,         -- 10 percent discount
       Fee - (Fee * 0.10) AS FinalFee
FROM Courses;

-- Step 4: three ways to write an alias
SELECT FirstName AS [First Name],     -- brackets allow spaces
       LastName  Surname,             -- AS is optional
       City      = City               -- alias = column style
FROM Students;

-- Step 5: handling NULLs (missing values)
SELECT FirstName,
       Email,
       ISNULL(Email, 'no email')               AS EmailOrText,
       COALESCE(Email, 'not provided')          AS EmailOrText2
FROM Students;

-- Step 6: remove duplicate rows with DISTINCT
SELECT City FROM Students;            -- Karachi appears 4 times
SELECT DISTINCT City FROM Students;   -- each city appears once
GO

-- Session 02: comments, batches, expressions and control of flow
USE CampusDB;   -- USE switches the current database
GO              -- GO ends a batch (a group of statements sent together)

/* This is a block comment.
   It can span many lines. */

-- Step 1: IF...ELSE decides what to run
DECLARE @Marks INT = 72;

IF @Marks >= 50
    PRINT 'Result: Pass';
ELSE
    PRINT 'Result: Fail';

-- Step 2: BEGIN...END groups several statements
IF @Marks >= 80
BEGIN
    PRINT 'Grade: A';
    PRINT 'Excellent work!';
END
ELSE
BEGIN
    PRINT 'Grade: below A';
    PRINT 'Keep practising.';
END

-- Step 3: WHILE repeats while a condition is true
DECLARE @Number INT = 1;
WHILE @Number <= 5
BEGIN
    PRINT 'Number is ' + CAST(@Number AS VARCHAR(2));
    SET @Number = @Number + 1;   -- never forget this, or the loop never ends
END

-- Step 4: CASE is an expression that returns a value per row
SELECT StudentID,
       Marks,
       CASE
           WHEN Marks >= 80 THEN 'A'
           WHEN Marks >= 65 THEN 'B'
           WHEN Marks >= 50 THEN 'C'
           WHEN Marks IS NULL THEN 'Not graded'
           ELSE 'F'
       END AS Grade
FROM Enrollments;
GO

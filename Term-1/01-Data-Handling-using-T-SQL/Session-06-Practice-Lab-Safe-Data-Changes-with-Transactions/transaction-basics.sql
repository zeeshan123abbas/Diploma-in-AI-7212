-- Session 06: COMMIT and ROLLBACK
-- Run campusdb-setup.sql (Session 01) first.
USE CampusDB;
GO

-- Part 1: make a mistake on purpose, then undo it
BEGIN TRANSACTION;
    UPDATE Courses SET Fee = 0;            -- no WHERE: every course fee becomes 0
    SELECT CourseName, Fee FROM Courses;   -- look: all fees are 0
ROLLBACK;                                  -- undo the whole transaction

SELECT CourseName, Fee FROM Courses;       -- fees are restored

-- Part 2: a correct change that we keep
BEGIN TRANSACTION;
    UPDATE Courses
    SET Fee = Fee + 1000                   -- add 1000 to the fee
    WHERE CourseID = 5;                    -- only Machine Learning Intro
COMMIT;                                    -- save it permanently

SELECT CourseName, Fee FROM Courses WHERE CourseID = 5;

-- Part 3: no transaction should be left open
SELECT @@TRANCOUNT AS OpenTransactions;    -- should be 0
GO

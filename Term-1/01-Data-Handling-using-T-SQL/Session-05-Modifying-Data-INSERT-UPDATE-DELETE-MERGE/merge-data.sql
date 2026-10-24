-- Session 05: MERGE = insert, update and delete in one statement
-- Scenario: the admissions office sends a new course price list.
USE CampusDB;
GO

-- Step 1: a staging table with the new list
CREATE TABLE CoursePriceList (
    CourseID   INT PRIMARY KEY,
    CourseName VARCHAR(60),
    Credits    INT,
    Fee        DECIMAL(10,2)
);

INSERT INTO CoursePriceList VALUES
(1, 'T-SQL Fundamentals',      3, 16000.00),   -- price changed
(2, 'MongoDB Basics',          3, 15000.00),   -- same
(6, 'Deep Learning Essentials',4, 30000.00);   -- brand new course

-- Step 2: MERGE the price list (source) into Courses (target)
MERGE Courses AS target
USING CoursePriceList AS source
    ON target.CourseID = source.CourseID
WHEN MATCHED AND target.Fee <> source.Fee THEN             -- exists, fee differs
    UPDATE SET target.Fee = source.Fee
WHEN NOT MATCHED BY TARGET THEN                            -- new course
    INSERT (CourseID, CourseName, Credits, Fee)
    VALUES (source.CourseID, source.CourseName, source.Credits, source.Fee)
OUTPUT $action AS ActionTaken,                             -- report what happened
       inserted.CourseID,
       inserted.Fee;                                       -- MERGE must end with ;

-- Step 3: check the result
SELECT * FROM Courses;

-- Step 4: tidy up
DROP TABLE CoursePriceList;
GO

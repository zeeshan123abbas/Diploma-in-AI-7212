-- Session 03: CONTAINS and FREETEXT (full-text search)
-- Requires the "Full-Text and Semantic Extractions for Search" feature
-- to be installed with SQL Server. Check with:
SELECT FULLTEXTSERVICEPROPERTY('IsFullTextInstalled') AS IsInstalled;  -- 1 = yes
GO

USE CampusDB;
GO

-- Step 1: create a full-text catalog (a container for full-text indexes)
CREATE FULLTEXT CATALOG CampusCatalog AS DEFAULT;

-- Step 2: index the CourseName column.
-- KEY INDEX must be a unique index; PK_Courses is the primary key from the setup script.
CREATE FULLTEXT INDEX ON Courses(CourseName)
    KEY INDEX PK_Courses
    WITH CHANGE_TRACKING AUTO;
GO

-- Wait a few seconds for the index to fill, then run:

-- Step 3: CONTAINS looks for exact words or prefixes
SELECT CourseName FROM Courses WHERE CONTAINS(CourseName, 'Python');
SELECT CourseName FROM Courses WHERE CONTAINS(CourseName, '"Statist*"');  -- prefix

-- Step 4: FREETEXT matches by meaning (word forms like learn / learning)
SELECT CourseName FROM Courses WHERE FREETEXT(CourseName, 'machine learn');
GO

-- Clean up (optional)
-- DROP FULLTEXT INDEX ON Courses;
-- DROP FULLTEXT CATALOG CampusCatalog;

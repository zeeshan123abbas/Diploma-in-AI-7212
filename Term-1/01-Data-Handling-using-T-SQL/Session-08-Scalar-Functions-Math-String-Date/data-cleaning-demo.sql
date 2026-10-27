-- Session 08: clean messy data with scalar functions
USE CampusDB;
GO

-- Step 1: a temporary table with messy data (# = temp table, removed when you disconnect)
CREATE TABLE #RawContacts (
    RawName  VARCHAR(50),
    RawPhone VARCHAR(20),
    RawDate  VARCHAR(10)          -- date stored as text dd/mm/yyyy
);

INSERT INTO #RawContacts VALUES
('   ayesha KHAN ', '0300-1234567', '15/01/2026'),
('BILAL ahmed',     '0321 7654321', '03/02/2026'),
(' sara  ',         '03331112222',  '28/02/2026');

-- Step 2: clean each column
SELECT
    -- name: trim spaces, first letter capital, rest lower case
    UPPER(LEFT(TRIM(RawName), 1)) + LOWER(SUBSTRING(TRIM(RawName), 2, 50)) AS CleanName,
    -- phone: remove dashes and spaces
    REPLACE(REPLACE(RawPhone, '-', ''), ' ', '')                            AS CleanPhone,
    -- date: convert text dd/mm/yyyy (style 103) into a real DATE
    CONVERT(DATE, RawDate, 103)                                             AS CleanDate
FROM #RawContacts;

-- Step 3: tidy up
DROP TABLE #RawContacts;
GO

-- Session 01: one small example of each T-SQL statement family
USE CampusDB;
GO

-- ---------- DDL: Data Definition Language (builds structure) ----------
-- Create a new table for clubs
CREATE TABLE Clubs (
    ClubID   INT         PRIMARY KEY,
    ClubName VARCHAR(40) NOT NULL
);

-- Add a new column to the table
ALTER TABLE Clubs ADD MeetingDay VARCHAR(10) NULL;
GO

-- ---------- DML: Data Manipulation Language (works with rows) ----------
-- Add two rows
INSERT INTO Clubs (ClubID, ClubName, MeetingDay) VALUES (1, 'AI Club', 'Monday');
INSERT INTO Clubs (ClubID, ClubName, MeetingDay) VALUES (2, 'Chess Club', 'Friday');

-- Change one row
UPDATE Clubs SET MeetingDay = 'Saturday' WHERE ClubID = 2;

-- Read the rows
SELECT * FROM Clubs;

-- Remove one row
DELETE FROM Clubs WHERE ClubID = 2;
GO

-- ---------- DCL: Data Control Language (who can do what) ----------
-- Create a login-free user just for this demo
CREATE USER DemoReader WITHOUT LOGIN;

-- Allow the user to read Clubs
GRANT SELECT ON Clubs TO DemoReader;

-- Take the permission back
REVOKE SELECT ON Clubs FROM DemoReader;
GO

-- ---------- Clean up ----------
DROP USER DemoReader;
DROP TABLE Clubs;   -- DDL again: removes the table completely
GO

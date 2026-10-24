-- =============================================================
-- CampusDB setup script (used in every session of this module)
-- Run the whole file in SSMS with F5. Safe to run again:
-- it drops the old database and builds a fresh copy.
-- =============================================================

USE master;
GO

-- Step 1: remove the old copy if it exists
IF DB_ID('CampusDB') IS NOT NULL
BEGIN
    ALTER DATABASE CampusDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE CampusDB;
END
GO

-- Step 2: create a new empty database
CREATE DATABASE CampusDB;
GO

USE CampusDB;
GO

-- Step 3: create the tables (DDL)
CREATE TABLE Departments (
    DeptID   INT          PRIMARY KEY,
    DeptName VARCHAR(50)  NOT NULL
);

CREATE TABLE Students (
    StudentID  INT          PRIMARY KEY,
    FirstName  VARCHAR(30)  NOT NULL,
    LastName   VARCHAR(30)  NOT NULL,
    Email      VARCHAR(80)  NULL,          -- some students have no email yet
    City       VARCHAR(30)  NOT NULL,
    DeptID     INT          NULL REFERENCES Departments(DeptID),
    EnrollDate DATE         NOT NULL
);

CREATE TABLE Courses (
    CourseID   INT           CONSTRAINT PK_Courses PRIMARY KEY,  -- named key (used for full-text search)
    CourseName VARCHAR(60)   NOT NULL,
    Credits    INT           NOT NULL,
    Fee        DECIMAL(10,2) NOT NULL
);

CREATE TABLE Enrollments (
    EnrollmentID INT  IDENTITY(1,1) PRIMARY KEY,   -- number is generated automatically
    StudentID    INT  NOT NULL REFERENCES Students(StudentID),
    CourseID     INT  NOT NULL REFERENCES Courses(CourseID),
    Marks        INT  NULL,                        -- NULL = exam not taken yet
    EnrolledOn   DATE NOT NULL
);

CREATE TABLE Faculty (
    FacultyID INT         PRIMARY KEY,
    FullName  VARCHAR(50) NOT NULL,
    ManagerID INT         NULL REFERENCES Faculty(FacultyID)  -- points to another faculty row
);
GO

-- Step 4: add sample rows (DML)
INSERT INTO Departments (DeptID, DeptName) VALUES
(1, 'Artificial Intelligence'),
(2, 'Data Science'),
(3, 'Software Engineering');

INSERT INTO Students (StudentID, FirstName, LastName, Email, City, DeptID, EnrollDate) VALUES
(101, 'Ayesha', 'Khan',    'ayesha@mail.com', 'Karachi',   1, '2026-01-10'),
(102, 'Bilal',  'Ahmed',   'bilal@mail.com',  'Lahore',    2, '2026-01-12'),
(103, 'Sara',   'Malik',   NULL,              'Karachi',   1, '2026-02-01'),
(104, 'Usman',  'Raza',    'usman@mail.com',  'Islamabad', 3, '2026-02-15'),
(105, 'Hina',   'Siddiqui','hina@mail.com',   'Karachi',   2, '2026-03-03'),
(106, 'Fahad',  'Ali',     NULL,              'Hyderabad', NULL, '2026-03-20'),
(107, 'Zara',   'Hussain', 'zara@mail.com',   'Lahore',    1, '2026-04-05'),
(108, 'Omar',   'Farooq',  'omar@mail.com',   'Karachi',   3, '2026-04-18');

INSERT INTO Courses (CourseID, CourseName, Credits, Fee) VALUES
(1, 'T-SQL Fundamentals',         3, 15000.00),
(2, 'MongoDB Basics',             3, 15000.00),
(3, 'Statistics for Data Science',4, 18000.00),
(4, 'Python Programming',         4, 20000.00),
(5, 'Machine Learning Intro',     4, 25000.00);

INSERT INTO Enrollments (StudentID, CourseID, Marks, EnrolledOn) VALUES
(101, 1, 85, '2026-01-15'), (101, 3, 78, '2026-02-01'), (101, 4, 92, '2026-03-01'),
(102, 1, 67, '2026-01-15'), (102, 2, 74, '2026-02-01'),
(103, 1, 90, '2026-02-05'), (103, 4, NULL, '2026-03-01'),
(104, 2, 55, '2026-02-20'), (104, 4, 61, '2026-03-01'),
(105, 3, 88, '2026-03-05'), (105, 1, 72, '2026-03-05'),
(107, 4, 95, '2026-04-10'), (107, 3, NULL, '2026-04-10'),
(108, 1, 49, '2026-04-20');
-- Student 106 has no enrollments and course 5 has no students (useful for outer joins)

INSERT INTO Faculty (FacultyID, FullName, ManagerID) VALUES
(1, 'Zeeshan Abbas', NULL),     -- head, no manager
(2, 'Nadia Iqbal',   1),
(3, 'Kamran Shah',   1),
(4, 'Rabia Noor',    2);
GO

-- Step 5: quick check
SELECT 'Students' AS TableName, COUNT(*) AS TotalRows FROM Students
UNION ALL SELECT 'Courses', COUNT(*) FROM Courses
UNION ALL SELECT 'Enrollments', COUNT(*) FROM Enrollments;
GO

-- Session 05: five ways to INSERT data
USE CampusDB;
GO

-- 1) One row, naming every column (best practice)
INSERT INTO Students (StudentID, FirstName, LastName, Email, City, DeptID, EnrollDate)
VALUES (109, 'Ali', 'Haider', 'ali@mail.com', 'Karachi', 1, '2026-05-02');

-- 2) Several rows in one statement
INSERT INTO Students (StudentID, FirstName, LastName, Email, City, DeptID, EnrollDate)
VALUES (110, 'Maham', 'Javed', NULL, 'Quetta', 2, '2026-05-03'),
       (111, 'Saad',  'Qureshi', 'saad@mail.com', 'Karachi', 3, '2026-05-04');

-- 3) Let IDENTITY create the ID automatically (do not list EnrollmentID)
INSERT INTO Enrollments (StudentID, CourseID, Marks, EnrolledOn)
VALUES (109, 5, NULL, '2026-05-10');

SELECT SCOPE_IDENTITY() AS NewEnrollmentID;   -- the ID just created

-- 4) INSERT ... SELECT: copy rows from a query into a table
CREATE TABLE KarachiStudents (
    StudentID INT PRIMARY KEY,
    FullName  VARCHAR(70)
);

INSERT INTO KarachiStudents (StudentID, FullName)
SELECT StudentID, FirstName + ' ' + LastName
FROM Students
WHERE City = 'Karachi';

SELECT * FROM KarachiStudents;

-- 5) SELECT ... INTO: create a NEW table and fill it in one step
SELECT CourseID, CourseName, Fee
INTO CourseBackup
FROM Courses;

SELECT * FROM CourseBackup;
GO

-- Session 05: UPDATE and DELETE
-- Golden rule: run the SELECT with the same WHERE first, check the rows, THEN update/delete.
USE CampusDB;
GO

-- ---------- UPDATE ----------
-- Step 1: preview the row
SELECT StudentID, Email FROM Students WHERE StudentID = 103;

-- Step 2: change one column of one row
UPDATE Students
SET Email = 'sara@mail.com'
WHERE StudentID = 103;

-- Step 3: change several columns at once
UPDATE Students
SET City = 'Karachi', DeptID = 2
WHERE StudentID = 106;

-- Step 4: update using a calculation (5% fee increase for 4-credit courses)
UPDATE Courses
SET Fee = Fee * 1.05
WHERE Credits = 4;

-- Step 5: update using data from another table (join)
--         give 5 bonus marks to every Karachi student in course 1
UPDATE e
SET e.Marks = e.Marks + 5
FROM Enrollments AS e
INNER JOIN Students AS s ON e.StudentID = s.StudentID
WHERE s.City = 'Karachi' AND e.CourseID = 1;

-- ---------- DELETE ----------
-- Step 6: delete one row
DELETE FROM KarachiStudents WHERE StudentID = 101;

-- Step 7: delete rows that match a condition
DELETE FROM CourseBackup WHERE Fee < 16000;

-- Step 8: remove ALL rows quickly but keep the table
TRUNCATE TABLE CourseBackup;

-- Step 9: remove the practice tables completely
DROP TABLE CourseBackup;
DROP TABLE KarachiStudents;
GO

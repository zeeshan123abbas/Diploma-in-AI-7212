-- Session 06: model answers for the Lab Practice tasks
-- Try the tasks yourself before opening this file.
USE CampusDB;
GO

-- Task 1: delete, look, roll back
BEGIN TRAN;
    DELETE FROM Enrollments WHERE StudentID = 108;
    SELECT * FROM Enrollments WHERE StudentID = 108;   -- no rows now
ROLLBACK;
SELECT * FROM Enrollments WHERE StudentID = 108;       -- rows are back
GO

-- Task 2: fill missing emails for Lahore students, commit only if 0 or 1 rows
DECLARE @rows INT;
BEGIN TRAN;
    UPDATE Students
    SET Email = LOWER(FirstName) + '@campus.pk'
    WHERE City = 'Lahore' AND Email IS NULL;
    SET @rows = @@ROWCOUNT;
IF @rows <= 1 COMMIT; ELSE ROLLBACK;
PRINT 'Rows changed: ' + CAST(@rows AS VARCHAR(10));
GO

-- Task 3: duplicate primary key inside TRY...CATCH
BEGIN TRY
    INSERT INTO Courses (CourseID, CourseName, Credits, Fee)
    VALUES (1, 'Duplicate Course', 3, 1000);
END TRY
BEGIN CATCH
    PRINT 'Error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)) + ': ' + ERROR_MESSAGE();
END CATCH;
GO

-- Task 4: +10% fee for 4-credit courses, show old and new
BEGIN TRAN;
    UPDATE Courses
    SET Fee = Fee * 1.10
    OUTPUT inserted.CourseName, deleted.Fee AS OldFee, inserted.Fee AS NewFee
    WHERE Credits = 4;
COMMIT;
GO

-- Task 5: nothing left open
SELECT @@TRANCOUNT AS OpenTransactions;
GO

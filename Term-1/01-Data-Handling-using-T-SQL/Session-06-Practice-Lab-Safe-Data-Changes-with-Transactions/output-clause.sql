-- Session 06: OUTPUT shows the rows before and after a change
USE CampusDB;
GO

BEGIN TRAN;
    UPDATE Enrollments
    SET Marks = Marks + 5                  -- 5 grace marks
    OUTPUT deleted.EnrollmentID,           -- deleted  = row BEFORE the update
           deleted.Marks  AS OldMarks,
           inserted.Marks AS NewMarks      -- inserted = row AFTER the update
    WHERE Marks < 60;                      -- only students below 60
COMMIT;
GO

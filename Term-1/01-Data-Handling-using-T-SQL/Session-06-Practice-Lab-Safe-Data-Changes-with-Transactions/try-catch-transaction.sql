-- Session 06: TRY...CATCH with a transaction (all or nothing)
USE CampusDB;
GO

BEGIN TRY
    BEGIN TRAN;

        -- Insert 1: valid (student 106 and course 5 both exist)
        INSERT INTO Enrollments (StudentID, CourseID, Marks, EnrolledOn)
        VALUES (106, 5, NULL, '2026-05-01');

        -- Insert 2: invalid (student 999 does not exist -> foreign key error)
        INSERT INTO Enrollments (StudentID, CourseID, Marks, EnrolledOn)
        VALUES (999, 5, NULL, '2026-05-01');

    COMMIT;                                -- never reached in this example
    PRINT 'Both rows saved.';
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK;                          -- undo insert 1 as well

    PRINT 'Error number : ' + CAST(ERROR_NUMBER() AS VARCHAR(10));
    PRINT 'Error message: ' + ERROR_MESSAGE();
END CATCH;
GO

-- Prove nothing was saved for student 106
SELECT * FROM Enrollments WHERE StudentID = 106;
GO

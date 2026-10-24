-- Session 02: handling errors and using a transaction
USE CampusDB;
GO

-- Step 1: TRY...CATCH catches an error instead of stopping the script
BEGIN TRY
    SELECT 10 / 0 AS Answer;          -- divide by zero causes an error
END TRY
BEGIN CATCH
    PRINT 'Something went wrong:';
    PRINT ERROR_MESSAGE();            -- the error text
    PRINT 'Error number: ' + CAST(ERROR_NUMBER() AS VARCHAR(10));
END CATCH;
GO

-- Step 2: a transaction = all statements succeed, or none of them do
BEGIN TRY
    BEGIN TRANSACTION;

        -- raise every course fee by 1000
        UPDATE Courses SET Fee = Fee + 1000;

        -- this insert fails: CourseID 1 already exists (duplicate key)
        INSERT INTO Courses (CourseID, CourseName, Credits, Fee)
        VALUES (1, 'Duplicate Course', 3, 1000);

    COMMIT TRANSACTION;               -- only reached if no error
    PRINT 'Changes saved.';
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;             -- undo the fee increase too
    PRINT 'Error, all changes undone: ' + ERROR_MESSAGE();
END CATCH;
GO

-- Step 3: prove that the fees did NOT change
SELECT CourseID, Fee FROM Courses;
GO

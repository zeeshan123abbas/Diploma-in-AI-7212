-- Session 06: use @@ROWCOUNT to decide COMMIT or ROLLBACK
USE CampusDB;
GO

DECLARE @rows INT;                         -- variable to hold the row count

BEGIN TRAN;
    UPDATE Students
    SET City = 'Karachi'
    WHERE StudentID = 106;                 -- we expect exactly 1 row

    SET @rows = @@ROWCOUNT;                -- read it immediately

IF @rows = 1
BEGIN
    COMMIT;
    PRINT 'Saved: 1 row changed.';
END
ELSE
BEGIN
    ROLLBACK;
    PRINT 'Undone: unexpected number of rows.';
END
GO

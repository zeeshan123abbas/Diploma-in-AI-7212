-- Session 02: data types and variables
USE CampusDB;
GO

-- Step 1: declare variables, each with a data type
DECLARE @StudentName VARCHAR(50)   = 'Ayesha Khan';   -- text
DECLARE @Age         INT           = 21;              -- whole number
DECLARE @Fee         DECIMAL(10,2) = 15000.50;        -- money with 2 decimals
DECLARE @JoinDate    DATE          = '2026-01-10';    -- date only
DECLARE @IsActive    BIT           = 1;               -- 1 = true, 0 = false

-- Step 2: show the values
SELECT @StudentName AS StudentName,
       @Age         AS Age,
       @Fee         AS Fee,
       @JoinDate    AS JoinDate,
       @IsActive    AS IsActive;

-- Step 3: change a variable with SET
SET @Age = @Age + 1;
PRINT 'Next year the age will be ' + CAST(@Age AS VARCHAR(5));

-- Step 4: VARCHAR vs NVARCHAR (N = Unicode, needed for Urdu text)
DECLARE @CityEnglish VARCHAR(20)  = 'Karachi';
DECLARE @CityUrdu    NVARCHAR(20) = N'کراچی';
SELECT @CityEnglish AS English, @CityUrdu AS Urdu;

-- Step 5: put a value from a table into a variable
DECLARE @TotalStudents INT;
SELECT @TotalStudents = COUNT(*) FROM Students;
PRINT 'Total students: ' + CAST(@TotalStudents AS VARCHAR(5));
GO

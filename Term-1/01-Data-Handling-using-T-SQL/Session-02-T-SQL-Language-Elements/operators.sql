-- Session 02: the six kinds of operators
USE CampusDB;
GO

-- 1) Arithmetic: + - * / %
SELECT 10 + 3 AS AddResult,
       10 - 3 AS SubtractResult,
       10 * 3 AS MultiplyResult,
       10 / 3 AS IntegerDivide,     -- 3 (both are whole numbers)
       10.0 / 3 AS DecimalDivide,   -- 3.333333
       10 % 3 AS Remainder;         -- 1

-- 2) Comparison: = <> > < >= <=
SELECT CourseName, Fee
FROM Courses
WHERE Fee >= 20000;

-- 3) Logical: AND, OR, NOT
SELECT FirstName, City, DeptID
FROM Students
WHERE City = 'Karachi' AND DeptID = 1;

-- 4) String concatenation: + joins text
SELECT FirstName + ' ' + LastName AS FullName
FROM Students;

-- 5) Compound assignment: += -= *= /=
DECLARE @Counter INT = 10;
SET @Counter += 5;    -- same as @Counter = @Counter + 5
SET @Counter *= 2;    -- same as @Counter = @Counter * 2
SELECT @Counter AS CounterValue;   -- 30

-- 6) Bitwise: & (AND), | (OR), ^ (XOR) on the bits of numbers
-- 6 = 110 in binary, 3 = 011 in binary
SELECT 6 & 3 AS BitAnd,   -- 010 = 2
       6 | 3 AS BitOr,    -- 111 = 7
       6 ^ 3 AS BitXor;   -- 101 = 5
GO

-- Session 08: string functions
USE CampusDB;
GO

SELECT FirstName,
       LastName,
       CONCAT(FirstName, ' ', UPPER(LastName))   AS FullName,     -- join text
       LEN(FirstName)                            AS NameLength,   -- number of characters
       LEFT(FirstName, 1) + LEFT(LastName, 1)    AS Initials,     -- first letters
       ISNULL(Email, 'not provided')             AS EmailShown,   -- fill missing email
       CHARINDEX('@', Email)                     AS AtPosition,   -- where is the @ ?
       SUBSTRING(Email, CHARINDEX('@', Email) + 1, 50) AS EmailDomain, -- text after @
       REPLACE(City, 'Karachi', 'KHI')           AS CityShort     -- swap text
FROM Students;

-- TRIM removes spaces at both ends
SELECT '[' + TRIM('   Aptech   ') + ']' AS Trimmed;               -- [Aptech]
GO

# Module 01: Data Handling using T-SQL

![SQL Server](https://img.shields.io/badge/SQL_Server-2022-CC2927?logo=microsoftsqlserver&logoColor=white) ![T-SQL](https://img.shields.io/badge/Language-T--SQL-0078D4) ![SSMS](https://img.shields.io/badge/Tool-SSMS_20+-5C2D91) ![Level](https://img.shields.io/badge/Level-Beginner-2EA44F)

> Diploma in AI / Data Science · Term 1 · 8 sessions × 2 hours · [⬅ Term Home](../README.md)

Almost every AI or data science project starts with data that lives in a relational database. This module teaches you to talk to Microsoft SQL Server using **Transact-SQL (T-SQL)**: you will create tables, read data with `SELECT`, combine tables with joins, change data safely and summarise it with built-in functions. All examples use one small practice database, **CampusDB** (students, courses, enrollments and faculty), so you can focus on the SQL and not on the data.

## 🎯 What You Will Learn

- Explain what a relational database is and where SQL Server fits
- Use SQL Server Management Studio (SSMS) to connect, browse objects and run queries
- Recognise the parts of T-SQL: DDL, DML and DCL, data types, operators and control of flow
- Read data with `SELECT`, filter with `WHERE`, sort with `ORDER BY` and limit with `TOP`
- Combine data from several tables using joins, set operators and subqueries
- Insert, update, delete and merge data, and protect changes with transactions
- Summarise data with aggregate, ranking, math, string and date functions

## 📋 Prerequisites

- Comfortable using a Windows computer and installing software
- Basic idea of a table (rows and columns), for example an Excel sheet
- No previous programming is required

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|---|---|---|
| SQL Server 2022 Developer or Express | the free database engine | [https://www.microsoft.com/en-us/sql-server/sql-server-downloads](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) |
| SQL Server Management Studio (SSMS) | write and run queries, manage databases | [https://learn.microsoft.com/en-us/ssms/install/install](https://learn.microsoft.com/en-us/ssms/install/install) |
| VS Code + MSSQL extension (optional) | lightweight editor, works on macOS/Linux too | [https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code) |

> 💡 **First step for every student:** open [`campusdb-setup.sql`](./Session-01-Introduction-to-T-SQL-and-SSMS/campusdb-setup.sql) in SSMS and press **F5**. It creates the CampusDB practice database used in all eight sessions. Run it again any time you want a fresh copy.

## 📚 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to T-SQL and SSMS | [Open notes](./Session-01-Introduction-to-T-SQL-and-SSMS/README.md) |
| 02 | T-SQL Language Elements | [Open notes](./Session-02-T-SQL-Language-Elements/README.md) |
| 03 | SELECT: Filtering and Sorting Data | [Open notes](./Session-03-SELECT-Filtering-and-Sorting/README.md) |
| 04 | Joins, Set Operators and Subqueries | [Open notes](./Session-04-Joins-Set-Operators-and-Subqueries/README.md) |
| 05 | Modifying Data: INSERT, UPDATE, DELETE, MERGE | [Open notes](./Session-05-Modifying-Data-INSERT-UPDATE-DELETE-MERGE/README.md) |
| 06 | Practice Lab: Safe Data Changes with Transactions | [Open notes](./Session-06-Practice-Lab-Safe-Data-Changes-with-Transactions/README.md) |
| 07 | Aggregate and Ranking Functions | [Open notes](./Session-07-Aggregate-and-Ranking-Functions/README.md) |
| 08 | Scalar Functions: Math, String and Date | [Open notes](./Session-08-Scalar-Functions-Math-String-Date/README.md) |

## 🚀 Module Mini-Project

**Library Management Database** - design and query a small library system:

1. Create a `LibraryDB` database with tables `Members`, `Books`, `Authors` and `Loans` (primary and foreign keys).
2. Insert at least 10 members, 20 books and 30 loan records.
3. Write queries for: books currently on loan, overdue loans (`DATEDIFF`), the top 5 most borrowed books (`TOP` + `GROUP BY`), and members who have never borrowed (`LEFT JOIN ... IS NULL`).
4. Rank members by number of loans using `DENSE_RANK()`.
5. Write a `MERGE` script that updates book stock from a `NewStock` table.
6. Wrap a "return a book" operation in a transaction with `TRY...CATCH`.
7. Submit one `.sql` file per task plus a short README with screenshots of your results.

## 🔗 Resources (official documentation)

- [Transact-SQL reference](https://learn.microsoft.com/en-us/sql/t-sql/language-reference)
- [SELECT statement](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql)
- [Joins in SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins)
- [Built-in functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions)
- [SSMS documentation](https://learn.microsoft.com/en-us/ssms/)

---

[⬅ Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad

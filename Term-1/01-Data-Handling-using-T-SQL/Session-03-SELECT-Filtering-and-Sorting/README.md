# Session 03: SELECT: Filtering and Sorting Data

> Module: Data Handling using T-SQL · Diploma in AI / Data Science · Term 1 · ⏱ ~2 hours

`SELECT` is the statement you will write more than any other. A data scientist uses it every day to pull exactly the rows and columns a model or report needs. In this session you will learn to choose columns, create calculated columns, deal with missing values, remove duplicates, filter, sort and limit results.

## 🎯 Learning Objectives

- Describe the elements of a `SELECT` statement and the order in which SQL Server processes them
- Select all columns, specific columns and calculated expressions with aliases
- Handle `NULL` values with `IS NULL`, `ISNULL` and `COALESCE`
- Remove duplicates with `DISTINCT` and sort results with `ORDER BY`
- Filter rows using comparison and logical operators, `BETWEEN`, `IN`, `LIKE`, `IS [NOT] DISTINCT FROM`, `CONTAINS` and `FREETEXT`
- Limit results with `TOP` and `OFFSET-FETCH`

## 📖 Concepts Explained

### 1. Elements of SELECT

```sql
SELECT   column list          -- 5. what to show
FROM     table                -- 1. where the data comes from
WHERE    row filter           -- 2. which rows to keep
GROUP BY grouping columns     -- 3. (Session 07)
HAVING   group filter         -- 4. (Session 07)
ORDER BY sort columns;        -- 6. how to sort
```

You **write** `SELECT` first, but SQL Server **processes** `FROM` first. That is why a column alias created in `SELECT` can be used in `ORDER BY` but not in `WHERE`.

```mermaid
flowchart LR
  F[FROM] --> W[WHERE] --> G[GROUP BY] --> H[HAVING] --> S[SELECT] --> O[ORDER BY]
```

### 2. Choosing columns

| Need | Write |
|---|---|
| Every column | `SELECT * FROM Courses` (fine for exploring, avoid in real apps) |
| Specific columns | `SELECT CourseName, Fee FROM Courses` |
| A calculation | `SELECT Fee * 0.10 AS Discount FROM Courses` |
| A friendly heading | `AS [Course Name]` (square brackets allow spaces) |

### 3. NULL means "unknown"

`NULL` is not zero and not an empty string; it means the value is missing. Any comparison with `NULL` using `=` returns *unknown*, so `WHERE Email = NULL` never finds anything.

| Task | Correct way |
|---|---|
| Find missing values | `WHERE Email IS NULL` |
| Find present values | `WHERE Email IS NOT NULL` |
| Replace with a default | `ISNULL(Email, 'no email')` or `COALESCE(Email, Phone, 'none')` |
| Compare where NULL = NULL should be true | `a IS NOT DISTINCT FROM b` (SQL Server 2022+) |

`COALESCE` is standard SQL and accepts many arguments, returning the first non-NULL one.

### 4. DISTINCT

`DISTINCT` removes duplicate rows from the result. `SELECT DISTINCT City FROM Students` lists each city once. It looks at the whole row, so `SELECT DISTINCT City, DeptID` removes only rows where *both* values repeat.

### 5. Filtering with WHERE

| Operator | Meaning | Example |
|---|---|---|
| `=`, `<>`, `>`, `<` | compare | `Fee > 15000` |
| `AND`, `OR`, `NOT` | combine conditions | `City = 'Karachi' AND DeptID = 1` |
| `BETWEEN a AND b` | range, both ends included | `Marks BETWEEN 70 AND 90` |
| `IN (...)` | matches any value in a list | `City IN ('Lahore','Islamabad')` |
| `LIKE` | pattern: `%` any text, `_` one character | `FirstName LIKE 'A%'` |

> **Precedence trap:** `NOT` runs first, then `AND`, then `OR`. Use brackets to make your meaning clear: `WHERE (City = 'Karachi' OR City = 'Lahore') AND DeptID = 1`.

### 6. CONTAINS and FREETEXT

These search inside text using a **full-text index** (an optional SQL Server feature). `CONTAINS` finds exact words or prefixes (`'"Statist*"'`). `FREETEXT` is looser: it matches different forms of a word, so `'learn'` also finds *Learning*. `LIKE '%word%'` works without an index but becomes slow on large tables.

### 7. Sorting and limiting

- `ORDER BY col` sorts ascending (A-Z, 0-9); add `DESC` for descending.
- `TOP (n)` returns only the first n rows; `TOP (n) PERCENT` returns a percentage; `WITH TIES` adds rows that tie with the last one.
- `OFFSET x ROWS FETCH NEXT y ROWS ONLY` skips x rows and returns y rows: ideal for page 1, page 2... in apps.

### 8. Formatting your queries

Write keywords in CAPITALS, put each clause on a new line, indent column lists and end statements with `;`. Readable SQL is easier to debug and review.

## 💻 Code Examples

### Example 1: Columns, aliases, NULLs and DISTINCT (`select-basics.sql`)

```sql
SELECT CourseName,
       Fee,
       Fee * 0.10        AS Discount,
       Fee - (Fee * 0.10) AS FinalFee
FROM Courses;

SELECT FirstName, ISNULL(Email, 'no email') AS EmailOrText
FROM Students;

SELECT DISTINCT City FROM Students;
```

**How it works:** the first query adds two calculated columns with aliases. The second replaces missing emails with text. The third lists each city once.

### Example 2: Filtering (`filtering.sql`)

```sql
SELECT StudentID, Marks FROM Enrollments WHERE Marks BETWEEN 70 AND 90;
SELECT FirstName FROM Students WHERE FirstName LIKE 'A%';
SELECT FirstName FROM Students WHERE Email IS NULL;
```

**How it works:** a range filter, a pattern filter (names starting with A) and a missing-value filter. The file also covers `IN`, `NOT` and `IS NOT DISTINCT FROM`.

### Example 3: Sorting and TOP (`sorting-and-top.sql`)

```sql
SELECT TOP (3) StudentID, Marks
FROM Enrollments
ORDER BY Marks DESC;

SELECT StudentID, FirstName
FROM Students
ORDER BY StudentID
OFFSET 2 ROWS FETCH NEXT 3 ROWS ONLY;
```

**How it works:** the first query returns the three best marks. The second skips two students and returns the next three, which is how a website shows "page 2".

### Example 4: Full-text search (`full-text-search.sql`)

```sql
CREATE FULLTEXT CATALOG CampusCatalog AS DEFAULT;
CREATE FULLTEXT INDEX ON Courses(CourseName) KEY INDEX PK_Courses;
SELECT CourseName FROM Courses WHERE CONTAINS(CourseName, 'Python');
SELECT CourseName FROM Courses WHERE FREETEXT(CourseName, 'machine learn');
```

**How it works:** a catalog and a full-text index are created once; then `CONTAINS` and `FREETEXT` can search the indexed column. Skip this file if Full-Text Search is not installed.

## 🧪 Lab Practice

1. Show `CourseName`, `Fee` and a column `FeeWithTax` (fee + 16%) for every course.
2. List students whose first name contains the letter `r`, sorted by `LastName`.
3. Show enrollments that have no marks yet, replacing `NULL` with `'Pending'` (hint: `CAST` the marks to `VARCHAR` inside `ISNULL`).
4. Show the two cheapest courses using `TOP ... WITH TIES`.
5. List distinct `DeptID` values from `Students`. Which value represents "no department"?

## 📝 Assignment

Write one query that answers: *"Which students from Karachi or Lahore joined in 2026 between February and April? Show full name as one column, city and join date, newest first."* Save it as `assignment-03.sql` with a comment explaining each clause.

## ❓ Quick Quiz

1. Which clause does SQL Server process first?
2. Why does `WHERE Email = NULL` return no rows?
3. What does `_` mean in a `LIKE` pattern?
4. What is the difference between `TOP (5)` and `TOP (5) WITH TIES`?
5. Which function returns the first non-NULL value from a list?

<details>
<summary>Show answers</summary>

1. `FROM`
2. Comparing with `NULL` using `=` gives *unknown*, never true. Use `IS NULL`.
3. Exactly one character.
4. `WITH TIES` also returns extra rows that have the same `ORDER BY` value as the 5th row.
5. `COALESCE`

</details>

## 💼 Interview Questions

**1. Why should you avoid `SELECT *` in production code?**

> It returns columns you may not need (slower, more network traffic) and can break code when the table structure changes.

**2. What is the difference between `ISNULL` and `COALESCE`?**

> `ISNULL` is T-SQL only and takes two arguments. `COALESCE` is ANSI standard, takes many arguments and returns the first non-NULL.

**3. Can you use a column alias in the WHERE clause? Why?**

> No. `WHERE` is processed before `SELECT`, so the alias does not exist yet. Repeat the expression or use a subquery/CTE.

## ✅ Summary

- `SELECT` chooses columns; `FROM` picks the table; `WHERE` filters; `ORDER BY` sorts.
- Aliases give friendly names; expressions create calculated columns.
- Handle `NULL` with `IS NULL`, `ISNULL`, `COALESCE` and `IS [NOT] DISTINCT FROM`.
- `DISTINCT` removes duplicates; `TOP` and `OFFSET-FETCH` limit results.
- `CONTAINS`/`FREETEXT` provide fast text search with a full-text index.

---

[⬅ Previous](../Session-02-T-SQL-Language-Elements/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-04-Joins-Set-Operators-and-Subqueries/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad

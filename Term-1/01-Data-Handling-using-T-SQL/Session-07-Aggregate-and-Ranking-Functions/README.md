# Session 07: Aggregate and Ranking Functions

> Module: Data Handling using T-SQL · Diploma in AI / Data Science · Term 1 · ⏱ ~2 hours

A manager rarely asks for "all 10,000 rows". They ask *"How many students per city?"*, *"What is the average mark in each course?"* or *"Who are the top 3 students?"*. In this session you will answer these questions with **built-in functions**: aggregate functions that turn many rows into one number, and ranking functions that give every row a position.

## 🎯 Learning Objectives

- Describe the three families of built-in functions: aggregate, ranking and scalar
- Summarise data with `COUNT`, `SUM`, `AVG`, `MIN` and `MAX`
- Group rows with `GROUP BY` and filter groups with `HAVING`
- Explain how aggregate functions treat `NULL` values
- Number and rank rows with `ROW_NUMBER`, `RANK`, `DENSE_RANK` and `NTILE`
- Restart numbering per group with `PARTITION BY`

## 📖 Concepts Explained

### 1. What is a built-in function?

A function takes input, does a job and returns a result. SQL Server ships with hundreds of them, so you do not need to write your own for common tasks.

| Family | Works on | Returns | Examples |
|---|---|---|---|
| Aggregate | a group of rows | one value per group | `COUNT`, `AVG` |
| Ranking | each row inside a window | a position number | `RANK`, `ROW_NUMBER` |
| Scalar | one value at a time | one value per row | `UPPER`, `ROUND`, `GETDATE` (Session 08) |

### 2. Aggregate functions

| Function | Meaning | NULL handling |
|---|---|---|
| `COUNT(*)` | number of rows | counts every row |
| `COUNT(column)` | number of non-NULL values | ignores NULL |
| `SUM(column)` | total | ignores NULL |
| `AVG(column)` | average | ignores NULL (NULL is *not* 0) |
| `MIN` / `MAX` | smallest / largest | ignores NULL |

> **Watch out:** `AVG` on an `INT` column returns an `INT` (decimals are cut). Write `AVG(Marks * 1.0)` or `AVG(CAST(Marks AS DECIMAL(5,2)))` to keep decimals.

### 3. GROUP BY and HAVING

`GROUP BY` puts rows into buckets and the aggregate runs once per bucket.

> **Analogy:** a teacher sorts answer sheets into piles by class, then counts each pile. The piles are `GROUP BY`; counting is `COUNT(*)`.

Rules to remember:

- Every column in `SELECT` must be either inside an aggregate or listed in `GROUP BY`.
- `WHERE` filters **rows** before grouping; `HAVING` filters **groups** after grouping.

```mermaid
flowchart LR
  A[FROM] --> B[WHERE: filter rows] --> C[GROUP BY: make piles] --> D[HAVING: filter piles] --> E[SELECT] --> F[ORDER BY]
```

### 4. Ranking functions

Ranking functions use the `OVER (...)` clause, which says *how* to order rows (and optionally *where to restart*).

```sql
RANK() OVER (PARTITION BY CourseID ORDER BY Marks DESC)
```

Suppose marks are 95, 90, 90, 85:

| Marks | ROW_NUMBER | RANK | DENSE_RANK |
|---|---|---|---|
| 95 | 1 | 1 | 1 |
| 90 | 2 | 2 | 2 |
| 90 | 3 | 2 | 2 |
| 85 | 4 | **4** | **3** |

- `ROW_NUMBER` always gives unique numbers, even for ties.
- `RANK` gives ties the same rank and then **skips** numbers (like a sports table).
- `DENSE_RANK` gives ties the same rank with **no gaps**.
- `NTILE(n)` splits rows into `n` roughly equal groups (for example top/middle/bottom thirds).
- `PARTITION BY` restarts the numbering for each group, like a separate merit list per course.

## 💻 Code Examples

Run `campusdb-setup.sql` (Session 01) first.

### Example 1: basic aggregates (`aggregate-functions.sql`)

```sql
SELECT COUNT(*)            AS TotalRows,
       COUNT(Marks)        AS RowsWithMarks,   -- NULL marks not counted
       AVG(Marks * 1.0)    AS AverageMarks,
       MIN(Marks)          AS LowestMarks,
       MAX(Marks)          AS HighestMarks
FROM Enrollments;
```

**How it works:** the whole table is one group, so you get one row. `COUNT(*)` is 14 but `COUNT(Marks)` is 12 because two marks are `NULL`.

### Example 2: GROUP BY and HAVING (`group-by-having.sql`)

```sql
SELECT City, COUNT(*) AS TotalStudents
FROM Students
GROUP BY City
HAVING COUNT(*) >= 2          -- only cities with 2 or more students
ORDER BY TotalStudents DESC;
```

**How it works:** students are put into one pile per city, each pile is counted, and `HAVING` drops cities with a single student.

### Example 3: merit list with ranks (`ranking-functions.sql`)

```sql
SELECT StudentID, Marks,
       ROW_NUMBER() OVER (ORDER BY Marks DESC) AS RowNum,
       RANK()       OVER (ORDER BY Marks DESC) AS RankNo,
       DENSE_RANK() OVER (ORDER BY Marks DESC) AS DenseRankNo
FROM Enrollments
WHERE Marks IS NOT NULL;
```

**How it works:** all three functions sort by marks (highest first) and number the rows. Compare the columns to see how ties are handled.

### Example 4: rank per course and NTILE (`partition-and-ntile.sql`)

```sql
SELECT CourseID, StudentID, Marks,
       RANK()   OVER (PARTITION BY CourseID ORDER BY Marks DESC) AS RankInCourse,
       NTILE(3) OVER (ORDER BY Marks DESC)                       AS Band
FROM Enrollments
WHERE Marks IS NOT NULL;
```

**How it works:** `PARTITION BY CourseID` starts at 1 again for every course. `NTILE(3)` divides all students into 3 bands: 1 = top, 3 = bottom.

The file `top-n-per-group.sql` shows the classic interview question "top student of each course" using a CTE.

## 🧪 Lab Practice

1. Count how many enrollments each course has. Show the course name (join `Courses`).
2. Show the average fee of courses grouped by `Credits`, rounded to 2 decimals.
3. List departments that have more than 2 students (`HAVING`).
4. Produce a merit list of all marks using `DENSE_RANK`.
5. Using `ROW_NUMBER` and `PARTITION BY StudentID`, show only each student's **first** enrollment (earliest `EnrolledOn`).

## 📝 Assignment

Create `course-report.sql` that shows, for every course: name, number of students, number with marks, average marks (2 decimals), highest marks, and a `RANK` of courses by average marks. Courses with no students must still appear (hint: `LEFT JOIN`).

## ❓ Quick Quiz

1. What is the difference between `COUNT(*)` and `COUNT(Marks)`?
2. Which clause filters groups: `WHERE` or `HAVING`?
3. Marks 80, 80, 70: what rank does 70 get with `RANK` and with `DENSE_RANK`?
4. What does `PARTITION BY` do inside `OVER()`?
5. Why might `AVG(Marks)` return 74 instead of 74.5?

<details><summary>Answers</summary>

1. `COUNT(*)` counts all rows; `COUNT(Marks)` skips NULLs · 2. `HAVING` · 3. RANK = 3, DENSE_RANK = 2 · 4. restarts the calculation for each group · 5. `Marks` is INT, so integer division drops decimals; multiply by `1.0`

</details>

## 💼 Interview Questions

1. **Difference between WHERE and HAVING?** `WHERE` filters individual rows before grouping and cannot use aggregates; `HAVING` filters groups after `GROUP BY` and can use aggregates.
2. **RANK vs DENSE_RANK vs ROW_NUMBER?** All number rows by an order; `ROW_NUMBER` is always unique, `RANK` repeats ties and leaves gaps, `DENSE_RANK` repeats ties without gaps.
3. **How do you get the top 1 row per group?** Use `ROW_NUMBER() OVER (PARTITION BY group ORDER BY value DESC)` in a CTE and keep rows where the number is 1.

## ✅ Summary

- Aggregates (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) collapse many rows into one value and ignore NULLs (except `COUNT(*)`).
- `GROUP BY` makes groups; `HAVING` filters them.
- Ranking functions need `OVER (ORDER BY ...)`; add `PARTITION BY` to restart per group.
- `ROW_NUMBER` is unique, `RANK` has gaps, `DENSE_RANK` has none, `NTILE` makes bands.

---

[⬅ Previous](../Session-06-Practice-Lab-Safe-Data-Changes-with-Transactions/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-08-Scalar-Functions-Math-String-Date/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad

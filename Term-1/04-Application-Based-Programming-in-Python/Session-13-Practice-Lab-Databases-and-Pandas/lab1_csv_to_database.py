# lab1_csv_to_database.py
# Practice (Sessions 11 + 12): load a CSV into a database table and query it back
import sqlite3
import pandas as pd

# Step 1: read and clean the CSV with pandas
df = pd.read_csv("employees.csv")
df["name"] = df["name"].str.strip().str.title()

# Step 2: save the DataFrame as a table in a SQLite database file
conn = sqlite3.connect("company.db")
df.to_sql("employees", conn, if_exists="replace", index=False)
print("Table created with", len(df), "rows")

# Step 3: run SQL with a normal cursor (Session 11 style)
cursor = conn.cursor()
cursor.execute("SELECT department, COUNT(*) FROM employees GROUP BY department")
print("Staff per department:", cursor.fetchall())

# Step 4: run SQL and get the answer as a DataFrame (pandas style)
query = "SELECT name, city, salary FROM employees WHERE salary > ? ORDER BY salary DESC"
high_paid = pd.read_sql(query, conn, params=(150000,))
print("\nEarning above 150,000:")
print(high_paid)

# Step 5: insert one new record safely, then count again
cursor.execute(
    "INSERT INTO employees (emp_id, name, department, city, join_date, salary, rating) VALUES (?, ?, ?, ?, ?, ?, ?)",
    (11, "Hamza Javed", "IT", "Islamabad", "2026-10-01", 130000, None),
)
conn.commit()
print("\nRows now:", pd.read_sql("SELECT COUNT(*) AS n FROM employees", conn)["n"][0])
conn.close()

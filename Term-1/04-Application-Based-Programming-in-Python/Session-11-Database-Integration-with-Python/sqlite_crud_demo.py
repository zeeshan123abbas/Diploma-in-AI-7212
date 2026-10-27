# sqlite_crud_demo.py
# The SAME CRUD ideas with SQLite, which is built into Python.
# Use this to practise when MySQL is not installed. Only the connect line
# and the placeholder (? instead of %s) are different.
import sqlite3

conn = sqlite3.connect("campus.db")      # creates the file if missing
cursor = conn.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT,
        marks INTEGER
    )
""")
cursor.execute("DELETE FROM students")   # start fresh each run

# Create (insert many rows at once)
rows = [("Ali", "Karachi", 78), ("Sara", "Lahore", 91), ("Bilal", "Multan", 64)]
cursor.executemany("INSERT INTO students (name, city, marks) VALUES (?, ?, ?)", rows)
conn.commit()

# Read
cursor.execute("SELECT id, name, city, marks FROM students")
print("All:", cursor.fetchall())

# Update
cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (70, "Bilal"))
# Delete
cursor.execute("DELETE FROM students WHERE name = ?", ("Ali",))
conn.commit()

# Read with a filter
cursor.execute("SELECT name, marks FROM students WHERE marks >= ?", (60,))
print("Passed:", cursor.fetchall())

conn.close()

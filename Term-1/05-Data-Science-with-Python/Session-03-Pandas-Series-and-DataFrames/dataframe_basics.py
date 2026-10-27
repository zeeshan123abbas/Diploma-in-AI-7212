# dataframe_basics.py
# A DataFrame is a 2-D table: many Series sharing the same index.

import pandas as pd

# 1) Create a DataFrame from a dictionary of lists (each key = one column)
data = {
    "name":  ["Ali", "Hina", "Usman", "Zara", "Omar"],
    "city":  ["Karachi", "Lahore", "Karachi", "Islamabad", "Lahore"],
    "age":   [20, 22, 19, 21, 23],
    "marks": [78, 91, 62, 85, 70],
}
df = pd.DataFrame(data)
print(df)

# 2) Basic information
print("\nShape (rows, columns):", df.shape)
print("Column names:", list(df.columns))
print("Data types:\n", df.dtypes)

# 3) Select one column -> you get a Series
print("\nMarks column:\n", df["marks"])

# 4) Select several columns -> you get a DataFrame
print("\nName and marks:\n", df[["name", "marks"]])

# 5) Add a new column calculated from another column
df["passed"] = df["marks"] >= 65
print("\nWith a new 'passed' column:\n", df)

# 6) Filter rows with a condition
print("\nStudents from Karachi:\n", df[df["city"] == "Karachi"])

# 7) Sort rows
print("\nSorted by marks (high to low):\n", df.sort_values("marks", ascending=False))

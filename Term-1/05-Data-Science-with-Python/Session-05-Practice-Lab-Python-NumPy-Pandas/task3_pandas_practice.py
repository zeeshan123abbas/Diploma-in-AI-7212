# task3_pandas_practice.py  (Practice for Session 03)
# Task: Series, DataFrame, loc and iloc on students.csv

import pandas as pd

df = pd.read_csv("students.csv")

# Step 1: make roll_no the index so we can use loc with roll numbers
df = df.set_index("roll_no")

# Step 2: a Series of Python marks
python_marks = df["python"]
print("Top scorer in Python:", df.loc[python_marks.idxmax(), "name"])

# Step 3: add total and percentage columns
df["total"] = df["python"] + df["stats"] + df["sql"]
df["percent"] = (df["total"] / 300 * 100).round(1)

# Step 4: loc - name and percent of roll numbers 104 to 107 (107 included)
print("\nloc 104..107:\n", df.loc[104:107, ["name", "percent"]])

# Step 5: iloc - first 3 rows and first 2 columns
print("\niloc first 3 rows, 2 columns:\n", df.iloc[0:3, 0:2])

# Step 6: filter - girls with attendance above 85
girls = df[(df["gender"] == "F") & (df["attendance"] > 85)]
print("\nGirls with 85%+ attendance:\n", girls[["name", "attendance"]])

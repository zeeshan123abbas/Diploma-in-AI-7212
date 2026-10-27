# task1_python_basics.py  (Practice for Session 01)
# Task: classify the columns of students.csv and do a plain-Python summary.

# Step 1: describe each column's data type by hand
column_types = {
    "roll_no": "Categorical (an ID, not for maths)",
    "name": "Categorical - nominal",
    "gender": "Categorical - nominal",
    "section": "Categorical - nominal",
    "attendance": "Numerical - continuous (percentage)",
    "python": "Numerical - discrete (marks)",
}
for column, kind in column_types.items():
    print(f"{column:<11} -> {kind}")

# Step 2: plain-Python average of a list of marks
python_marks = [78, 91, 55, 88, 42, 73, 85, 66, 39, 94, 70, 80]
average = sum(python_marks) / len(python_marks)
print("\nAverage Python marks:", round(average, 2))

# Step 3: count how many students scored below 50
below_50 = 0
for mark in python_marks:
    if mark < 50:
        below_50 = below_50 + 1
print("Students below 50:", below_50)

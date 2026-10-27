# task4_groupby_practice.py  (Practice for Session 04)
# Task: explore and summarise students.csv, then save a report.

import pandas as pd

df = pd.read_csv("students.csv")
df["percent"] = ((df["python"] + df["stats"] + df["sql"]) / 3).round(1)

# Step 1: quick exploration
print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Students per section:\n", df["section"].value_counts())

# Step 2: average percent per section
section_avg = df.groupby("section")["percent"].mean().round(1)
print("\nAverage % per section:\n", section_avg)

# Step 3: several statistics per gender
print("\nAttendance by gender:\n", df.groupby("gender")["attendance"].agg(["mean", "min", "max"]))

# Step 4: does attendance matter? compare high and low attendance groups
def attendance_group(value):
    # label each student by attendance
    if value >= 80:
        return "80+"
    return "below 80"

df["attendance_group"] = df["attendance"].apply(attendance_group)
print("\nAverage % by attendance group:\n", df.groupby("attendance_group")["percent"].mean().round(1))

# Step 5: save the section report
section_avg.to_csv("section_report.csv", header=["average_percent"])
print("\nSaved section_report.csv")

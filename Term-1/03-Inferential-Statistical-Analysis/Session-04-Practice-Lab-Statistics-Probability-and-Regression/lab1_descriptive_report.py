# lab1_descriptive_report.py
# Practice for Session 01: a full descriptive report of students.csv
import pandas as pd

# Step 1: load the data file (it is in the same folder)
df = pd.read_csv("students.csv")
print("Rows and columns:", df.shape)
print(df.head())

# Step 2: centre of the marks
print("\nMean marks  :", round(df["marks"].mean(), 2))
print("Median marks:", df["marks"].median())
print("Mode marks  :", df["marks"].mode().tolist())

# Step 3: spread of the marks
print("Std dev     :", round(df["marks"].std(), 2))
q1, q3 = df["marks"].quantile([0.25, 0.75])
iqr = q3 - q1
print("IQR         :", iqr)

# Step 4: outliers using the 1.5 * IQR rule
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = df[(df["marks"] < low) | (df["marks"] > high)]
print("Outliers    :", len(outliers))

# Step 5: skewness (positive = right tail, negative = left tail)
print("Skewness    :", round(df["marks"].skew(), 3))

# Step 6: average marks per city
print("\nAverage marks by city:")
print(df.groupby("city")["marks"].mean().round(1).sort_values(ascending=False))

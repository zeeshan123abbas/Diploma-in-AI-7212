# describe_with_pandas.py
# One line summary of a whole dataset using pandas
import pandas as pd

# Step 1: a small table of students
data = {
    "name":   ["Ali", "Sara", "Bilal", "Hina", "Usman", "Ayesha"],
    "age":    [19, 21, 20, 22, 19, 20],
    "marks":  [72, 88, 65, 91, 58, 79],
    "city":   ["Karachi", "Lahore", "Karachi", "Multan", "Karachi", "Lahore"],
}
df = pd.DataFrame(data)

# Step 2: describe() gives count, mean, std, min, quartiles and max
print(df.describe())

# Step 3: for text (categorical) columns, count each category
print("\nStudents per city:")
print(df["city"].value_counts())

# Step 4: quartiles and IQR (inter-quartile range) of marks
q1 = df["marks"].quantile(0.25)
q3 = df["marks"].quantile(0.75)
print("\nQ1 =", q1, " Q3 =", q3, " IQR =", q3 - q1)

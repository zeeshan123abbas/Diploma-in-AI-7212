# numpy_use_case.py
# Real-world use case: a class result sheet calculated with NumPy.

import numpy as np

names = np.array(["Ali", "Hina", "Usman", "Zara"])
# columns: English, Maths, Science (out of 100)
marks = np.array([
    [72, 88, 65],
    [91, 79, 94],
    [45, 52, 60],
    [83, 95, 77],
])

# Step 1: total and percentage of each student
totals = marks.sum(axis=1)
percentages = totals / 300 * 100
print("Totals:", totals)
print("Percentages:", np.round(percentages, 1))

# Step 2: give grades using np.where (if / else for arrays)
grades = np.where(percentages >= 80, "A",
         np.where(percentages >= 60, "B", "C"))

# Step 3: print a neat result sheet
print("\nName    Total  Percent  Grade")
for i in range(len(names)):
    print(f"{names[i]:<7} {totals[i]:>5}  {percentages[i]:>6.1f}   {grades[i]}")

# Step 4: subject-wise class average and topper
print("\nSubject averages (Eng, Math, Sci):", marks.mean(axis=0).round(1))
print("Class topper:", names[totals.argmax()])

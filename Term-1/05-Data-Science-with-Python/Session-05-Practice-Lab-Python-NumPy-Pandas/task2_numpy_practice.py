# task2_numpy_practice.py  (Practice for Session 02)
# Task: use NumPy to analyse the marks of 12 students in 3 subjects.

import numpy as np

# Step 1: marks as a 2-D array (rows = students, columns = python, stats, sql)
marks = np.array([
    [78, 65, 81], [91, 84, 77], [55, 48, 60], [88, 92, 90],
    [42, 51, 58], [73, 70, 69], [85, 79, 88], [66, 58, 72],
    [39, 44, 50], [94, 89, 96], [70, 74, 65], [80, 77, 83],
])
print("Shape:", marks.shape)

# Step 2: average of each subject (down the columns)
print("Subject averages:", marks.mean(axis=0).round(1))

# Step 3: total and percentage of each student (across the rows)
totals = marks.sum(axis=1)
percent = (totals / 300 * 100).round(1)
print("Percentages:", percent)

# Step 4: how many students got 80% or more?
print("Students with 80%+:", (percent >= 80).sum())

# Step 5: the highest single mark and where it is
row, col = np.unravel_index(marks.argmax(), marks.shape)
print("Highest mark", marks.max(), "-> student row", row, "subject column", col)

# Step 6: add 5 grace marks to stats only, but never above 100
marks[:, 1] = np.minimum(marks[:, 1] + 5, 100)
print("Stats after grace:", marks[:, 1])

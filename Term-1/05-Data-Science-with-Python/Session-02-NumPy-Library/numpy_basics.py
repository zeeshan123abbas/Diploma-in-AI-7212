# numpy_basics.py
# Creating NumPy arrays and looking at their properties.

import numpy as np   # "np" is the short name everyone uses

# 1) Create an array from a Python list
marks = np.array([78, 85, 62, 90, 71])
print("Array:", marks)
print("Type:", type(marks))
print("Data type of items:", marks.dtype)   # int64 = whole numbers
print("Shape:", marks.shape)                # (5,) -> 5 items, 1 dimension
print("Dimensions:", marks.ndim)

# 2) A 2-D array (rows x columns): 3 students, 4 subjects
scores = np.array([
    [78, 85, 62, 90],
    [55, 67, 80, 72],
    [88, 91, 79, 95],
])
print("\n2-D array:\n", scores)
print("Shape:", scores.shape)               # (3, 4) -> 3 rows, 4 columns
print("Total items:", scores.size)

# 3) Ready-made arrays
print("\nZeros:", np.zeros(4))
print("Ones:", np.ones(3))
print("Range 0..9 step 2:", np.arange(0, 10, 2))
print("5 evenly spaced numbers 0..1:", np.linspace(0, 1, 5))

# 4) Indexing and slicing (same idea as lists)
print("\nFirst mark:", marks[0])
print("Last mark:", marks[-1])
print("First three marks:", marks[:3])
print("Student 2, subject 3:", scores[1, 2])   # row 1, column 2 (counting from 0)
print("All marks of subject 1:", scores[:, 0])  # every row, column 0

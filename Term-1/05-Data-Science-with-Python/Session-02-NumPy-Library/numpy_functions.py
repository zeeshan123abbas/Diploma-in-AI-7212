# numpy_functions.py
# Useful built-in NumPy functions for quick analysis.

import numpy as np

temps = np.array([31, 34, 29, 36, 38, 33, 30])   # one week of temperatures in Karachi

# 1) Summary statistics
print("Mean (average):", temps.mean())
print("Median:", np.median(temps))
print("Minimum:", temps.min(), " Maximum:", temps.max())
print("Standard deviation:", round(temps.std(), 2))
print("Sum:", temps.sum())

# 2) Position of the min and max values
print("Hottest day index:", temps.argmax())
print("Coolest day index:", temps.argmin())

# 3) Filtering with a condition (boolean mask)
hot_days = temps > 33          # gives True/False for each day
print("\nIs it hot?", hot_days)
print("Hot temperatures:", temps[hot_days])
print("How many hot days:", hot_days.sum())   # True counts as 1

# 4) Sorting and rounding
print("\nSorted:", np.sort(temps))
print("Square root:", np.round(np.sqrt(temps), 2))

# 5) Reshape: 6 numbers into 2 rows x 3 columns
numbers = np.arange(1, 7)
table = numbers.reshape(2, 3)
print("\nReshaped:\n", table)
print("Column sums:", table.sum(axis=0))  # axis=0 -> down the columns
print("Row sums:", table.sum(axis=1))     # axis=1 -> across the rows

# 6) Random numbers (seed makes results repeatable)
rng = np.random.default_rng(seed=42)
dice = rng.integers(1, 7, size=10)   # 10 dice rolls (1 to 6)
print("\nDice rolls:", dice)

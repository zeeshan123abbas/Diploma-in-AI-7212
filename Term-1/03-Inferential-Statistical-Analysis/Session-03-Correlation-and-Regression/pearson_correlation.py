# pearson_correlation.py
# Pearson correlation: strength of a LINEAR relationship between two numbers
import numpy as np
from scipy import stats

# Step 1: hours studied and exam marks of 8 students
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
marks = np.array([35, 42, 50, 55, 61, 68, 74, 83])

# Step 2: calculate r by the formula (to understand it)
hours_dev = hours - hours.mean()
marks_dev = marks - marks.mean()
r_manual = (hours_dev * marks_dev).sum() / np.sqrt((hours_dev ** 2).sum() * (marks_dev ** 2).sum())
print("r (manual) =", round(r_manual, 4))

# Step 3: same answer with scipy, plus a p-value
r, p_value = stats.pearsonr(hours, marks)
print("r (scipy)  =", round(r, 4), " p-value =", round(p_value, 6))

# Step 4: interpret the strength
if abs(r) >= 0.7:
    print("Strong relationship")
elif abs(r) >= 0.4:
    print("Moderate relationship")
else:
    print("Weak relationship")

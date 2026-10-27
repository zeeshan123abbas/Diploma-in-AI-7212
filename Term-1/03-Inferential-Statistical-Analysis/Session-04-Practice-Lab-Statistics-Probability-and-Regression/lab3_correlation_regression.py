# lab3_correlation_regression.py
# Practice for Session 03: what drives marks?
import pandas as pd
from scipy import stats

df = pd.read_csv("students.csv")

# Step 1: correlation of every numeric column with marks
numeric = df[["study_hours", "attendance", "marks"]]
print("Pearson correlation matrix:")
print(numeric.corr().round(3))

# Step 2: Spearman for comparison
print("\nSpearman correlation matrix:")
print(numeric.corr(method="spearman").round(3))

# Step 3: regression line marks = a + b * study_hours
line = stats.linregress(df["study_hours"], df["marks"])
print(f"\nmarks = {line.intercept:.2f} + {line.slope:.2f} * study_hours")
print("R-squared:", round(line.rvalue ** 2, 3))

# Step 4: predictions for 3, 6 and 9 hours of study
for h in [3, 6, 9]:
    print(f"Predicted marks for {h} hours: {line.intercept + line.slope * h:.1f}")

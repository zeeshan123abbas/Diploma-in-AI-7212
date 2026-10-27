# missing_values.py
# Finding and filling (imputing) missing values.

import numpy as np
import pandas as pd

# na_values tells pandas to treat the word "unknown" as missing too
df = pd.read_csv("messy_customers.csv", na_values=["unknown"])

# 1) FIND missing values
print("Missing values per column:\n", df.isnull().sum(), "\n")
print("Rows that have at least one missing value:\n", df[df.isnull().any(axis=1)], "\n")

# 2) Option A: DROP rows with missing values (simple, but we lose data)
dropped = df.dropna()
print("Rows before:", len(df), " after dropna:", len(dropped))

# 3) Option B: FILL (impute) missing values - usually better
filled = df.copy()
filled["age"] = filled["age"].fillna(filled["age"].median())              # numbers -> median
filled["monthly_income"] = filled["monthly_income"].fillna(filled["monthly_income"].mean().round())
filled["city"] = filled["city"].fillna("Unknown")                         # text -> a label
print("\nMissing after filling:", filled.isnull().sum().sum())
print(filled[["name", "city", "age", "monthly_income"]])

# 4) A value that is present but WRONG (age 250) - treat it as missing, then fill
filled.loc[filled["age"] > 100, "age"] = np.nan
filled["age"] = filled["age"].fillna(filled["age"].median())
print("\nAges after fixing the impossible value:", filled["age"].tolist())

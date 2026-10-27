# duplicates_and_text.py
# Removing duplicate rows and fixing messy text.

import pandas as pd

df = pd.read_csv("messy_customers.csv")

# 1) Duplicates
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df))

# 2) Messy text: extra spaces and mixed CAPITAL/small letters
print("\nCities before:", df["city"].unique().tolist())
df["city"] = df["city"].str.strip().str.title()     # remove spaces, then "Karachi" style
df["name"] = df["name"].str.strip().str.title()
print("Cities after: ", df["city"].unique().tolist())
print("Names:", df["name"].tolist())

# 3) A column that should be numbers but contains text ("unknown")
print("\nIncome type before:", df["monthly_income"].dtype)
df["monthly_income"] = pd.to_numeric(df["monthly_income"], errors="coerce")  # bad text -> NaN
print("Income type after: ", df["monthly_income"].dtype)

# 4) Save the cleaner file
df.to_csv("customers_clean.csv", index=False)
print("\nSaved customers_clean.csv")

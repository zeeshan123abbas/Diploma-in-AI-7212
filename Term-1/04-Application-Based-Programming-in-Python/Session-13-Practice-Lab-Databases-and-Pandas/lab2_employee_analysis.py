# lab2_employee_analysis.py
# Practice (Session 12): explore, clean and summarise with pandas
import pandas as pd

df = pd.read_csv("employees.csv", parse_dates=["join_date"])

# Step 1: clean text and missing values
df["name"] = df["name"].str.strip().str.title()
print("Missing ratings:", df["rating"].isna().sum())
df["rating"] = df["rating"].fillna(df["rating"].mean()).round(1)

# Step 2: new columns
df["years_of_service"] = 2026 - df["join_date"].dt.year
df["salary_band"] = pd.cut(df["salary"], bins=[0, 100000, 160000, 1000000],
                           labels=["Junior", "Mid", "Senior"])

# Step 3: summaries
print("\nAverage salary by department:")
print(df.groupby("department")["salary"].mean().round(0).sort_values(ascending=False))

print("\nCount per salary band:")
print(df["salary_band"].value_counts())

print("\nTop rated employee in each department:")
best = df.loc[df.groupby("department")["rating"].idxmax(), ["department", "name", "rating"]]
print(best.to_string(index=False))

# Step 4: pivot table: departments x cities, average salary
print("\nPivot (average salary):")
print(pd.pivot_table(df, values="salary", index="department", columns="city", aggfunc="mean").fillna("-"))

# lab3_raise_report.py
# Practice: business rule with pandas, write results to DB and CSV
import sqlite3
import pandas as pd

df = pd.read_csv("employees.csv")
df["name"] = df["name"].str.strip().str.title()
df["rating"] = df["rating"].fillna(3.0)

# Rule: rating >= 4.5 -> 15% raise, >= 4.0 -> 10%, otherwise 5%
def raise_percent(rating):
    if rating >= 4.5:
        return 15
    elif rating >= 4.0:
        return 10
    return 5

df["raise_pct"] = df["rating"].apply(raise_percent)
df["new_salary"] = (df["salary"] * (1 + df["raise_pct"] / 100)).round(0).astype(int)

report = df[["name", "department", "salary", "rating", "raise_pct", "new_salary"]]
print(report.to_string(index=False))
print("\nExtra yearly cost: Rs.", int((df["new_salary"] - df["salary"]).sum() * 12))

# Save to CSV and to a database table
report.to_csv("raise_report.csv", index=False)
with sqlite3.connect("company.db") as conn:
    report.to_sql("raise_report", conn, if_exists="replace", index=False)
print("Saved raise_report.csv and table raise_report")

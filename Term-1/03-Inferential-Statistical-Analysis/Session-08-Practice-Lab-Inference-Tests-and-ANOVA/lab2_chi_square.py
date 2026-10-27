# lab2_chi_square.py
# Practice for Session 06: is returning next month related to the channel?
import pandas as pd
from scipy import stats

df = pd.read_csv("campaign.csv")

# Step 1: build a contingency table of counts with pandas
table = pd.crosstab(df["channel"], df["returned_next_month"])
print("Observed counts:")
print(table)

# Step 2: chi-square test of independence
chi2, p, dof, expected = stats.chi2_contingency(table)
print(f"\nchi2 = {chi2:.2f}, df = {dof}, p = {p:.4f}")

# Step 3: check the rule "every expected count >= 5"
print("All expected counts >= 5?", (expected >= 5).all())

# Step 4: return rate per channel for the business report
rate = (df["returned_next_month"] == "Yes").groupby(df["channel"]).mean()
print("\nReturn rate by channel:")
print(rate.round(2))

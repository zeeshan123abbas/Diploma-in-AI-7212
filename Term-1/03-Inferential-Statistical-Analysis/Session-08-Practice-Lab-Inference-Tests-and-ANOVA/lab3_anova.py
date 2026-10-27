# lab3_anova.py
# Practice for Session 07: compare order value across ALL three channels
import pandas as pd
from scipy import stats

df = pd.read_csv("campaign.csv")

# Step 1: split order values into one list per channel
groups = [g["order_value"].to_numpy() for _, g in df.groupby("channel")]
names = sorted(df["channel"].unique())
print(df.groupby("channel")["order_value"].agg(["count", "mean", "std"]).round(0))

# Step 2: check equal variances first (Levene)
stat, p_lev = stats.levene(*groups)
print(f"\nLevene p = {p_lev:.3f}  (p > 0.05 means variances look equal)")

# Step 3: one-way ANOVA
f, p = stats.f_oneway(*groups)
print(f"ANOVA: F = {f:.2f}, p = {p:.5f}")

# Step 4: if significant, find which pairs differ with Tukey's HSD
if p < 0.05:
    res = stats.tukey_hsd(*groups)
    for i in range(3):
        for j in range(i + 1, 3):
            print(f"  {names[i]} vs {names[j]}: p = {res.pvalue[i, j]:.4f}")

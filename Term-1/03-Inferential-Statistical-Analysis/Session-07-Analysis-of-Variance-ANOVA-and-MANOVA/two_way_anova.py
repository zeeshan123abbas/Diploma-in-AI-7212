# two_way_anova.py
# Two-way ANOVA (balanced design) calculated step by step with pandas.
# Question: do FERTILISER type and WATERING level affect plant growth (cm)?
import pandas as pd
from scipy import stats

# Step 1: 2 fertilisers x 2 watering levels x 3 plants each
df = pd.DataFrame({
    "fertiliser": ["A"] * 6 + ["B"] * 6,
    "water": ["low", "low", "low", "high", "high", "high"] * 2,
    "growth": [10, 12, 11, 15, 16, 14,    13, 14, 12, 20, 22, 21],
})

grand = df["growth"].mean()
r = 3                                    # plants in each cell
a = df["fertiliser"].nunique()           # levels of factor A
b = df["water"].nunique()                # levels of factor B

# Step 2: sums of squares for each source of variation
ss_a = b * r * ((df.groupby("fertiliser")["growth"].mean() - grand) ** 2).sum()
ss_b = a * r * ((df.groupby("water")["growth"].mean() - grand) ** 2).sum()
cell_means = df.groupby(["fertiliser", "water"])["growth"].transform("mean")
ss_cells = r * ((df.groupby(["fertiliser", "water"])["growth"].mean() - grand) ** 2).sum()
ss_ab = ss_cells - ss_a - ss_b          # interaction
ss_error = ((df["growth"] - cell_means) ** 2).sum()

# Step 3: degrees of freedom and mean squares
df_a, df_b, df_ab, df_e = a - 1, b - 1, (a - 1) * (b - 1), a * b * (r - 1)
ms_e = ss_error / df_e

# Step 4: F and p for each effect
for name, ss, d in [("Fertiliser", ss_a, df_a), ("Water", ss_b, df_b), ("Interaction", ss_ab, df_ab)]:
    f = (ss / d) / ms_e
    p = 1 - stats.f.cdf(f, d, df_e)
    print(f"{name:12} SS = {ss:6.2f}  F = {f:6.2f}  p = {p:.4f}")

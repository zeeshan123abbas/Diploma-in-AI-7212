# spearman_rank.py
# Spearman's rank correlation: works on RANKS, good for ordinal data or outliers
import pandas as pd
from scipy import stats

# Step 1: two judges rank 6 singers in a competition (1 = best)
df = pd.DataFrame({
    "singer":  ["A", "B", "C", "D", "E", "F"],
    "judge_1": [1, 2, 3, 4, 5, 6],
    "judge_2": [2, 1, 4, 3, 6, 5],
})

# Step 2: the classic formula  rho = 1 - 6*sum(d^2) / (n*(n^2 - 1))
df["d"] = df["judge_1"] - df["judge_2"]
n = len(df)
rho_manual = 1 - 6 * (df["d"] ** 2).sum() / (n * (n ** 2 - 1))
print(df)
print("rho (manual) =", round(rho_manual, 4))

# Step 3: scipy does the same (and ranks the data for you)
rho, p_value = stats.spearmanr(df["judge_1"], df["judge_2"])
print("rho (scipy)  =", round(rho, 4))

# Step 4: Pearson vs Spearman when there is an outlier
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 100]       # last value is an outlier
print("Pearson  r  :", round(stats.pearsonr(x, y)[0], 3))
print("Spearman rho:", round(stats.spearmanr(x, y)[0], 3))

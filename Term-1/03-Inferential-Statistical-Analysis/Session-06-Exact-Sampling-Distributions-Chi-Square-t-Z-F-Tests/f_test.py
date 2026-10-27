# f_test.py
# F-test: compare the VARIANCES (consistency) of two groups
import numpy as np
from scipy import stats

# Step 1: weights (grams) of biscuit packets from two machines
machine_a = np.array([200, 202, 199, 201, 200, 198, 201, 200])
machine_b = np.array([195, 205, 198, 207, 193, 202, 199, 204])

# Step 2: sample variances
var_a = machine_a.var(ddof=1)
var_b = machine_b.var(ddof=1)

# Step 3: F = larger variance / smaller variance
f_stat = max(var_a, var_b) / min(var_a, var_b)
df1 = df2 = len(machine_a) - 1

# Step 4: two-sided p-value from the F distribution
p_value = 2 * (1 - stats.f.cdf(f_stat, df1, df2))

print(f"Variance A = {var_a:.2f}, Variance B = {var_b:.2f}")
print(f"F = {f_stat:.2f}, p = {p_value:.4f}")
print("Machines differ in consistency" if p_value < 0.05 else "No evidence of different consistency")

# Step 5: Levene's test is a robust alternative used in practice
stat, p_lev = stats.levene(machine_a, machine_b)
print(f"Levene p = {p_lev:.4f}")

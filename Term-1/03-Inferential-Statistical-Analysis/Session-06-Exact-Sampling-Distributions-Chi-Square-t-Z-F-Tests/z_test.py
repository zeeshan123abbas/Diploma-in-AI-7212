# z_test.py
# Z-test: compare a mean when the population SD (sigma) is KNOWN or n is large
import numpy as np
from scipy import stats

# Step 1: a juice factory says cartons hold 1000 ml, sigma = 15 ml (known).
# We measure 40 cartons and get a sample mean of 994 ml.
mu_0 = 1000
sigma = 15
n = 40
sample_mean = 994

# Step 2: z statistic = (x_bar - mu) / (sigma / sqrt(n))
z = (sample_mean - mu_0) / (sigma / np.sqrt(n))

# Step 3: two-sided p-value from the standard normal distribution
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

# Step 4: critical value for alpha = 0.05 (two-sided)
z_crit = stats.norm.ppf(0.975)

print("z statistic =", round(z, 3))
print("critical z  = +/-", round(z_crit, 3))
print("p-value     =", round(p_value, 5))
print("Decision    :", "Reject H0 - cartons are underfilled or overfilled" if p_value < 0.05 else "Fail to reject H0")

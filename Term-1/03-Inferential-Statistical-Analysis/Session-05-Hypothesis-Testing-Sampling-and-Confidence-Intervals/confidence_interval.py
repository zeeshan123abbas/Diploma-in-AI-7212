# confidence_interval.py
# 95% confidence interval for a mean
import numpy as np
from scipy import stats

# Step 1: delivery times (minutes) of 12 food orders
times = np.array([28, 35, 31, 40, 26, 33, 37, 30, 29, 34, 38, 32])
n = len(times)
mean = times.mean()
sd = times.std(ddof=1)

# Step 2: standard error of the mean
se = sd / np.sqrt(n)

# Step 3: t critical value for 95% confidence (small sample -> t)
t_crit = stats.t.ppf(0.975, df=n - 1)

# Step 4: margin of error and interval
margin = t_crit * se
print(f"Mean = {mean:.2f}, SE = {se:.2f}, t* = {t_crit:.3f}")
print(f"95% CI = ({mean - margin:.2f}, {mean + margin:.2f}) minutes")

# Step 5: the same interval in one line with scipy
low, high = stats.t.interval(0.95, df=n - 1, loc=mean, scale=se)
print(f"scipy  = ({low:.2f}, {high:.2f})")

# Step 6: a 99% interval is wider (more confidence = less precision)
low99, high99 = stats.t.interval(0.99, df=n - 1, loc=mean, scale=se)
print(f"99% CI = ({low99:.2f}, {high99:.2f})")

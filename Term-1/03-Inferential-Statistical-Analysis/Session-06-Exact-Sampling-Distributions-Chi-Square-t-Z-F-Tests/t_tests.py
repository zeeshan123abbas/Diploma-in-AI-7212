# t_tests.py
# Three kinds of t-test for comparing MEANS (small samples, sigma unknown)
import numpy as np
from scipy import stats

alpha = 0.05

# 1) One-sample: is the average battery life different from 10 hours?
battery = np.array([9.6, 10.2, 9.8, 9.5, 9.9, 9.7, 10.1, 9.4])
t, p = stats.ttest_1samp(battery, popmean=10)
print(f"One-sample  : t = {t:.3f}, p = {p:.4f}")

# 2) Independent two-sample: do Morning and Evening batches score differently?
morning = np.array([72, 78, 65, 80, 74, 69, 77])
evening = np.array([68, 70, 62, 66, 71, 64, 67])
t, p = stats.ttest_ind(morning, evening, equal_var=False)   # Welch's t-test
print(f"Independent : t = {t:.3f}, p = {p:.4f}")

# 3) Paired: same students before and after a revision class
before = np.array([55, 60, 48, 70, 65, 58])
after  = np.array([62, 64, 55, 72, 70, 63])
t, p = stats.ttest_rel(after, before)
print(f"Paired      : t = {t:.3f}, p = {p:.4f}")
print("Revision class helped?", "Yes" if p < alpha else "No evidence")

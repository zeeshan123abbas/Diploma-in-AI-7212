# chi_square_tests.py
# Chi-square tests work with COUNTS of categories
import numpy as np
from scipy import stats

# ---- Part A: goodness of fit ----
# Is a die fair? We rolled it 120 times.
observed = np.array([25, 17, 15, 23, 24, 16])   # counts of 1..6
expected = np.array([20, 20, 20, 20, 20, 20])   # fair die: 120 / 6 each

chi2, p = stats.chisquare(f_obs=observed, f_exp=expected)
print("Goodness of fit: chi2 =", round(chi2, 3), " p =", round(p, 4))
print("Die looks", "UNFAIR" if p < 0.05 else "fair (no evidence of bias)")

# ---- Part B: test of independence ----
# Is course choice related to gender? (contingency table of counts)
#                 Python  Design  Networking
table = np.array([[30,     10,     20],     # male
                  [25,     25,     10]])    # female

chi2, p, dof, expected_table = stats.chi2_contingency(table)
print("\nIndependence: chi2 =", round(chi2, 3), " dof =", dof, " p =", round(p, 4))
print("Expected counts if NOT related:")
print(expected_table.round(1))
print("Course choice and gender are", "RELATED" if p < 0.05 else "independent")

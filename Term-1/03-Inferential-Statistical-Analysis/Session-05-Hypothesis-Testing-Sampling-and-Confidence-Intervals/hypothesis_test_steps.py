# hypothesis_test_steps.py
# The 5 steps of a hypothesis test, written out one by one.
# Claim: a restaurant says the average delivery time is 30 minutes.
# We think it is MORE than 30.
import numpy as np
from scipy import stats

times = np.array([28, 35, 31, 40, 26, 33, 37, 30, 29, 34, 38, 32])

# Step 1: state the hypotheses
#   H0: mu = 30   (the claim is true)
#   H1: mu > 30   (deliveries are slower)
claimed_mean = 30

# Step 2: choose the level of significance
alpha = 0.05

# Step 3: calculate the test statistic (one-sample t-test, one-sided)
t_stat, p_value = stats.ttest_1samp(times, popmean=claimed_mean, alternative="greater")
print("t statistic =", round(t_stat, 3))
print("p-value     =", round(p_value, 4))

# Step 4: compare p-value with alpha
if p_value < alpha:
    decision = "Reject H0"
else:
    decision = "Fail to reject H0"
print("Decision    :", decision)

# Step 5: conclusion in plain words
if decision == "Reject H0":
    print("There is enough evidence that average delivery takes more than 30 minutes.")
else:
    print("Not enough evidence that deliveries are slower than 30 minutes.")

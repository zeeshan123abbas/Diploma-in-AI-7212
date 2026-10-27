# ci_simulation.py
# What does "95% confident" really mean? Let's simulate it.
import numpy as np
from scipy import stats

rng = np.random.default_rng(0)
true_mean = 50          # we know the truth here because we created the data
captured = 0
trials = 1000

for _ in range(trials):
    # Step 1: draw a sample of 25 values from the population
    sample = rng.normal(loc=true_mean, scale=10, size=25)
    # Step 2: build its 95% confidence interval
    se = sample.std(ddof=1) / np.sqrt(len(sample))
    low, high = stats.t.interval(0.95, df=24, loc=sample.mean(), scale=se)
    # Step 3: did the interval catch the true mean?
    if low <= true_mean <= high:
        captured += 1

# Step 4: about 95% of intervals contain the true mean
print(f"{captured} of {trials} intervals contained the true mean ({captured / trials:.1%})")

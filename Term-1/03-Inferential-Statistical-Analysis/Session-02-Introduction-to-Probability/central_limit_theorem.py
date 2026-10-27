# central_limit_theorem.py
# Even if data is NOT normal, the averages of many samples look normal.
import numpy as np

rng = np.random.default_rng(42)

# Step 1: a skewed population (waiting times, exponential, mean = 10 min)
population = rng.exponential(scale=10, size=100_000)
print("Population mean:", round(population.mean(), 2))

# Step 2: take 2,000 samples of size 40 and store each sample's mean
sample_means = []
for _ in range(2000):
    sample = rng.choice(population, size=40)
    sample_means.append(sample.mean())
sample_means = np.array(sample_means)

# Step 3: the sample means centre on the population mean
print("Mean of sample means:", round(sample_means.mean(), 2))

# Step 4: their spread is close to sigma / sqrt(n)  (the standard error)
print("SD of sample means  :", round(sample_means.std(), 2))
print("sigma / sqrt(n)     :", round(population.std() / np.sqrt(40), 2))

# Step 5: a quick text histogram shows the bell shape
counts, edges = np.histogram(sample_means, bins=10)
for c, left in zip(counts, edges):
    print(f"{left:5.1f} | " + "#" * (c // 10))

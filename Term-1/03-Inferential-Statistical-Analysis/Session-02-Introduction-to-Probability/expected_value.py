# expected_value.py
# Expected value of a discrete random variable: E[X] = sum of x * P(x)

# Step 1: a lucky-draw ticket costs Rs. 100. Possible prizes and chances:
prizes        = [0,    100,  500, 5000]
probabilities = [0.80, 0.15, 0.04, 0.01]

# Step 2: check that probabilities add up to 1
print("Total probability:", sum(probabilities))

# Step 3: expected prize
expected = 0
for x, p in zip(prizes, probabilities):
    expected += x * p
print("Expected prize: Rs.", expected)

# Step 4: variance = sum of (x - mean)^2 * P(x)
variance = sum((x - expected) ** 2 * p for x, p in zip(prizes, probabilities))
print("Variance:", round(variance, 2))

# Step 5: compare with ticket price
print("Expected profit per ticket: Rs.", expected - 100)

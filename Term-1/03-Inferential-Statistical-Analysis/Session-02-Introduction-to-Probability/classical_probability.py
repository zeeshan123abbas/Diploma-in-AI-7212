# classical_probability.py
# Classical probability = favourable outcomes / total outcomes
import random

# Step 1: all outcomes of rolling one fair die
outcomes = [1, 2, 3, 4, 5, 6]

# Step 2: the event "roll an even number"
even = [x for x in outcomes if x % 2 == 0]

# Step 3: theoretical probability
p_even = len(even) / len(outcomes)
print("Theoretical P(even) =", p_even)

# Step 4: experiment - roll the die 10,000 times and count evens
random.seed(1)                 # same random numbers every run
rolls = 10_000
even_count = 0
for _ in range(rolls):
    if random.choice(outcomes) % 2 == 0:
        even_count += 1

# Step 5: experimental probability gets close to 0.5 for many rolls
print("Experimental P(even) =", even_count / rolls)

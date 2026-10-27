# perceptron.py
# One artificial neuron (a perceptron) built from scratch with NumPy.
# It learns the logical AND gate: output 1 only when both inputs are 1.
# Command:  python perceptron.py

import numpy as np

# Training data: 4 examples of the AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

weights = np.zeros(2)     # one weight per input, start at zero
bias = 0.0
learning_rate = 0.1

def step(value):
    """Activation function: fire (1) if value is positive, else 0."""
    return 1 if value > 0 else 0

# Training loop: show all examples several times (each pass = one epoch)
for epoch in range(10):
    errors = 0
    for inputs, target in zip(X, y):
        weighted_sum = np.dot(inputs, weights) + bias   # w1*x1 + w2*x2 + b
        output = step(weighted_sum)
        error = target - output                         # 0 if correct
        weights += learning_rate * error * inputs       # nudge weights
        bias += learning_rate * error                   # nudge bias
        errors += abs(error)
    print(f"Epoch {epoch + 1}: mistakes = {errors}")
    if errors == 0:
        break

print("\nLearned weights:", weights, "bias:", round(bias, 2))
for inputs in X:
    print(inputs, "->", step(np.dot(inputs, weights) + bias))

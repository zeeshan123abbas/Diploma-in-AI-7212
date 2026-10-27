# rules_vs_learning.py
# Traditional programming (we write the rules) vs Machine Learning (the computer learns the rules).
# Command:  python rules_vs_learning.py

from sklearn.tree import DecisionTreeClassifier

# --- Part 1: Traditional programming -------------------------------------
# A human writes the rule by hand.
def is_hot_by_rule(temperature):
    if temperature >= 35:      # rule chosen by a human
        return "hot"
    return "not hot"

print("Rule-based answers:")
for t in [20, 34, 36, 41]:
    print(f"  {t} C ->", is_hot_by_rule(t))

# --- Part 2: Machine Learning --------------------------------------------
# We only give EXAMPLES (data + correct answers). The model finds the rule itself.
temperatures = [[18], [22], [25], [29], [31], [33], [36], [38], [40], [44]]  # inputs (features)
labels = ["not hot", "not hot", "not hot", "not hot", "not hot",
          "not hot", "hot", "hot", "hot", "hot"]                        # correct answers

model = DecisionTreeClassifier()     # step 1: choose a model
model.fit(temperatures, labels)      # step 2: learn from examples

print("\nML answers (model learned the rule from data):")
for t in [20, 34, 36, 41]:
    prediction = model.predict([[t]])[0]   # step 3: predict for new inputs
    print(f"  {t} C ->", prediction)

# The tree found its own threshold. Let us print it.
threshold = model.tree_.threshold[0]
print(f"\nThreshold learned by the model: {threshold:.1f} C")

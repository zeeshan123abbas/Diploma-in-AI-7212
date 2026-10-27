# rules_vs_learning.py
# Compare a hand-written rule with a model that LEARNS the rule from data.

from sklearn.tree import DecisionTreeClassifier

# Each row: [hours_studied, classes_attended]
students = [[1, 4], [2, 6], [3, 5], [5, 10], [6, 12], [7, 11], [8, 14], [2, 3]]
# 1 = passed, 0 = failed (what actually happened)
results = [0, 0, 0, 1, 1, 1, 1, 0]

# --- Approach 1: a programmer writes the rule by hand ---
def rule_based(hours, classes):
    # The programmer guessed this rule
    if hours >= 4:
        return 1
    return 0

# --- Approach 2: the computer learns the rule from examples ---
model = DecisionTreeClassifier(max_depth=2, random_state=0)
model.fit(students, results)   # learning step

# Try both approaches on new students
new_students = [[4, 9], [3, 12], [9, 15]]
for hours, classes in new_students:
    by_rule = rule_based(hours, classes)
    by_model = model.predict([[hours, classes]])[0]
    print(f"hours={hours}, classes={classes} -> rule says {by_rule}, model says {by_model}")

print("\nThe rule never changes. The model changes when we give it new data.")

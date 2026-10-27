# classification_basics.py
# Classification = predict a CATEGORY (label), e.g. "Pass" or "Fail".
# This file shows the vocabulary: features, labels, train set, test set.

import pandas as pd
from sklearn.model_selection import train_test_split

# A tiny dataset: hours studied and attendance -> result
data = pd.DataFrame({
    "study_hours": [1, 2, 2.5, 3, 4, 5, 5.5, 6, 1.5, 3.5, 4.5, 0.5],
    "attendance":  [60, 65, 70, 75, 80, 90, 92, 95, 55, 78, 85, 50],
    "result":      ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass",
                    "Pass", "Pass", "Fail", "Pass", "Pass", "Fail"],
})

# 1) Features (X) = the inputs.  Label (y) = what we want to predict.
X = data[["study_hours", "attendance"]]
y = data["result"]
print("Features:\n", X.head(3))
print("Labels:", y.unique())
print("How many of each class:\n", y.value_counts())

# 2) Split: the model learns from the TRAIN part and is checked on the TEST part
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0, stratify=y   # stratify keeps the class mix equal
)
print("\nTrain rows:", len(X_train), " Test rows:", len(X_test))

# 3) A hand-made "model": a simple rule
def simple_rule(hours, attendance):
    if hours >= 3 and attendance >= 70:
        return "Pass"
    return "Fail"

predictions = [simple_rule(h, a) for h, a in zip(X_test["study_hours"], X_test["attendance"])]
print("\nTest actual:     ", list(y_test))
print("Rule predictions:", predictions)
correct = sum(p == a for p, a in zip(predictions, y_test))
print("Accuracy:", correct, "/", len(y_test))

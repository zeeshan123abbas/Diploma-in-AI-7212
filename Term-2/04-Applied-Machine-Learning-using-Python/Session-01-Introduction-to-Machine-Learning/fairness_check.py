# fairness_check.py
# A first look at bias: does the model work equally well for two groups?

import numpy as np
from sklearn.linear_model import LogisticRegression

rng = np.random.default_rng(0)

# Make a toy loan dataset. Group A has many rows, group B has only a few.
income_a = rng.normal(60, 15, 400)        # 400 applicants from city A
income_b = rng.normal(45, 15, 40)         # only 40 applicants from city B
income = np.concatenate([income_a, income_b])
group = np.array(["A"] * 400 + ["B"] * 40)

# True outcome: repaid the loan (1) or not (0). Rule is different for group B.
repaid = np.where(group == "A", income > 55, income > 35).astype(int)

# Train one model on everyone (only income is used as input)
model = LogisticRegression()
model.fit(income.reshape(-1, 1), repaid)
predicted = model.predict(income.reshape(-1, 1))

# Check accuracy for each group separately
for g in ["A", "B"]:
    mask = group == g
    acc = (predicted[mask] == repaid[mask]).mean()
    print(f"Group {g}: rows={mask.sum()}, accuracy={acc:.2f}")

print("\nIf one group gets much lower accuracy, the model is not fair to that group.")

# manova_wilks.py
# MANOVA idea: compare groups on SEVERAL outcome variables at once.
# We compute Wilks' lambda with numpy (small and readable).
import numpy as np
from scipy import stats

# Step 1: three teaching methods; two outcomes per student: [theory, practical]
groups = {
    "lecture": np.array([[65, 60], [70, 62], [68, 59], [72, 65], [66, 61]]),
    "video":   np.array([[70, 68], [74, 70], [73, 72], [78, 74], [71, 69]]),
    "project": np.array([[78, 82], [82, 85], [80, 84], [85, 88], [79, 83]]),
}

all_data = np.vstack(list(groups.values()))
grand_mean = all_data.mean(axis=0)

# Step 2: W = within-groups scatter matrix, B = between-groups scatter matrix
W = np.zeros((2, 2))
B = np.zeros((2, 2))
for data in groups.values():
    centred = data - data.mean(axis=0)
    W += centred.T @ centred
    diff = (data.mean(axis=0) - grand_mean).reshape(-1, 1)
    B += len(data) * (diff @ diff.T)

# Step 3: Wilks' lambda = det(W) / det(W + B)  (close to 0 = groups differ)
wilks = np.linalg.det(W) / np.linalg.det(W + B)
print("Wilks' lambda =", round(wilks, 4))

# Step 4: Bartlett's chi-square approximation for a p-value
n, p_vars, k = len(all_data), 2, len(groups)
chi2 = -(n - 1 - (p_vars + k) / 2) * np.log(wilks)
dof = p_vars * (k - 1)
p_value = 1 - stats.chi2.cdf(chi2, dof)
print(f"chi2 = {chi2:.2f}, df = {dof}, p = {p_value:.6f}")
print("Methods differ on the combined outcomes" if p_value < 0.05 else "No combined difference")

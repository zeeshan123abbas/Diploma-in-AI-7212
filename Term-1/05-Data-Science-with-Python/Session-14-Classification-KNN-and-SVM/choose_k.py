# choose_k.py
# Which k works best for KNN? Try several values with 5-fold cross-validation.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Breast cancer dataset: 569 patients, 30 measurements, label = malignant / benign
X, y = load_breast_cancer(return_X_y=True)

k_values = list(range(1, 26, 2))    # odd numbers avoid ties in voting
scores = []
for k in k_values:
    # pipeline = scale first, then KNN (scaling is re-learned inside every fold)
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
    # cross-validation: split data into 5 parts, test on each part once, average the 5 scores
    cv_scores = cross_val_score(model, X, y, cv=5)
    scores.append(cv_scores.mean())
    print(f"k = {k:>2}  average accuracy = {cv_scores.mean():.3f}")

best_k = k_values[scores.index(max(scores))]
print("\nBest k:", best_k)

plt.figure(figsize=(6, 4))
plt.plot(k_values, scores, marker="o")
plt.title("KNN: cross-validated accuracy for different k")
plt.xlabel("k (number of neighbours)")
plt.ylabel("Average accuracy (5 folds)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("choose_k.png")
print("Saved choose_k.png")

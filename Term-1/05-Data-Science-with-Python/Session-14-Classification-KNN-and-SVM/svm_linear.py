# svm_linear.py
# Support Vector Machine: find the widest "street" that separates two classes.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

# 1) Two groups of points that can be separated by a straight line
X, y = make_blobs(n_samples=60, centers=2, random_state=6, cluster_std=1.2)

# 2) Linear SVM
model = SVC(kernel="linear", C=1.0)
model.fit(X, y)
print("Number of support vectors per class:", model.n_support_)
print("Prediction for point (6, -6):", model.predict([[6, -6]])[0])

# 3) Draw points, the separating line and the margins
plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", s=30)

# make a grid over the plot and ask the model how far each grid point is from the line
xx, yy = np.meshgrid(np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 200),
                     np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 200))
grid = np.c_[xx.ravel(), yy.ravel()]
distance = model.decision_function(grid).reshape(xx.shape)
plt.contour(xx, yy, distance, levels=[-1, 0, 1], colors="black", linestyles=["--", "-", "--"])

# circle the support vectors
sv = model.support_vectors_
plt.scatter(sv[:, 0], sv[:, 1], s=120, facecolors="none", edgecolors="green", linewidths=1.5)
plt.title("Linear SVM: line, margins and support vectors")
plt.tight_layout()
plt.savefig("svm_linear.png")
print("Saved svm_linear.png")

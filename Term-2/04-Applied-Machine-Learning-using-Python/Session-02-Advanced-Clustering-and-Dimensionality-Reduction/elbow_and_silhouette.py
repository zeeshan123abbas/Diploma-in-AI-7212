# elbow_and_silhouette.py
# How many clusters? Try k = 2..8 and compare inertia and silhouette score.

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1) Make 300 points that really have 4 groups
X, _ = make_blobs(n_samples=300, centers=4, random_state=7)

k_values = range(2, 9)
inertias = []
silhouettes = []

# 2) Train one K-Means model for each k
for k in k_values:
    model = KMeans(n_clusters=k, n_init=10, random_state=0)
    labels = model.fit_predict(X)
    inertias.append(model.inertia_)                   # lower = tighter clusters
    silhouettes.append(silhouette_score(X, labels))   # higher = better separated
    print(f"k={k}  inertia={model.inertia_:8.1f}  silhouette={silhouettes[-1]:.3f}")

# 3) Plot both measures side by side
fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4))
left.plot(list(k_values), inertias, marker="o")
left.set_title("Elbow method (inertia)")
left.set_xlabel("k")
right.plot(list(k_values), silhouettes, marker="o", color="green")
right.set_title("Silhouette score")
right.set_xlabel("k")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "elbow_silhouette.png")
plt.savefig(out)
print("Chart saved to", out)

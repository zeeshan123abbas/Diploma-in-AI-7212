# dbscan_vs_kmeans.py
# K-Means expects round blobs. DBSCAN follows dense regions of any shape.

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

# 1) Two half-moon shapes (not round at all)
X, _ = make_moons(n_samples=300, noise=0.06, random_state=0)

# 2) Cluster with both algorithms
kmeans_labels = KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(X)
dbscan_labels = DBSCAN(eps=0.2, min_samples=5).fit_predict(X)

# DBSCAN marks noise points with the label -1
print("K-Means groups:", sorted(set(kmeans_labels.tolist())))
print("DBSCAN groups :", sorted(set(dbscan_labels.tolist())), "(-1 means noise)")

# 3) Plot side by side
fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4))
left.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap="coolwarm", s=15)
left.set_title("K-Means (cuts moons wrongly)")
right.scatter(X[:, 0], X[:, 1], c=dbscan_labels, cmap="coolwarm", s=15)
right.set_title("DBSCAN (follows the shape)")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dbscan_vs_kmeans.png")
plt.savefig(out)
print("Chart saved to", out)

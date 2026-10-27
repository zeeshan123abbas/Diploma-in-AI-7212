# pca_and_tsne.py
# Squeeze 64 pixel features (handwritten digits) down to 2 numbers so we can plot them.

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 1) 1797 images of digits 0-9, each image = 64 numbers
digits = load_digits()
X, y = digits.data, digits.target
print("Original shape:", X.shape)

# 2) PCA: a fast, linear method
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("PCA shape:", X_pca.shape)
print("Variance kept by 2 components:", round(pca.explained_variance_ratio_.sum() * 100, 1), "%")

# 3) t-SNE: slower, non-linear, good for pictures of clusters
X_tsne = TSNE(n_components=2, random_state=0, init="pca").fit_transform(X)

# 4) Plot both, colour = true digit
fig, (left, right) = plt.subplots(1, 2, figsize=(11, 5))
left.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="tab10", s=8)
left.set_title("PCA (2 components)")
right.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap="tab10", s=8)
right.set_title("t-SNE (2 components)")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pca_vs_tsne.png")
plt.savefig(out)
print("Chart saved to", out)

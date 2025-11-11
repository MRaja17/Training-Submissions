# Intermediate 1 — Apply NumPy on a Real Dataset (Iris)
# We'll use scikit-learn's built-in Iris dataset (no internet needed).
# Tasks: compute basic stats with NumPy and a simple linear algebra op.

import numpy as np
from sklearn.datasets import load_iris

data = load_iris()
X = data.data  # shape (150, 4), float64
y = data.target  # 0,1,2

# 1) Basic NumPy stats
means = X.mean(axis=0)
stds  = X.std(axis=0, ddof=1)
mins  = X.min(axis=0)
maxs  = X.max(axis=0)

# 2) Standardize features (vectorized)
X_std = (X - means) / stds

# 3) Covariance matrix (via arrays)
cov = np.cov(X_std, rowvar=False)  # shape (4,4)

# 4) Simple PCA via eigen-decomposition
evals, evecs = np.linalg.eigh(cov)
idx = np.argsort(evals)[::-1]
evals, evecs = evals[idx], evecs[:, idx]
X_pca2 = X_std @ evecs[:, :2]  # first two principal components

print("Feature means:", means.round(3))
print("Feature stds :", stds.round(3))
print("Feature mins :", mins.round(3))
print("Feature maxs :", maxs.round(3))
print("\nTop-2 eigenvalues:", evals[:2].round(3))
print("Explained variance ratio (top-2):", (evals[:2]/evals.sum()).round(3))
print("\nFirst 5 rows of PC scores:\n", np.round(X_pca2[:5], 3))

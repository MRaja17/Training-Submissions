# Intermediate 2 — NumPy with scikit-learn
# We'll build a very small pipeline that uses NumPy arrays throughout.

import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

data = load_iris()
X = data.data.astype(np.float64)  # ensure dtype
y = data.target

pipe = Pipeline([
    ("scaler", StandardScaler(with_mean=True, with_std=True)),
    ("clf", LogisticRegression(max_iter=1000, multi_class="auto"))
])

scores = cross_val_score(pipe, X, y, cv=5, n_jobs=None)
print("5-fold CV accuracy (mean ± std): %.3f ± %.3f" % (scores.mean(), scores.std()))

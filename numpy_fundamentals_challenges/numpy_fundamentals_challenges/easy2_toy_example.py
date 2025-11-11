# Easy 2 — Toy Example Using NumPy
# Goal: demonstrate vectorization, broadcasting, and simple stats.

import numpy as np

rng = np.random.default_rng(42)

# Imagine 5 students, 4 quizzes (scores out of 10)
scores = rng.integers(6, 10+1, size=(5,4))
# Apply a curve: +0.5 to each quiz (broadcasts to all rows)
curved = scores + 0.5

# Compute per-student average (vectorized)
student_avg = curved.mean(axis=1)
# Compute per-quiz average
quiz_avg = curved.mean(axis=0)

print("Original scores:\n", scores)
print("\nCurved scores (+0.5):\n", curved)
print("\nPer-student average:", student_avg)
print("Per-quiz average   :", quiz_avg)

# Hard 1 — Optimization via Vectorization & Memory Choices
# Compare pure Python loops vs NumPy vectorization and broadcasting.

import numpy as np
import time

def timeit(fn, *args, repeat=3, **kwargs):
    best = float("inf")
    out  = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        out = fn(*args, **kwargs)
        dt = time.perf_counter() - t0
        best = min(best, dt)
    return best, out

N = 2_000_000

# Task: y = a*x + b applied elementwise
a, b = 1.7, -0.9

# Pure Python list
x_list = list(range(N))

def python_loop(x_list, a, b):
    y = [a*xi + b for xi in x_list]
    return y

# NumPy vectorized
x_np = np.arange(N, dtype=np.float32)  # smaller dtype fits in cache better
def numpy_vec(x_np, a, b):
    return a*x_np + b

# Broadcasting experiment
A = np.random.default_rng(0).random((1000, 1000), dtype=np.float32)
row_add = np.random.default_rng(1).random((1, 1000), dtype=np.float32)

def broadcasting_add(A, row_add):
    return A + row_add  # no explicit loops

t_py, _ = timeit(python_loop, x_list, a, b, repeat=2)
t_np, _ = timeit(numpy_vec, x_np, a, b, repeat=5)
t_br, _ = timeit(broadcasting_add, A, row_add, repeat=3)

print(f"N={N:,}")
print(f"Python loop best time: {t_py:.4f} s")
print(f"NumPy vectorized best time: {t_np:.4f} s")
print(f"Broadcasting add 1000x1000 + 1x1000 best time: {t_br:.4f} s")
print("\nNotes:")
print("- Using float32 reduces memory bandwidth vs float64.")
print("- Vectorization and broadcasting eliminate Python loop overhead.")
print("- Contiguous arrays and aligned dtypes improve cache efficiency.")

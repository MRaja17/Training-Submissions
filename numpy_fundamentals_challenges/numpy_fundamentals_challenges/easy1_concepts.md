# Easy 1 — NumPy Fundamentals (In My Own Words)

**NumPy** is Python’s fast math toolkit for working with numbers in bulk. Its core idea is the **ndarray**: a contiguous block of typed numbers (like `float32` or `int64`) that supports **vectorized** operations. Instead of looping in Python, you tell NumPy what to do with entire arrays—and it runs optimized C code behind the scenes.

Key building blocks:
- **ndarray** — N‑dimensional, fixed‑type arrays (1D vectors, 2D matrices, etc.).
- **Vectorization** — operate on whole arrays at once (cleaner code, big speedups).
- **Broadcasting** — mix shapes smartly (e.g., add a 1×N row to many rows) without copying data.
- **Views vs Copies** — slicing usually creates *views* (no data duplication) which is memory‑efficient.
- **Dtypes & memory layout** — controlling `dtype` and contiguity matters for speed and memory.
- **uFuncs** — fast elementwise functions (e.g., `np.add`, `np.exp`, `np.sqrt`) with broadcasting support.
- **Linear algebra** — `np.dot`, `@`, `np.linalg.*` for matrix ops and decompositions.

In short, NumPy gives you compact, expressive code that’s **faster**, **clearer**, and **more scalable** than hand‑written Python loops.

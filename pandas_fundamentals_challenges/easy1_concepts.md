# Easy 1 — Pandas Fundamentals (in my own words)

Pandas is a Python library for **tabular data**—think spreadsheets and database tables. Its two core objects are:

- **Series**: one column of data with labels (an index).
- **DataFrame**: a table made of multiple Series (columns) that share the same index.

With Pandas you can:
- **Load** data from CSV/Excel/SQL/JSON into a DataFrame.
- **Inspect** and **clean** data (head/tail/info(), handle missing values, rename columns).
- **Filter & select** rows/columns with label- or boolean-based indexing (`.loc`, `.iloc`).
- **Transform** columns with vectorized operations (`.assign`, arithmetic, `str`, `dt`).
- **Aggregate** with `groupby` (sum, mean, count) to get insights.
- **Reshape** data (pivot, melt, stack/unstack, merge/join/concat).
- **Export** cleaned results back to files for downstream use.

The mental model: *DataFrame = labeled, columnar, in‑memory table* where you write concise, readable code to slice, transform, and summarize data efficiently.
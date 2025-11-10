# Easy 1 — Key concept of SQL Basics (in my own words)

**SQL (Structured Query Language)** is a standardized way to *describe what data you want* from tabular data rather than *how to get it*. 
At its core, SQL Basics are about:
- **Selecting rows and columns** with `SELECT ... FROM ...`.
- **Filtering** rows with `WHERE` (predicates like comparisons, `IN`, `LIKE`, `BETWEEN`, `IS NULL`).
- **Projecting** specific columns, computing **expressions/aliases**, and removing duplicates via `DISTINCT`.
- **Aggregating** and **grouping** with `GROUP BY` (e.g., `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) and refining grouped results with `HAVING`.
- **Joining** related tables with `JOIN` using key relationships.
- **Ordering** results with `ORDER BY`, and **limiting/paginating** with `LIMIT`/`OFFSET`.
- Relying on the **optimizer** to figure out an efficient plan, often improved with **indexes**.

In short: you *declare* the result shape (“what”), the engine figures out the steps (“how”).
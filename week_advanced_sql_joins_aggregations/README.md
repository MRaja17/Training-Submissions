# Advanced SQL Joins & Aggregations – Weekly Tasks

## Easy 1: Key Concepts in My Own Words

- **JOINs** let us combine rows from two or more tables using a related column (like `customer_id` in both tables).
- **INNER JOIN** returns only the rows where there is a match in both tables.
- **LEFT JOIN** returns all rows from the left table and matching rows from the right table. If there is no match, the right side will be `NULL`.
- **RIGHT JOIN** is the opposite of LEFT JOIN (all from the right table, matching from the left).
- **FULL OUTER JOIN** returns all rows from both tables. Where there is no match, the missing side is `NULL`.
- **Aggregations** use functions like `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` to combine many rows into one result (for example, total amount spent by each customer).
- **GROUP BY** groups rows that share the same value in one or more columns, so we can apply aggregations per group (e.g., per customer or per product).
- **HAVING** filters groups *after* aggregation (like `WHERE`, but works on grouped/aggregated results).

This README collects explanations and links to the other files:

- `easy_toy_example.sql` – toy example with JOINs and aggregations.
- `intermediate_real_dataset.ipynb` – pandas joins + aggregations on a small dataset.
- `hard_performance_notes.md` – notes on SQL performance optimization.
- `mini_project/mini_project.ipynb` – end-to-end mini project.


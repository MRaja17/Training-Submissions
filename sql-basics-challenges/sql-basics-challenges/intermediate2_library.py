"""
Intermediate 2 — Implement SQL Basics using an appropriate library (pandas + sqlite3)

This script shows basic SQL operations through Python:
- Loading CSVs to SQLite
- Running SQL queries from Python
- Fetching results into pandas for further analysis
"""
import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("/mnt/data/sql-basics-challenges/data/sales.sqlite")

con = sqlite3.connect(DB_PATH)

# 1) Run the toy example query and save results
toy = pd.read_sql_query(
    """
    SELECT product_name, category, price
    FROM products
    ORDER BY price DESC
    LIMIT 5;
    """,
    con
)
toy.to_csv(DB_PATH.parent / "toy_example_results.csv", index=False)

# 2) Run intermediate queries
top_customers = pd.read_sql_query(
    """
    SELECT customer_id, SUM(line_total) AS total_spend
    FROM v_order_details
    GROUP BY customer_id
    ORDER BY total_spend DESC
    LIMIT 5;
    """, con
)

monthly_rev = pd.read_sql_query(
    """
    SELECT strftime('%Y-%m', order_date) AS year_month, SUM(line_total) AS monthly_revenue
    FROM v_order_details
    GROUP BY year_month
    ORDER BY year_month;
    """, con
)

top_customers.to_csv(DB_PATH.parent / "top_customers.csv", index=False)
monthly_rev.to_csv(DB_PATH.parent / "monthly_revenue.csv", index=False)

print("Saved:", DB_PATH.parent / "toy_example_results.csv")
print("Saved:", DB_PATH.parent / "top_customers.csv")
print("Saved:", DB_PATH.parent / "monthly_revenue.csv")
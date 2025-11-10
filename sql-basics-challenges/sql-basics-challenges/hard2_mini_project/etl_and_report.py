import sqlite3, os
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

BASE = Path("/mnt/data/sql-basics-challenges")
DATA = BASE / "data"
OUT = Path("/mnt/data/sql-basics-challenges/hard2_mini_project") / "outputs"
OUT.mkdir(exist_ok=True, parents=True)

db_path = DATA / "sales.sqlite"
con = sqlite3.connect(db_path)

# Recompute KPIs using SQL
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

# Save tables
top_customers.to_csv(OUT / "top_customers.csv", index=False)
monthly_rev.to_csv(OUT / "monthly_revenue.csv", index=False)

# Plot trend (matplotlib, single plot, no specific colors)
plt.figure()
plt.plot(monthly_rev['year_month'], monthly_rev['monthly_revenue'], marker='o')
plt.title("Monthly Revenue")
plt.xlabel("Year-Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue.png")
plt.close()

# Write simple markdown report
summary = []
summary.append("# Sales Insights — Report\n")
summary.append("## Top Customers (by total spend)\n")
summary.append(top_customers.to_markdown(index=False))
summary.append("\n\n## Monthly Revenue (table)\n")
summary.append(monthly_rev.to_markdown(index=False))

report_path = Path("/mnt/data/sql-basics-challenges/hard2_mini_project") / "report.md"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(summary))

print("Wrote:", report_path)
print("Wrote:", OUT / "top_customers.csv")
print("Wrote:", OUT / "monthly_revenue.csv")
print("Wrote:", OUT / "monthly_revenue.png")
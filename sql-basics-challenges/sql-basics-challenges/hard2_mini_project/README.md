# Hard 2 — Mini Project: Sales Insights (End-to-End)

**Goal:** Build a simple end-to-end pipeline:
1. **Extract/Load** CSVs → SQLite
2. **Transform/Analyze** with SQL (KPIs + Trends)
3. **Publish** a lightweight report and chart

## How to run
```bash
python etl_and_report.py
```

Outputs:
- `outputs/monthly_revenue.png` — revenue trend chart
- `outputs/top_customers.csv` — top spenders
- `outputs/monthly_revenue.csv` — monthly revenue table
- `report.md` — short written summary with key findings
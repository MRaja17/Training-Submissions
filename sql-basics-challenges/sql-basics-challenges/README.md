# SQL Basics — Weekly Challenges

This folder contains deliverables for the challenge set (Easy → Hard). It is repo-ready (Markdown, SQL scripts, Python code, data, and figures).

## Structure
- `easy1_concepts.md` — explanation of core SQL Basics
- `easy2_toy_example.sql` — simple SQL query (top 5 products by price)
- `intermediate1_real_dataset.sql` — aggregate queries over a realistic schema
- `intermediate1_explanation.md` — narrative explanation of results
- `intermediate2_library.py` — pandas + SQLite implementation for running queries and saving results
- `hard1_add_indexes.sql` & `hard1_optimization.md` — performance tuning (indexes + guidance)
- `hard2_mini_project/` — end-to-end mini project (ETL, KPIs, chart, report)
- `data/` — CSVs and a `sales.sqlite` database

## Quickstart (local)
```bash
# (optional) create venv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install pandas matplotlib

# run library demo
python intermediate2_library.py

# run end-to-end mini project
cd hard2_mini_project
python etl_and_report.py
```

## GitHub submission (example)
```bash
# from your local clone of MRaja17/Training-Submissions
mkdir -p SQL/Week_SQL_Basics
cp -r /path/to/sql-basics-challenges/* SQL/Week_SQL_Basics/

git checkout -b feature/sql-basics-challenges
git add SQL/Week_SQL_Basics
git commit -m "Add SQL Basics challenges (easy→hard) with data and mini project"
git push -u origin feature/sql-basics-challenges

# then open a Pull Request on GitHub
```